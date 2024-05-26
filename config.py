import os

from dotenv import dotenv_values, load_dotenv

# Get the directory of the current file (config.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(base_dir, ".env")
# Load environment variables from the .env file
load_dotenv(env_path)

config = {
    **dotenv_values(env_path),
    **os.environ,  # override loaded values with environment variables
}

try:
    LOG_PATH = config["LOG_PATH"]
    LOG_LEVEL = config["LOG_LEVEL"]
    HOST = config["HOST"]
    GTE_LARGE_MODEL_PATH = config["GTE_LARGE_MODEL_PATH"]
    MINILM_L6V2_MODEL_PATH = config["MINILM_L6V2_MODEL_PATH"]
    PORT = int(config["PORT"])
    OPENAPI_KEY = config["OPENAPI_KEY"]
except Exception:
    raise Exception("Missing environment variables")
