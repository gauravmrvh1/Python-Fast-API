import pandas as pd
import numpy as np
import faiss
import json
from sentence_transformers import SentenceTransformer

df = pd.read_csv("faq.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(df["question"].tolist())

vectors = np.array(embeddings).astype("float32")

dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(vectors)

# memory store
chat_memory = []

def chatbot(query):

    global chat_memory

    chat_memory.append(("User",query))

    query_vector = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vector,1)

    answer = df.iloc[indices[0][0]]["answer"]

    chat_memory.append(("Bot",answer))

    return {
        "answer":answer,
        "memory":chat_memory
    }
    
def save_memory(memory):
    with open("memory.json","w") as f:
        json.dump(memory,f)
    
# print(chatbot("mera order kal cancel hua tha"))
# print(chatbot("pagal bana rakha paise kaise milenge"))
# response = (chatbot("I forgot my password"))
response = (chatbot("pagal bana rakha paise kaise milenge"))
save_memory(response['memory'])