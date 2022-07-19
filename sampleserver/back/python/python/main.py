import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
from flask import Flask, request

app = Flask(__name__)

def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

def get_dataset():
    df = pd.read_csv('wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df
def result(value) :
    model = cached_model()
    df = get_dataset()
    user_input = value
    embedding = model.encode(user_input)
    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]
    return answer['챗봇']

@app.route('/', methods=['GET','POST'])
def request_main():
    value = request.json['info']
    abc = result(value)
    return abc

if __name__ == '__main__':
    app.run()