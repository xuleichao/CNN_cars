'''

by xlc time:2018-05-10 11:01:55
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
import tensorflow as tf
from PIL import Image
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img = Image.open('123.png')
