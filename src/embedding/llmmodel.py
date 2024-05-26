from sentence_transformers import SentenceTransformer

from config import GTE_LARGE_MODEL_PATH, MINILM_L6V2_MODEL_PATH

gte_model = SentenceTransformer(GTE_LARGE_MODEL_PATH, device=None)
mini_l6_model = SentenceTransformer(MINILM_L6V2_MODEL_PATH, device=None)
