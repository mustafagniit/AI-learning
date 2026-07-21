import chromadb

from services.embedding import create_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)

def store_chunks(chunks, filename):
    for index, chunk in enumerate(chunks):
        vector = create_embedding(chunk)
        collection.add(

            ids=[
                f"{filename}_ {index}"
            ],
            documents=[
                chunk
            ],
            embeddings=[
                vector
            ],
            metadatas=[
                {
                    "source": filename
                }
            ]
        )

def search_documents(question):
    question_vector = create_embedding(question)
    result = collection.query(
        query_embeddings=[
            question_vector
        ],
        n_results=3
    )
    return result["documents"][0]

