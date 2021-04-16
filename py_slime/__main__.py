#!/usr/bin/python3
# encoding: utf-8
""" py_slime 's entry_points"""
import fire


def entry_point():  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.Fire()


def ipython():  # pragma: no cover
    """ 打开ipython命令 """
    from IPython import embed
    embed()


def version():
    """ 显示当前版本 """
    import py_slime
    print(py_slime.__version__)


if __name__ == '__main__':
    entry_point()
