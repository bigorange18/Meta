import torch
from torch.nn import nn

class DetectMulti(nn.Module):
    def __init__(self,weights="./weights/yolov5s.pt", device=torch.device("cup"), dnn=False, data=None, fp16=False, fuse=True):
        super().__init__()
        w = str(weights[0] if isinstance(weights, list) else weights)
        
        pass


    def _model_type(self,weight="path/to/model.pt"):


