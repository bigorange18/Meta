import parser
import argparse
import sys
import os
import yaml
from pathlib import Path
from lib.general import check_git_status
from lib.general import select_device
from lib.general import increment_path
from ultralytics.utils.checks import check_requirements

FILE = Path(__file__).resolve()     # 返回路径当前工作目录路径  .absolute()绝对
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))



def train(hyp, opt, device):
    save_path = str(ROOT / 'runs/train')
    save_weight = save_path / 'weights'
    save_weight.mkdir(parents=True, exist_ok=True) # make dir
    last, best = save_weight / 'last.pt', save_weight / 'best.pt'

    epochs = opt.epochs
    batch_size = opt.batch_size
    weights = opt.weights
        # Hyperparameters
    if isinstance(hyp, str):
        with open(hyp, errors='ignore') as f:
            hyp = yaml.safe_load(f)  # load hyps dict
    opt.hyp = hyp.copy()  # for saving hyps to checkpoints

    # Save run settings






def parse_opt(known=False):
    par = argparse.ArgumentParser()
    par.add_argument('--weights', type=str, default=ROOT / 'weights/yolov5.pt', help='model.pt path')
    par.add_argument('--device', type=str, default='cuda:0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    par.add_argument('--cfg', type=str, default=ROOT / 'models/model_chv.yaml', help='model.yaml path')
    par.add_argument('--data', type=str, default=ROOT / 'data/data_chv.yaml', help='dataset.yaml path')
    par.add_argument('--batch_size', type=int, default=2, help='batch size')
    par.add_argument('--epochs', type=int, default=100, help='number of epochs')
    par.add_argument('--img_size', '--img', '--img-size', nargs='+', type=int, default=640, help='inference size ( height, width)')
    par.add_argument('--workers', type=int, default=4, help='maximum number of dataloader workers')
    par.add_argument('--hyp', type=str, default=ROOT / 'data/hyp.scratch-low.yaml', help='hyperparameters path')

    par.add_argument('--project', type=str, default='improve', help='save to project/name')
    par.add_argument('--name', type=str, default='exp', help='save to project/name')
    par.add_argument('--save_dir')
    return par.parse_args()



def main(opt ):
    # check
    check_git_status()
    check_requirements(ROOT / 'requirements.txt')
    opt.save_dir = str(increment_path(Path(opt.project) / opt.name, exist_ok=False))

    #
    device = select_device(opt.device, opt.batch_size)

    pass

if __name__ == '__main__':
    main(parse_opt())