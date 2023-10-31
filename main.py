import os, sys
from src.meta import MetaSystem


def main():
    # 需要增加log日志
    mateverse = MetaSystem()
    mateverse._SysCheck()
    mateverse.MetaProj()
    mateverse.MetaRun()


    pass

if __name__ == "__main__":
    main()