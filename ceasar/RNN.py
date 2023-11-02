import torch.nn
from ceasar.ceasar_algorithms import dict_char

class RNN(torch.nn.Module):
    def __init__(self):
        super(RNN, self).__init__()
        self.embed = torch.nn.Embedding(len(dict_char), len(dict_char))
        self.rnn = torch.nn.RNN(len(dict_char), 256, batch_first=True)
        self.linear = torch.nn.Linear(256, len(dict_char))

    def forward(self, sentences, state=None):
        embed = self.embed(sentences)
        o, a = self.rnn(embed)
        out = self.linear(o)
        return out