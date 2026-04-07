from chonkie import LateChunker, RecursiveRules

from chunking.doc_reader_utils import get_documents

chunker = LateChunker(
    embedding_model="nomic-ai/modernbert-embed-base",
    chunk_size=2048,
    rules=RecursiveRules(),
    min_characters_per_chunk=24,
)

docs = get_documents()

for docs in docs :
    chunks = chunker.chunk(doc.text)

    for chunk in chunks:
        print(f"Chunk text: {chunk.text}")
        print(f"Token count: {chunk.token_count}")
        print(f"Start index: {chunk.start_index}")
        print(f"End index: {chunk.end_index}")