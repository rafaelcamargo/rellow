import tiktoken
from constants.tokens import special_tokens

# Private tokenizer instance (internal use only)
_tokenizer = tiktoken.get_encoding("cl100k_base")

def tokenize_dataset(data):
    """Tokenize keys and values using the internal tokenizer."""
    inputs = []
    outputs = []
    for key, value in data.items():
        inp_tokens = _tokenizer.encode(key)
        out_tokens = _tokenizer.encode(value)
        inputs.append(inp_tokens)
        outputs.append(out_tokens)
    return inputs, outputs

def build_vocab(inputs, outputs):
    """Build vocabulary mapping from token IDs and add special tokens."""
    offset = len(special_tokens)
    all_ids = set(tok for seq in inputs + outputs for tok in seq)
    vocab = {tok: i + offset for i, tok in enumerate(sorted(all_ids))}
    vocab.update({k: v for k, v in special_tokens.items()})
    inv_vocab = {v: k for k, v in vocab.items()}
    return vocab, inv_vocab
