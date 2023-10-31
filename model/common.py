import torch
from torch.nn import nn
from lib.general import auto_download

class DetectMultiBackend(nn.Module):
    def __init__(self,weights="./weights/yolov5s.pt", device=torch.device("cpu"), dnn=False, data=None, fp16=False, fuse=True):
        super().__init__()
        w = str(weights[0] if isinstance(weights, list) else weights)
        #
        cuda = torch.cuda.is_available() and device.type != "cpu"
        # 下载权重文件，并加载
        ckpt = torch.load(auto_download(weights), map_location="cpu")
        #
        model = 1
        

        pass


    def _model_type(self,weight="path/to/model.pt"):
        """
        检测权重文件是否以.pt结尾
        """
        pass


    def forward(self, x, augment=False,  visualize=False):
        _, _, h, w = x.shape



class Ensemble(nn.ModuleList):
    def __init__(self):
        super().__init__()

    def forward(self, x, augment=False, profile=False, visualize=False):
        y = [module(x, augment, profile, visualize)[0] for module in self]
        y = torch.cat(y, 1)
        return y , None