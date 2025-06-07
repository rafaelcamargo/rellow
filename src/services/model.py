import os
import json
import torch
from pathlib import Path
from services.transformer import TinyTransformer

# Internal constants for file paths
_MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
_VOCAB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
_MODEL_PATH = os.path.join(_MODEL_DIR, "rellow.pt")
_VOCAB_PATH = os.path.join(_VOCAB_DIR, "vocab.json")

# Internal device selection
_DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

def save_model(model, vocab):
    """
    Save the model state and vocabulary to disk.
    
    Args:
        model: The trained transformer model
        vocab: The vocabulary dictionary
    """
    # Create necessary directories
    os.makedirs(_MODEL_DIR, exist_ok=True)
    os.makedirs(_VOCAB_DIR, exist_ok=True)
    
    # Save model state
    torch.save(model.state_dict(), _MODEL_PATH)
    
    # Save vocabulary
    with open(_VOCAB_PATH, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)
    
    print(f"Model saved to {_MODEL_PATH}")
    print(f"Vocabulary saved to {_VOCAB_PATH}")

def load_model():
    """
    Load the model and its vocabulary from disk.
    
    Returns:
        tuple: (model, vocab, inv_vocab)
    """
    # Load vocabulary
    with open(_VOCAB_PATH, "r", encoding="utf-8") as f:
        vocab = json.load(f)
    inv_vocab = {int(v): k for k, v in vocab.items()}
    
    # Initialize and load model
    model = TinyTransformer(vocab_size=len(vocab)).to(_DEVICE)
    model.load_state_dict(torch.load(_MODEL_PATH, map_location=_DEVICE))
    model.eval()
    
    return model, vocab, inv_vocab

def get_device():
    """
    Get the device being used for model operations.
    
    Returns:
        torch.device: The device being used
    """
    return _DEVICE 
