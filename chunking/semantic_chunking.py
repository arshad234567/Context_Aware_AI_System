from chonkie import SemanticChunker

from doc_reader_utils  import get_document

chunker = SemanticChunker(
    embedding_model="minishlab/potion-base-32M",  # Default model
    threshold=0.8,                               # Similarity threshold (0-1)
    chunk_size=2048,                             # Maximum tokens per chunk
    similarity_window=3,                         # Window for similarity calculation
    skip_window=0                                # Skip-and-merge window (0=disabled)
)

chunker = SemanticChunker(
    embedding_model="minishlab/potion-base-32M",
    threshold=0.7,
    chunk_size=2048,
    skip_window=1  # Enable merging of similar non-consecutive groups
)