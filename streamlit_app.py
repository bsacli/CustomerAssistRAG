import streamlit as st
import requests
import uuid

# Streamlit app setup
st.set_page_config(page_title="Customer Assist API", page_icon="🤖", layout="wide")
st.title("Customer Assist")

# Base URL for the API
base_url = "http://localhost:5000"

# Initialize session state for question, answer, and conversation ID
if 'question' not in st.session_state:
    st.session_state.question = ""
if 'answer' not in st.session_state:
    st.session_state.answer = ""
if 'conversation_id' not in st.session_state:
    st.session_state.conversation_id = ""

# Function to ask a question to the API
def ask_question(url, question):
    data = {"question": question}
    response = requests.post(f"{url}/question", json=data)
    return response.json()

# Function to send feedback to the API
def send_feedback(url, conversation_id, feedback):
    feedback_data = {"conversation_id": conversation_id, "feedback": feedback}
    response = requests.post(f"{url}/feedback", json=feedback_data)
    return response.status_code

# Main content
st.session_state.question = st.text_input("Enter your question:", value=st.session_state.question)

if st.button("Get Answer"):
    if st.session_state.question:
        with st.spinner("Getting answer..."):
            response = ask_question(base_url, st.session_state.question)
        
        st.session_state.answer = response.get("answer", "No answer provided")
        st.session_state.conversation_id = response.get("conversation_id", str(uuid.uuid4()))

if st.session_state.answer:
    st.subheader("Answer:")
    st.write(st.session_state.answer)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👍 Positive"):
            status = send_feedback(base_url, st.session_state.conversation_id, 1)
            st.success(f"Positive feedback sent. Status code: {status}")
    with col2:
        if st.button("👎 Negative"):
            status = send_feedback(base_url, st.session_state.conversation_id, -1)
            st.error(f"Negative feedback sent. Status code: {status}")
    with col3:
        if st.button("⏭️ Skip feedback"):
            st.info("Feedback skipped.")
else:
    st.warning("Please enter a question and click 'Get Answer'.")
