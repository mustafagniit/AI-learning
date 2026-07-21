import logging
from openai import OpenAI
from openai import OpenAIError
import os

# Configure logger
logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def create_embedding(text: str):

    if not text or not text.strip():
        # logger.warning("Embedding request received with empty text")
        raise ValueError("Text cannot be empty")

    try:
        # logger.info("Creating embedding for text length: %s", len(text))

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        embedding = response.data[0].embedding

        # logger.info(
        #     "Embedding created successfully. Vector size: %s",
        #     len(embedding)
        # )

        return embedding

    except OpenAIError as e:
        logger.error(
            "OpenAI API error while creating embedding: %s",
            str(e),
            exc_info=True
        )
        raise

    except Exception as e:
        logger.error(
            "Unexpected error while creating embedding: %s",
            str(e),
            exc_info=True
        )
        raise