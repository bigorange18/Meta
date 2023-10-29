import os, sys
import torch
from pathlib import Path
from lib.general import increment_path, select_device

FILE = Path(__file__).resolve()         # 转为绝对路径
ROOT = FILE.parents[0]                  # 找到路径
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))          # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

def detect(
        source = "0",
        savefile = ROOT / "runs/detect",
        name = "exp",
        device=''

):
    '''
    1、判断输入的是视频还是开启摄像头
    '''
    source = str(source)
    # 摄像头
    is_cam = source.isnumeric() or source.endswith(".stream")
    # 传入视频是以screen开头
    is_video = source.lower().startswith("screen")
    # 创建新的文件夹保存输出结果
    save_file = increment_path(Path(save_file) / name, exist_ok=False)

    #gpu
    # device = torch.device("device:0")
    device = select_device(device)

    # 从摄像头参数中获取
    img_size = (640, 640)

    if is_cam:
        view_img = 1





print(ROOT)