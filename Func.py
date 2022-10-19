from copy import deepcopy
from os import system

def median(fitness:list):
    '''求中位数'''
    lf=deepcopy(fitness)
    lf.sort()
    half=len(lf)//2
    mid=(lf[half]+lf[-half-1])/2
    return mid  

def picsTogif():
    '''将保存的图片转成视频'''
    system('cd ./pics/ && ffmpeg -r 5 -i %d.png -vf palettegen palette.png && ffmpeg -y -r 5 -i %d.png -i palette.png -lavfi paletteuse output.gif')
    system('cd ./pics/ && del *.png palette.png')

def writeFile(context:list,filepath:str='./data/gen.ini'):
    '''写文件:保存数据'''
    with open(filepath,'w') as f:
        f.write(str(context))