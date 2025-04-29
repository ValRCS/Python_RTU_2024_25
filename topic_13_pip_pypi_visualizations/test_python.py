# let's see which version of python we are using
import sys # standard library, no need to install anything
print(f"Python version: {sys.version}")
# also let's see where this python is located
print(f"Python location: {sys.executable}")
# also our system path
print(f"System path: {sys.path}")
# let's see which version of pip we are using
import pip # almost standard library but comes with Python, no need to install anything
# pip is a package manager for python, it is used to install and manage packages
print(f"pip version: {pip.__version__}")
# also let's see where this pip is located
print(f"pip location: {pip.__file__}")
# we could use pip to install packages,but usually we use command line directly
