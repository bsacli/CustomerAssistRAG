import psycopg2
from datetime import datetime

def add_sample_data():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="customer_support",
            user="admin",
            password="admin",
        )
        print("Database connection successful!")

        with conn.cursor() as cur:
            # Sample data for the conversations table
            cur.execute("""
                INSERT INTO conversations 
                (id, question, response, model_used, response_time, relevance, 
                relevance_explanation, prompt_tokens, completion_tokens, total_tokens,
                eval_prompt_tokens, eval_completion_tokens, eval_total_tokens, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                'test_conversation_1',  # id
                'What is the return policy?',  # question
                'Our return policy lasts 30 days...',  # response
                'phi3',  # model_used
                0.5,  # response_time
                'RELEVANT',  # relevance
                'The answer accurately addresses the question.',  # relevance_explanation
                10,  # prompt_tokens
                15,  # completion_tokens
                25,  # total_tokens
                5,  # eval_prompt_tokens
                10,  # eval_completion_tokens
                15,  # eval_total_tokens
                datetime.now()  # timestamp
            ))
            conn.commit()
            print("Sample data added to conversations table.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    add_sample_data()
