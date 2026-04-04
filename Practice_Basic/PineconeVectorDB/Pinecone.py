from humanize import metric
from pinecone import Pinecone, ServerlessSpec
import os, time
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import uuid
from data import data as seed_data
load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
# print(client)

# assistants = pc.assistant.list_assistants()
# print(assistants)

# assistant_name = f"example-assistant-{int(time.time())}"
# print(assistant_name)


# ##################### Create assistant if not exists ####################################
# if assistant_name not in [a.name for a in assistants]:
#     assistant = pc.assistant.create_assistant(
#         assistant_name=assistant_name,
#         instructions="Answer in polite, short sentences. Use American English spelling and vocabulary.",
#         timeout=30  # Wait 30 seconds for assistant operation to complete.
#     )
#     print(assistant)
# else:
#     print("Assistant already exists")
###########################################################################################


###########################################################################################
# response = client.embeddings.create(
#     input="Paracetamol is used for fever",
#     model="text-embedding-3-small"
# )
# vector = response.data[0].embedding
# print(len(vector))  # 384 for text-embedding-3-small
###########################################################################################

# vector = [0.1] * 1536
# print(len(vector))


# model = SentenceTransformer('all-MiniLM-L6-v2')
# query = "Paracetamol is used for fever"
# query_vector = model.encode(query)
# print(query_vector)  # ~384
# print(len(query_vector))  # ~384



# ############################## Delete old index if exists #####################################
# if "my-index" in pc.list_indexes().names():
#     pc.delete_index("my-index")
#     print("Old index deleted")
#     time.sleep(5)
#################################################################################################
    
    


def create_index_if_not_exists(
    index_name="my-index",
    dimension=384,
    metric="cosine",
    cloud="aws",
    region="us-east-1"
):
    """
    Create Pinecone index if it does not already exist
    
    :param index_name: name of index
    :param dimension: embedding dimension
    :param metric: similarity metric (cosine / dotproduct / euclidean)
    :param cloud: cloud provider
    :param region: region
    """
    try:
        existing_indexes = pc.list_indexes().names()

        if index_name not in existing_indexes:
            pc.create_index(
                name=index_name,
                dimension=dimension,
                metric=metric,
                spec=ServerlessSpec(
                    cloud=cloud,
                    region=region
                )
            )

            print(f"✅ Index '{index_name}' created successfully")
            time.sleep(5)  # wait for readiness
        else:
            print(f"ℹ️ Index '{index_name}' already exists")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
      

def store_vectors(data, batch_size=100):
    """
    Store text data into Pinecone with embeddings
    :param data: list of text strings
    :param batch_size: number of records per batch
    """
    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # #Store vector
    # index.upsert([
    #     ("1", model.encode("Paracetamol is used for fever").tolist()),
    #     ("2", model.encode("Ibuprofen reduces pain").tolist())
    # ])
    
    try:
        # Connect to index
        index = pc.Index("my-index")
        
        vectors = []
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(data)
        for i, text in enumerate(data):
            vector = {
                "id": str(uuid.uuid4()),  # unique ID for each record
                "values": embeddings[i].tolist(),
                "metadata": {"text": text}
            }
            vectors.append(vector)

            # Batch insert
            if len(vectors) >= batch_size:
                index.upsert(vectors)
                vectors = []

        # Insert remaining
        if vectors:
            index.upsert(vectors)

        return "Data inserted successfully ✅"

    except Exception as e:
        return f"Error: {str(e)}"


def search_vectors(query, top_k=2, return_scores=True):
    """
    Search similar vectors in Pinecone based on query string
    :param query: user query string
    :param top_k: number of results
    :param return_scores: include similarity score or not
    :return: list of results
    """
    try:
        # Connect to index
        index = pc.Index("my-index")
        
        model = SentenceTransformer('all-MiniLM-L6-v2')

        # Step 1: Convert query to vector
        query_vector = model.encode(query).tolist()

        # Step 2: Search in Pinecone
        result = index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )

        # print("Raw search result:", result)
        
        matches = result.get("matches", [])
        if not matches:
            return []

        # Step 3: Format output
        response = []
        for match in matches:
            item = {
                "text": match["metadata"].get("text", "")
            }

            if return_scores:
                item["score"] = match.get("score")

            response.append(item)

        return response

    except Exception as e:
        return {"error": str(e)}


def dynamic_data_generation() -> list:
    diseases = ["fever", "cold", "diabetes", "infection", "pain", "allergy"]
    medicines = ["Paracetamol", "Ibuprofen", "Aspirin", "Cetirizine", "Metformin"]
    actions = ["treats", "helps with", "reduces", "prevents", "controls"]
    data = []
    for med in medicines:
        for disease in diseases:
            for action in actions:
                sentence = f"{med} {action} {disease}"
                data.append(sentence)

    return data


# ************************************************************************************************
def main():
    
    create_index_if_not_exists()

    while True:
        print("\n===== MENU =====")
        print("1. Insert data")
        print("2. Search")
        print("3. Dynamic data generation")
        print("4. Store multiple vectors with metadata")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\nEnter sentences (comma separated):")
            user_input = input(">> ")
            data = [x.strip() for x in user_input.split(",")]
            result = store_vectors(data)
            print(result)

        elif choice == "2":
            query = input("\nEnter your query: ")
            # Search vectors
            results = search_vectors(query)
            for i, r in enumerate(results, start=1):
                if r["score"] > 0.5:
                    print(f"{i}. {r['text']} (Score: {round(r['score'], 2)})")

        elif choice == "3":
            print("\nGenerating dynamic data...")
            generated_data = dynamic_data_generation()
            for item in generated_data:
                print(item)
                
        elif choice == "4":
            print("\nStoring seed data...")
            result = store_vectors(seed_data)
            print(result)
                
        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("Invalid choice")
# ************************************************************************************************

print("\n\n Starting Pinecone Vector DB demo...", flush=True, end="\n\n", sep="")
if __name__ == "__main__":
    main()
    