import re
import os, torch
import cv2
import platform
import time
from pathlib import Path
from subprocess import check_output
from lib.classes import Camera

def check_git_status(repo:str="bigorange18/Meta", branch:str="dev"):
    """
    Meta
    检查当前本地仓库与线上分支的提交差异数量
    """
    git_url = f"https://github.com/{repo}.git"
    msg = f", for updates see {git_url}"
    assert Path(".git").exists(), "This is not a git repository. You should clone it with --recursive option" + msg
    splits = re.split(pattern=r'\s', string=check_output("git remote -v", shell=True).decode())
    remote = splits[0]
    check_output(f"git fetch {remote}", shell=True, timeout=3)
    local_branch = check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode().strip()
    # remote_branch = check_output(f"git rev-parse --abbrev-ref {remote}/{branch}", shell=True).decode().strip()
    diff_count = check_output(f"git rev-list {local_branch}..{remote}/{branch} --count", shell=True).decode().strip()   
    if diff_count != "0":
        print(f"{repo} is {diff_count} commit(s) behind {remote}/{branch}")
    else:
        print(f"{repo} is up-to-date with {remote}/{branch}")

def get_camera_status(camera="0"):
    """
    获取相机参数
    """
    cap = cv2.VideoCapture(camera)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    cam = Camera()
    cam.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cam.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cam.fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return cam







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
    info = f"Python-{platform.python_version()} torch-{torch.__version__} " 
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
            space = ' ' * (len(info) + 1)
            for i, d in enumerate(devices):
                p = torch.cuda.get_device_properties(i)
                info += f"{'' if i == 0 else space}CUDA:{d} ({p.name}, {p.total_memory / (1 << 20):.0f}MiB)\n"  # bytes to MB
            arg = 'cuda:0'
        elif mps and getattr(torch, 'has_mps', False) and torch.backends.mps.is_available():  # prefer MPS if available
            info += 'MPS\n'
            arg = 'mps'
        else:  # revert to CPU
            info += 'CPU\n'
            arg = 'cpu'

        if not newline:
            info = info.rstrip()
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

def check_file(file, suffix=''):
    # Search/download file (if necessary) and return path
    check_suffix(file, suffix)  # optional
    file = str(file)  # convert to str()
    if os.path.isfile(file) or not file:  # exists
        return file
    elif file.startswith(('http:/', 'https:/')):  # download
        url = file  # warning: Pathlib turns :// -> :/
        file = Path(urllib.parse.unquote(file).split('?')[0]).name  # '%2F' to '/', split https://url.com/file.txt?auth
        if os.path.isfile(file):
            LOGGER.info(f'Found {url} locally at {file}')  # file already exists
        else:
            LOGGER.info(f'Downloading {url} to {file}...')
            torch.hub.download_url_to_file(url, file)
            assert Path(file).exists() and Path(file).stat().st_size > 0, f'File download failed: {url}'  # check
        return file
    elif file.startswith('clearml://'):  # ClearML Dataset ID
        assert 'clearml' in sys.modules, "ClearML is not installed, so cannot use ClearML dataset. Try running 'pip install clearml'."
        return file
    else:  # search
        files = []
        for d in 'data', 'models', 'utils':  # search directories
            files.extend(glob.glob(str(ROOT / d / '**' / file), recursive=True))  # find file
        assert len(files), f'File not found: {file}'  # assert file was found
        assert len(files) == 1, f"Multiple files match '{file}', specify exact path: {files}"  # assert unique
        return files[0]  # return file


