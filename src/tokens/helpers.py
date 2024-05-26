import tiktoken

from src.logger import logger


def split_text_into_tokens(text: str, max_tokens: int, encoding_model="gpt-3.5-turbo", encoding_name="cl100k_base"):
    """
    Splits a long text into chunks based on the specified maximum token length.

    Parameters:
    - text (str): The input text to be split.
    - max_tokens (int): The maximum number of tokens per chunk.
    - encoding_name (str): The name of the encoding to use. Default is "gpt-3.5-turbo".

    Returns:
    - List[str]: A list of text chunks, each within the specified token limit.
    """
    try:
        # Initialize the encoding for the specified model
        enc = tiktoken.get_encoding(encoding_name)

        enc = tiktoken.encoding_for_model(encoding_model)

        # Encode the text into tokens
        tokens = enc.encode(text)

        # Split the tokens into chunks of max_tokens length
        chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]

        # Decode the token chunks back into text
        text_chunks = [enc.decode(chunk) for chunk in chunks]

        logger.debug(f"Splitted chunks {text_chunks}")
        return text_chunks
    except Exception as ex:
        logger.error(f"Error splitting text: {ex}", exc_info=True)


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    try:
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens
    except Exception as ex:
        logger.error(f"Error splitting text: {ex}", exc_info=True)
