import os
import tiktoken

# reads dataset and store it as raw_text
cwd = os.path.dirname(__file__)
file_path = os.path.join(cwd, "data", "the-verdict.txt")
with open(file_path, "r", encoding="utf-8") as f:
  raw_text = f.read()

#initiliazes tiktoken
tokenizer = tiktoken.get_encoding("gpt2")

# encodes/decodes sample text
encoded = tokenizer.encode(raw_text, allowed_special={"<|endoftext|>"})
print(encoded[:50])

decoded = tokenizer.decode(encoded[:50])
print(decoded)

