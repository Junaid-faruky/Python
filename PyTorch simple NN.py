# 17. PyTorch simple NN
import torch, torch.nn as nn
model = nn.Sequential(nn.Linear(2,4), nn.ReLU(), nn.Linear(4,1))
x = torch.tensor([[1.0,2.0]])
print(model(x))
