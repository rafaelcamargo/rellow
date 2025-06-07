import torch
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence
from constants.tokens import PAD_ID

def encode_with_specials(token_ids, vocab, add_sos_eos=False):
    if add_sos_eos:
        return [vocab['<sos>']] + [vocab[t] for t in token_ids] + [vocab['<eos>']]
    return [vocab[t] for t in token_ids]

class WordGenDataset(Dataset):
    def __init__(self, inputs, outputs, vocab, max_len=64):
        self.inputs = inputs
        self.outputs = outputs
        self.vocab = vocab
        self.max_len = max_len

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        x = encode_with_specials(self.inputs[idx], self.vocab)
        y = encode_with_specials(self.outputs[idx], self.vocab, add_sos_eos=True)
        return torch.tensor(x), torch.tensor(y)

def collate_fn(batch):
    xs, ys = zip(*batch)
    xs = pad_sequence(xs, batch_first=True, padding_value=PAD_ID)
    ys = pad_sequence(ys, batch_first=True, padding_value=PAD_ID)
    return xs, ys
