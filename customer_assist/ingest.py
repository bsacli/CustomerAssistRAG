import os
import pandas as pd
import json
import minsearch


DATA_PATH = os.getenv("DATA_PATH", "../Data/documents-with-ids.json")


def load_index(data_path=DATA_PATH):
    
    with open(data_path, 'rt') as f_in:
        documents = json.load(f_in)

    index = minsearch.Index(
                            text_fields=['intent', 'question', 'response', 'category'],
                            keyword_fields=['id']
                            )

    index.fit(documents)
    return index