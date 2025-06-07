import os
import json
import torch
from torch import nn, optim
from pathlib import Path
from torch.utils.data import DataLoader
from services.word_generation_dataset import WordGenDataset, collate_fn
from services.tokenizer import tokenize_dataset, build_vocab
from services.transformer import TinyTransformer
from services.model import save_model

# 1. Preprocessing
print("Preprocessing...")

# 1.1 Read dataset and store it as json
cwd = os.path.dirname(__file__)
file_path = os.path.join(cwd, "data", "definitions.json")
with open(file_path, "r", encoding="utf-8") as f:
  data = json.load(f)
print("Data loaded!")

# 1.2 Tokenize using internal tokenizer logic
inputs, outputs = tokenize_dataset(data)
print("Data Tokenized!")

# 1.3 Build vocabulary
vocab, inv_vocab = build_vocab(inputs, outputs)
print("Vocabulary built!")

# 1.4 Create dataset and dataloader
dataset = WordGenDataset(inputs, outputs, vocab)
print("Dataset built!")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
print("Dataloader built!")

# 2. Training
print("Training...")

# 2.1 Initialize model
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
vocab_size = len(vocab)
model = TinyTransformer(vocab_size=vocab_size).to(device)

# 2.2 Loss and Optimizer
criterion = nn.CrossEntropyLoss(ignore_index=vocab["<pad>"])
optimizer = optim.Adam(model.parameters(), lr=1e-4)

# 2.3 Training Loop
num_epochs = 10

for epoch in range(num_epochs):
    model.train()
    total_loss = 0

    for batch in dataloader:
        src, tgt = batch
        src, tgt = src.to(device), tgt.to(device)

        # Shift target to create input/target pairs
        tgt_input = tgt[:, :-1]
        tgt_expected = tgt[:, 1:]

        # Forward pass
        logits = model(src, tgt_input)

        # Reshape for loss: (batch*seq_len, vocab_size)
        loss = criterion(logits.reshape(-1, vocab_size), tgt_expected.reshape(-1))

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch+1}/{num_epochs} - Loss: {avg_loss:.4f}")

# 2.4 Save model
print("Saving...")
save_model(model, vocab)
print("Finished!")
