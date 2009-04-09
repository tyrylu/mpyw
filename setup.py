# -- coding: UTF-8 --
from distutils.core import setup
import py2exe
setup(name="mpyw", version="1.0 alpha", windows =["mpyw.pyw", "eventhandlers.py", "window.py", "window.xrc"], data_files = [""])
