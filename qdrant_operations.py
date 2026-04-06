from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

from chonkie import Pipeline

load_dotenv()

qdrant_client = QdrantClient(
    url="https://de60ef6a-2aef-4b35-81e4-4bf2db1e2e68.eu-central-1-0.aws.cloud.qdrant.io",
    api_key=os.getenv("QDRANT_API_KEY"),
)

docs = (Pipeline()
    .fetch_from("file", dir="./knowledge_base", ext=[".txt", ".md"])
    .process_with("text")
    .chunk_with("semantic", threshold=0.8, chunk_size=1024)
    .refine_with("overlap", context_size=100)
    .store_in("qdrant",
              collection_name="knowledge",
              url="http://localhost:6333")
    .run())

print(f"Ingested {len(docs)} documents")