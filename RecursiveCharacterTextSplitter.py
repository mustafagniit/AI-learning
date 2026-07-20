from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a framework for building applications powered by large language models.

It helps developers load documents, split text into chunks, create embeddings,
store vectors, retrieve relevant information, and interact with LLMs.

RecursiveCharacterTextSplitter attempts to split text by larger separators first,
such as paragraphs and sentences, before falling back to smaller separators like
spaces or individual characters.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 50)