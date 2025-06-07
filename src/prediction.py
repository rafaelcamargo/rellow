import torch
import tiktoken
from constants.tokens import special_tokens
from services.model import load_model, get_device

# Initialize tokenizer
_tokenizer = tiktoken.get_encoding("cl100k_base")

def generate_word(words, model, vocab, inv_vocab, max_length=64):
    """Generate an imaginary word and its definition from three input words."""
    device = get_device()
    
    # Tokenize input words
    input_text = ",".join(words)
    input_tokens = _tokenizer.encode(input_text)
    input_tensor = torch.tensor([vocab.get(str(tok), vocab["<pad>"]) for tok in input_tokens]).unsqueeze(0).to(device)
    
    # Initialize target with SOS token
    target = torch.tensor([[vocab["<sos>"]]]).to(device)
    
    # Generate output
    with torch.no_grad():
        for _ in range(max_length):
            output = model(input_tensor, target)
            next_token = output[:, -1, :].argmax(dim=-1, keepdim=True)
            
            # Stop if we predict EOS token
            if next_token.item() == vocab["<eos>"]:
                break
                
            target = torch.cat([target, next_token], dim=1)
    
    # Convert output tokens to text
    output_tokens = target[0].cpu().numpy()
    output_text = _tokenizer.decode([int(inv_vocab[tok]) for tok in output_tokens if tok not in special_tokens.values()])
    
    return output_text

def main():
    # Load model and vocabulary
    model, vocab, inv_vocab = load_model()
    
    # Example usage
    words = ["carro", "frio", "borracha"]
    result = generate_word(words, model, vocab, inv_vocab)
    print(f"Input words: {', '.join(words)}")
    print(f"Generated: {result}")

main()
