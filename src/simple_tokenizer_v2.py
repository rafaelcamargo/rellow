import re

class SimpleTokenizerV1:
  def __init__(self, vocab):
    self.str_to_int = vocab            #1
    self.int_to_str = {i:s for s,i in vocab.items()}        #2

  def encode(self, text):         #3
    preprocessed = re.split(r'([,.?_!"()\']|--|\s+)', text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]

    preprocessed = [item if item in self.str_to_int
                    else "<|unk|>" for item in preprocessed]

    ids = [self.str_to_int[s] for s in preprocessed]
    return ids

  def decode(self, ids):         #4
    text = " ".join([self.int_to_str[i] for i in ids]) 
    text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)      #5
    return text
