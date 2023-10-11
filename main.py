import os, sys
from src.Meta_Class import MetaSystem


def main():
    mateverse = MetaSystem()
    mateverse._SysCheck()
    mateverse.MetaProj()
    mateverse.MetaRun()


    pass

if __name__ == "__main__":
    main()