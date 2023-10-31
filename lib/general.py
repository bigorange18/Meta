import os, torch
from pathlib import Path


def check_git_status(repo:str="chenorange2219/Meta", branch:str="master"):
    """
    Metaverse
    检查当前本地仓库与线上分支的提交差异数量
    """
    git_url = f"https://github.com/{repo}.git"
    msg = f", for updates see {git_url}"

    return os.system(f"git ls-remote {repo} {branch}") == 0


def get_git_hash():
    return os.popen








def increment_path(path, exist_ok=False, sep='', mkdir=False):
    path = Path(path)
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')
        for i in range(2, 999):
            cur_path = f'{path}{sep}{i}{suffix}'
            if not os.path.exists(cur_path):
                break
        path = Path(cur_path)
        if mkdir:
            path.mkdir(parents=True, exist_ok=True)
    return path

def select_device(device="", batch_size=0, newline=True):
    # f'YOLOv5 🚀 {git_describe() or file_date()}
    device = str(device).strip().lower().replace("cuda:", "").replace("none", "")
    cpu = device == "cup"
    mps = device == "mps"
    if cpu or mps:
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    elif device:
        os.environ["CUDA_VISIBLE_DEVICES"] = device
        assert torch.cuda.is_available() and torch.cuda.device_count() >= len(device.replace(",", "")), \
               f"没有gpu ' --device {device}'"
        if not cpu and not mps and torch.cuda.is_available():
            devices = device.split(',') if device else '0'  # range(torch.cuda.device_count())  # i.e. 0,1,6,7
            n = len(devices)  # device count
            if n > 1 and batch_size > 0:  # check batch_size is divisible by device_count
                assert batch_size % n == 0, f'batch-size {batch_size} not multiple of GPU count {n}'
            space = ' ' * (len(s) + 1)
            for i, d in enumerate(devices):
                p = torch.cuda.get_device_properties(i)
                s += f"{'' if i == 0 else space}CUDA:{d} ({p.name}, {p.total_memory / (1 << 20):.0f}MiB)\n"  # bytes to MB
            arg = 'cuda:0'
        elif mps and getattr(torch, 'has_mps', False) and torch.backends.mps.is_available():  # prefer MPS if available
            s += 'MPS\n'
            arg = 'mps'
        else:  # revert to CPU
            s += 'CPU\n'
            arg = 'cpu'

        if not newline:
            s = s.rstrip()
        # LOGGER.info(s)
        return torch.device(arg)

def auto_download(weight:str="yolov5s.pt", repo:str="gitbug1949", release:str="v1.1"):
    """
    1、判断权重文件是否存在
    从git中下载权重文件
    """
    if not os.path.exists(weight):
        url = f"https://github.com/{repo}/virtual/releases/tag/{release}/{weight}"
        weight_path = "./weights/" + weight
        torch.hub.download_url_to_file(url, weight )
        assert os.path.exists(weight), f"{weight} not found"



def check_suffix(weight="./weight/yolov5.pt", suffix=(".pt")):
    """
    1、判断权重文件是否以.pt结尾
    """
    if weight and suffix:
        if isinstance(suffix, str):
            suffix = list(suffix)
        weight_suffix = Path(weight).suffix.lower()
        assert weight_suffix in suffix, f"{weight} suffix must be one of {suffix}"


def check_img_size(img_size, s=32, floor=0):
    if isinstance(img_size, int):
        img_size = [img_size, img_size]
    else:
        if isinstance(img_size[0], int):
            img_size[0] = [img_size[0], img_size[0]]
        if isinstance(img_size[1], int):
            img_size[1] = [img_size[1], img_size[1]]
    return max(img_size[0][0], img_size[1][0]) >= s and max(img_size[0][1], img_size[1][1]) >= s and max

print(auto_download("yolov5s.pt"))