from fastapi import FastAPI, Request
from twilio.twiml.messaging_response import MessagingResponse
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os, time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Init
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("my-index")

model = SentenceTransformer('all-MiniLM-L6-v2')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/whatsapp")
async def whatsapp_bot(request: Request):
    form = await request.form()
    user_msg = form.get("Body")

    # Step 1: Embed query
    query_vector = model.encode(user_msg).tolist()

    # Step 2: Search Pinecone
    result = index.query(
        vector=query_vector,
        top_k=2,
        include_metadata=True
    )

    matches = result['matches']
    best_score = matches[0]['score'] if matches else 0

    # Step 3: Decide response
    if best_score > 0.6:
        answer = matches[0]['metadata']['text']
    else:
        # fallback to AI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Give safe medical advice: {user_msg}"
            }]
        )
        answer = response.choices[0].message.content

        # auto-learn
        index.upsert([{
            "id": "auto_" + str(time.time()),
            "values": model.encode(answer).tolist(),
            "metadata": {"text": answer}
        }])

    # Step 4: Send reply
    twilio_resp = MessagingResponse()
    twilio_resp.message(answer)

    return str(twilio_resp)