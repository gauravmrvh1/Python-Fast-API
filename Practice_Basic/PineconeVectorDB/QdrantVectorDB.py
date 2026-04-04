from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()


qdrant_client = QdrantClient(
    url=os.getenv("Qdrential_API_URL"),
    api_key=os.getenv("Qdrential_API_KEY")
)

print(qdrant_client.get_collections())