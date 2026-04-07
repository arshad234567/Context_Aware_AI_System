import tokenizer
from chonkie import RecursiveChunker, RecursiveRules
from doc_reader_utils import get_documents


chunker = RecursiveChunker(
    tokenizer_or_token_counter="gpt2",
    chunk_size=128,    #
    rules=RecursiveRules() # rules on which chunking should be done.
)


docs = get_documents()

for docs in docs :
    chunks = chunker.chunk(doc.text)

    for chunk in chunks:
        print(f"Chunk text: {chunk.text}")
        print(f"Token count: {chunk.token_count}")
        print(f"Start index: {chunk.start_index}")
        print(f"End index: {chunk.end_index}")


