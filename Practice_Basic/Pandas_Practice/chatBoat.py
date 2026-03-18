# pip install pandas faiss-cpu sentence-transformers fastapi uvicorn
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

df = pd.read_csv("faq.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("\n **************** model *********************************************************")
print(model)
print("\n **************** model *********************************************************")

embeddings = model.encode(df["question"].tolist())
print("\n **************** embeddings ***************************************************** \n")
print(embeddings)
print("\n **************** embeddings ***************************************************** \n")


vectors = np.array(embeddings).astype("float32")
print("\n **************** vectors ***************************************************** \n")
print(vectors)
print("\n **************** vectors ***************************************************** \n")


print("\n **************** vectors.shape *****************************************************")
dimension = vectors.shape[1]
print(dimension)
print("\n **************** vectors.shape ***************************************************** \n")


index = faiss.IndexFlatL2(dimension)

index.add(vectors)

def chatbot(query):

    query_vector = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vector,1)

    answer = df.iloc[indices[0][0]]["answer"]

    return answer


# print(chatbot("How to reset password?"))
# print(chatbot("I forgot my password"))
# print(chatbot("support connect"))
# print(chatbot("refund kaise milega"))
# print(chatbot("How to contact support"))
# print(chatbot("Unable to login due to password"))
# print(chatbot("pagal bana rakha paise kaise milenge"))
print(chatbot("mera order kal cancel hua tha"))



