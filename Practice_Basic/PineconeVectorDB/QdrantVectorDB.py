from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from helpers.qdrant_helper import normalize_qdrant_response
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import logging
from data import data as seed_data

load_dotenv()

# =========================
# LOGGING CONFIG
# =========================
logging.basicConfig(
    level=logging.INFO,  # DEBUG / INFO / ERROR
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# =========================
# 1. Initialize Client
# =========================
def get_qdrant_client():
    try:
        client = QdrantClient(
            url=os.getenv("Qdrential_API_URL"),
            api_key=os.getenv("Qdrential_API_KEY")
        )
        logger.info("************************Connected to Qdrant ✅************************")
        return client
    except Exception as e:
        logger.error(f"Error connecting to Qdrant: {e}")
        raise


# =========================
# 2. Load Model
# =========================
def get_model():
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        logger.info("************************Model loaded ✅************************")
        return model
    except Exception as e:
        logger.error(f"Model load failed: {e}")
        raise


# =========================
# 3. Create Collection
# =========================
def create_collection(client, collection_name, vector_size=384):
    try:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config={
                "size": vector_size,
                "distance": "Cosine"
            }
        )
        logger.info(f"Collection '{collection_name}' ready ✅")
    except Exception as e:
        logger.error(f"Collection creation failed: {e}")
        raise


# =========================
# 4. Generate Vector
# =========================
def generate_vector(model, text):
    try:
        return model.encode(text).tolist()
    except Exception as e:
        logger.error(f"Vector generation failed: {e}")
        raise


# =========================
# 5. Insert Data
# =========================
def insert_data(client, collection_name, data, model):
    try:
        points = []

        for idx, text in enumerate(data, start=1):
            vector = generate_vector(model, text)

            points.append({
                "id": idx,
                "vector": vector,
                "payload": {"text": text}
            })

        client.upsert(
            collection_name=collection_name,
            points=points
        )

        logger.info("************************Data inserted ✅************************")

    except Exception as e:
        logger.error(f"Data insert failed: {e}")
        raise


# =========================
# 6. Search Data
# =========================
def search_data(client, collection_name, query_text, model, limit=3):
    try:
        query_vector = generate_vector(model, query_text)

        response = client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=limit
        )

        logger.info("************************Search executed successfully ✅************************")

        return normalize_qdrant_response(response)

    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise


# =========================
# 7. List Collections
# =========================
def list_collections(client):
    try:
        return client.get_collections()
    except Exception as e:
        logger.error(f"Fetch collections failed: {e}")
        raise


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    try:
        client = get_qdrant_client()
        model = get_model()

        logger.info(list_collections(client))

        collection_name = "test"

        create_collection(client, collection_name)

        insert_data(client, collection_name, seed_data, model)

        results = search_data(client, collection_name, "medicine for fever", model)

        logger.info("************************Search Results:************************")
        for r in results:
            logger.info(r.payload)

    except Exception as e:
        logger.critical(f"Fatal error: {e}")