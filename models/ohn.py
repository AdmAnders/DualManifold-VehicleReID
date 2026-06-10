import torch
import torch.nn as nn
import timm
from models.onn import ONNLayer
from models.attention import ASONN, GCAM, OBAM
from configs.config import cfg

class GeMPooling(nn.Module):
    def __init__(self, p: float = 3.0, eps: float = 1e-6):
        super().__init__()
        self.p = nn.Parameter(torch.tensor(p))
        self.eps = eps

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        p = self.p.clamp(min=1.0)
        x_c = x.clamp(min=self.eps)
        return x_c.pow(p).mean(dim=[2, 3]).pow(1.0 / p)

class OperationalHybridNetwork(nn.Module):
    def __init__(self, num_classes: int, Q: int = cfg.TAYLOR_Q, embed_dim: int = cfg.EMBED_DIM):
        super().__init__()
        self.Q = Q
        self.backbone = timm.create_model(
            "efficientnet_b4", pretrained=True,
            features_only=False, num_classes=0, global_pool="")
        





The rest of the code will be updated after the article is published.