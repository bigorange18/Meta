import os, torch
from pathlib import Path

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



print(increment_path("./cfg"))