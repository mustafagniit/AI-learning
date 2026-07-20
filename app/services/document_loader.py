import fitz

def load_pdf(file_path):
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    return text

def split_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):

        end = start + chunk_size

        chunk=text[start:end]

        chunks.append(chunk)


        start = end - overlap


    return chunks