def download(url, dir='.', unzip=True, delete=True, curl=False, threads=1, retry=3):
    # Multithreaded file download and unzip function, used in data.yaml for autodownload
    def download_one(url, dir):
        # Download 1 file
        success = True
        if os.path.isfile(url):
            f = Path(url)  # filename
        else:  # does not exist
            f = dir / Path(url).name
            LOGGER.info(f'Downloading {url} to {f}...')
            for i in range(retry + 1):
                if curl:
                    success = curl_download(url, f, silent=(threads > 1))
                else:
                    torch.hub.download_url_to_file(url, f, progress=threads == 1)  # torch download
                    success = f.is_file()
                if success:
                    break
                elif i < retry:
                    LOGGER.warning(f'⚠️ Download failure, retrying {i + 1}/{retry} {url}...')
                else:
                    LOGGER.warning(f'❌ Failed to download {url}...')

        if unzip and success and (f.suffix == '.gz' or is_zipfile(f) or is_tarfile(f)):
            LOGGER.info(f'Unzipping {f}...')
            if is_zipfile(f):
                unzip_file(f, dir)  # unzip
            elif is_tarfile(f):
                subprocess.run(['tar', 'xf', f, '--directory', f.parent], check=True)  # unzip
            elif f.suffix == '.gz':
                subprocess.run(['tar', 'xfz', f, '--directory', f.parent], check=True)  # unzip
            if delete:
                f.unlink()  # remove zip

    dir = Path(dir)
    dir.mkdir(parents=True, exist_ok=True)  # make directory
    if threads > 1:
        pool = ThreadPool(threads)
        pool.imap(lambda x: download_one(*x), zip(url, repeat(dir)))  # multithreaded
        pool.close()
        pool.join()
    else:
        for u in [url] if isinstance(url, (str, Path)) else url:
            download_one(u, dir)


def check_dataset(data, autodownload=True):
    # Download, check and/or unzip dataset if not found locally

    # Download (optional)
    extract_dir = ''
    if isinstance(data, (str, Path)) and (is_zipfile(data) or is_tarfile(data)):
        download(data, dir=f'{DATASETS_DIR}/{Path(data).stem}', unzip=True, delete=False, curl=False, threads=1)
        data = next((DATASETS_DIR / Path(data).stem).rglob('*.yaml'))
        extract_dir, autodownload = data.parent, False

    # Read yaml (optional)
    if isinstance(data, (str, Path)):
        data = yaml_load(data)  # dictionary

    # Checks
    for k in 'train', 'val', 'names':
        assert k in data, emojis(f"data.yaml '{k}:' field missing ❌")
    if isinstance(data['names'], (list, tuple)):  # old array format
        data['names'] = dict(enumerate(data['names']))  # convert to dict
    assert all(isinstance(k, int) for k in data['names'].keys()), 'data.yaml names keys must be integers, i.e. 2: car'
    data['nc'] = len(data['names'])

    # Resolve paths
    path = Path(extract_dir or data.get('path') or '')  # optional 'path' default to '.'
    if not path.is_absolute():
        path = (ROOT / path).resolve()
        data['path'] = path  # download scripts
    for k in 'train', 'val', 'test':
        if data.get(k):  # prepend path
            if isinstance(data[k], str):
                x = (path / data[k]).resolve()
                if not x.exists() and data[k].startswith('../'):
                    x = (path / data[k][3:]).resolve()
                data[k] = str(x)
            else:
                data[k] = [str((path / x).resolve()) for x in data[k]]

    # Parse yaml
    train, val, test, s = (data.get(x) for x in ('train', 'val', 'test', 'download'))
    if val:
        val = [Path(x).resolve() for x in (val if isinstance(val, list) else [val])]  # val path
        if not all(x.exists() for x in val):
            LOGGER.info('\nDataset not found ⚠️, missing paths %s' % [str(x) for x in val if not x.exists()])
            if not s or not autodownload:
                raise Exception('Dataset not found ❌')
            t = time.time()
            if s.startswith('http') and s.endswith('.zip'):  # URL
                f = Path(s).name  # filename
                LOGGER.info(f'Downloading {s} to {f}...')
                torch.hub.download_url_to_file(s, f)
                Path(DATASETS_DIR).mkdir(parents=True, exist_ok=True)  # create root
                unzip_file(f, path=DATASETS_DIR)  # unzip
                Path(f).unlink()  # remove zip
                r = None  # success
            elif s.startswith('bash '):  # bash script
                LOGGER.info(f'Running {s} ...')
                r = subprocess.run(s, shell=True)
            else:  # python script
                r = exec(s, {'yaml': data})  # return None
            dt = f'({round(time.time() - t, 1)}s)'
            s = f"success ✅ {dt}, saved to {colorstr('bold', DATASETS_DIR)}" if r in (0, None) else f'failure {dt} ❌'
            LOGGER.info(f'Dataset download {s}')
    check_font('Arial.ttf' if is_ascii(data['names']) else 'Arial.Unicode.ttf', progress=True)  # download fonts
    return data  # dictionary



