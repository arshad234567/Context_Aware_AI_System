from chonkie import SentenceChunker
from doc_reader_utils import get_documents

chunker = SentenceChunker(
    tokenizer_or_token_counter="gpt2",
    chunk_size=128,
    chunk_overlap=30,
    min_sentences_per_chunk=1,
)

docs = get_documents()

for doc in docs:
    chunks = chunker.chunk(doc.text)

    for chunk in chunks:
        print(f"Chunk text: {chunk.text}")
        print(f"Token count: {chunk.token_count}")
        print(f"Start index: {chunk.start_index}")
        print(f"End index: {chunk.end_index}")
