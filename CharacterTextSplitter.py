from langchain_text_splitters import CharacterTextSplitter

text = """
,It provides tools for loading, splitting, embedding, and retrieving documents.
"""

splitter = CharacterTextSplitter(
    separator='',
    chunk_size=50,
    chunk_overlap=10,
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 20)