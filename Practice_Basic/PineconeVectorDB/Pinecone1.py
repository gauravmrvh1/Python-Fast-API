from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
import os, time
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = "my-index"

# ✅ Step 1: Create index if not exists
if INDEX_NAME not in pc.list_indexes().names():
    print("⚙️ Creating new index...")
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,  # SentenceTransformer dimension
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    time.sleep(5)
    print("✅ Index created")

# Connect index
index = pc.Index(INDEX_NAME)

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')


def ask_ai(question):
    print("\n🔍 User Question:", question)

    # Step 2: Embed query
    query_vector = model.encode(question).tolist()

    # Step 3: Search Pinecone
    result = index.query(
        vector=query_vector,
        top_k=3,
        include_metadata=True
    )

    matches = result['matches']

    # Step 4: Extract results
    answers = [m['metadata']['text'] for m in matches]
    scores = [m['score'] for m in matches]

    best_score = scores[0] if scores else 0
    print("\n📊 Confidence Score:", round(best_score, 2))

    # ❌ No OpenAI → fallback simple message
    if best_score < 0.6:
        print("\n⚠️ No strong match found")

        fallback = "Sorry, I don't have enough data. Please consult a doctor."

        print("\n🤖 Response:")
        print(fallback)

        # ✅ Optional auto-learn (store question only)
        index.upsert([{
            "id": "q_" + str(time.time()),
            "values": model.encode(question).tolist(),
            "metadata": {
                "text": question,
                "type": "user_query"
            }
        }])

        return fallback

    # ✅ Good match → show results
    print("\n✅ Best Matches:\n")

    formatted = []
    for i, (ans, score) in enumerate(zip(answers, scores)):
        line = f"{i+1}. {ans}  (Score: {round(score,2)})"
        print(line)
        formatted.append(ans)

    final_answer = formatted[0]

    print("\n🎯 Final Answer:")
    print(final_answer)

    return final_answer


# 🔥 Sample data insert (run once if DB empty)
def seed_data():
    data = [
        "Paracetamol is used for fever",
        "Ibuprofen reduces pain",
        "Aspirin helps with inflammation",
        "Cough syrup helps in cold"
    ]

    vectors = []
    for i, text in enumerate(data):
        vectors.append({
            "id": f"doc_{i}",
            "values": model.encode(text).tolist(),
            "metadata": {"text": text}
        })

    index.upsert(vectors)
    print("✅ Initial data inserted")


# 👉 Uncomment first time
# seed_data()


# 🔥 Interactive loop
while True:
    user_input = input("\n💬 Ask something (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    ask_ai(user_input)