def safe_download(file, url, url2=None, min_bytes=1E0, error_msg=''):
    # Attempts to download file from url or url2, checks and removes incomplete downloads < min_bytes
    from utils.general import LOGGER

    file = Path(file)
    assert_msg = f"Downloaded file '{file}' does not exist or size is < min_bytes={min_bytes}"
    try:  # url1
        LOGGER.info(f'Downloading {url} to {file}...')
        torch.hub.download_url_to_file(url, str(file), progress=LOGGER.level <= logging.INFO)
        assert file.exists() and file.stat().st_size > min_bytes, assert_msg  # check
    except Exception as e:  # url2
        if file.exists():
            file.unlink()  # remove partial downloads
        LOGGER.info(f'ERROR: {e}\nRe-attempting {url2 or url} to {file}...')
        # curl download, retry and resume on fail
        curl_download(url2 or url, file)
    finally:
        if not file.exists() or file.stat().st_size < min_bytes:  # check
            if file.exists():
                file.unlink()  # remove partial downloads
            LOGGER.info(f'ERROR: {assert_msg}\n{error_msg}')
        LOGGER.info('')



def attempt_download(file, repo='ultralytics/yolov5', release='v7.0'):
    # Attempt file download from GitHub release assets if not found locally. release = 'latest', 'v7.0', etc.
    from utils.general import LOGGER

    def github_assets(repository, version='latest'):
        # Return GitHub repo tag (i.e. 'v7.0') and assets (i.e. ['yolov5s.pt', 'yolov5m.pt', ...])
        if version != 'latest':
            version = f'tags/{version}'  # i.e. tags/v7.0
        response = requests.get(f'https://api.github.com/repos/{repository}/releases/{version}').json()  # github api
        return response['tag_name'], [x['name'] for x in response['assets']]  # tag, assets

    file = Path(str(file).strip().replace("'", ''))
    if not file.exists():
        # URL specified
        name = Path(urllib.parse.unquote(str(file))).name  # decode '%2F' to '/' etc.
        if str(file).startswith(('http:/', 'https:/')):  # download
            url = str(file).replace(':/', '://')  # Pathlib turns :// -> :/
            file = name.split('?')[0]  # parse authentication https://url.com/file.txt?auth...
            if Path(file).is_file():
                LOGGER.info(f'Found {url} locally at {file}')  # file already exists
            else:
                safe_download(file=file, url=url, min_bytes=1E5)
            return file

        # GitHub assets
        assets = [f'yolov5{size}{suffix}.pt' for size in 'nsmlx' for suffix in ('', '6', '-cls', '-seg')]  # default
        try:
            tag, assets = github_assets(repo, release)
        except Exception:
            try:
                tag, assets = github_assets(repo)  # latest release
            except Exception:
                try:
                    tag = subprocess.check_output('git tag', shell=True, stderr=subprocess.STDOUT).decode().split()[-1]
                except Exception:
                    tag = release

        if name in assets:
            file.parent.mkdir(parents=True, exist_ok=True)  # make parent dir (if required)
            safe_download(file,
                          url=f'https://github.com/{repo}/releases/download/{tag}/{name}',
                          min_bytes=1E5,
                          error_msg=f'{file} missing, try downloading from https://github.com/{repo}/releases/{tag}')

    return str(file)
