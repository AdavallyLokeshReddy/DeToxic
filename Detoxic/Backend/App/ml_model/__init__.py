# ml_model package
from functools import lru_cache
from .predictor import ModelWrapper

@lru_cache()
def get_model():
    """Return a cached ModelWrapper instance."""
    return ModelWrapper()
