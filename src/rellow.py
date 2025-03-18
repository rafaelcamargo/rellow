import os
import re
from simple_tokenizer_v2 import SimpleTokenizerV1

# reads dataset and store it as raw_text
cwd = os.path.dirname(__file__)
file_path = os.path.join(cwd, "data", "the-verdict.txt")
with open(file_path, "r", encoding="utf-8") as f:
  raw_text = f.read()

# extracts all the words of the dataset
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s+)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# identifies every word in the dataset with an integer (token),
# appends two special tokens: endoftext and unk (unkown),
# and create a vocabulary
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab_size = len(all_tokens)
vocab = {token:integer for integer,token in enumerate(all_tokens)}

# initializes Simple Tokenizer V2
tokenizer = SimpleTokenizerV1(vocab)

# creates a sample text
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
full_text = " <|endoftext|> ".join((text1, text2))

# encodes/decodes sample text
ids = tokenizer.encode(full_text)
print(tokenizer.decode(ids))
