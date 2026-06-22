from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

MODEL_NAME = "distilbert-base-uncased"

class ModelWrapper:
    def __init__(self, model_name=MODEL_NAME):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=6)

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        probs = torch.sigmoid(outputs.logits).detach().numpy()[0]
        return {
            "toxic": float(probs[0]),
            "severe_toxic": float(probs[1]),
            "obscene": float(probs[2]),
            "threat": float(probs[3]),
            "insult": float(probs[4]),
            "identity_hate": float(probs[5]),
        }
