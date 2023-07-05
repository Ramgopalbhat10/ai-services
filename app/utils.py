from sentence_transformers import SentenceTransformer


def load_embedding_model():
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
    return model