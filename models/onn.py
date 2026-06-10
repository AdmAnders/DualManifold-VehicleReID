import torch
import torch.nn as nn
import torch.nn.functional as F
from configs.config import cfg

class ONNLayer(nn.Module):
    def __init__(self, in_channels: int, out_channels: int,
                 kernel_size: int = 1, Q: int = 5,
                 padding: int = 0, groups: int = 1):
        super().__init__()
        self.Q = Q
        self.kernels = nn.ParameterList([
            nn.Parameter(torch.empty(out_channels, in_channels // groups,
                                     kernel_size, kernel_size))
            for _ in range(Q)
        ])
        self.bias = nn.Parameter(torch.zeros(out_channels))
        self.alpha = nn.Parameter(torch.ones(Q))

        for k in self.kernels:
            nn.init.xavier_uniform_(k)

    




The rest of the code will be updated after the article is published.