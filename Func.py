from os import system
from random import random

def picsTogif():
    '''将保存的图片转成视频'''
    system('cd ./pics/ && ffmpeg -r 5 -i %d.png -vf palettegen palette.png && ffmpeg -y -r 5 -i %d.png -i palette.png -lavfi paletteuse output.gif')
    system('cd ./pics/ && del *.png palette.png')

def writeFile(context:list,filepath:str='./data/gen.ini',mode:str='w'):
    '''写文件:保存数据'''
    with open(filepath,mode) as f:
        f.write(str(context))
        f.write('\n')