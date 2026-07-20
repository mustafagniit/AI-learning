from openai import OpenAI
import json
import numpy as np
client = OpenAI(api_key="")

document = """
Python is a popular programming language. It is easy to learn and has a large ecosystem.

Machine learning is one of Python's most popular applications. Popular libraries include Scikit-learn, TensorFlow, and PyTorch.

Pandas is used for data analysis. It provides DataFrames for working with tabular data.

Matplotlib is used for creating visualizations such as line charts, bar charts, and scatter plots.
"""


prompt = f"""
You are an expert document chunker.

Read the document carefully.

Split it into meaningful chunks.

Rules:
- One topic per chunk.
- Keep related sentences together.
- Return JSON.

Document:

{document}
"""

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print(response.output_text)


# -----------------------------------------
# Step 4: Convert LLM response into chunks
# -----------------------------------------

chunks_json = json.loads(
    response.output_text
)

chunks = []


# for item in chunks_json:
#     chunks.append(
#         item["text"]
#     )


for item in chunks_json["chunks"]:
    chunks.append(item["text"])

print("\nCreated Chunks:")
print("----------------")

for i, chunk in enumerate(chunks):
    print(
        f"\nChunk {i+1}:"
    )
    print(chunk)



    # -----------------------------------------
# Step 5: Create embeddings
# Each chunk becomes a vector
# -----------------------------------------

vector_database = []


for chunk in chunks:

    embedding_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )


    vector = (
        embedding_response
        .data[0]
        .embedding
    )


    vector_database.append(
        {
            "text": chunk,
            "embedding": vector
        }
    )


print("\nStored vectors:")
print(len(vector_database))

# -----------------------------------------
# Step 6: Create similarity function
# -----------------------------------------

def cosine_similarity(vector1, vector2):

    vector1 = np.array(vector1)
    vector2 = np.array(vector2)


    return np.dot(vector1, vector2) / (
        np.linalg.norm(vector1)
        *
        np.linalg.norm(vector2)
    )




# -----------------------------------------
# Step 7: User Question
# -----------------------------------------

question = (
    "Which Python library is used for data analysis?"
)



# -----------------------------------------
# Step 8: Convert question into embedding
# -----------------------------------------

question_embedding_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=question
)


question_vector = (
    question_embedding_response
    .data[0]
    .embedding
)

print("\nPrinting vector question:")
print(question_vector)





# -----------------------------------------
# Step 9: Search our temporary vector DB
# -----------------------------------------

search_results = []


for item in vector_database:


    score = cosine_similarity(
        question_vector,
        item["embedding"]
    )


    search_results.append(
        {
            "text": item["text"],
            "score": score
        }
    )



# Sort highest similarity first

search_results.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Get best matching chunks

top_chunks = search_results[:2]



print("\nRetrieved Chunks:")
print("------------------")



for result in top_chunks:
    print(
        "\nScore:",
        result["score"]
    )

    print(
        result["text"]
    )

# -----------------------------------------
# Step 10: Give retrieved context to LLM
# -----------------------------------------

context = "\n\n".join(
    [
        item["text"]
        for item in top_chunks
    ]
)



final_prompt = f"""

Answer the question using only the context below.

Context:

{context}


Question:

{question}

"""


answer = client.responses.create(
    model="gpt-5.5",
    input=final_prompt
)



print("\nFinal Answer:")
print("----------------")

print(
    answer.output_text
)