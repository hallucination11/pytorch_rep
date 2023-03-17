import torch
import torch.nn as nn

emb_m = torch.nn.Embedding(10, 10)
a = emb_m(torch.tensor(1))
print(a)