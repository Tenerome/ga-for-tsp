from copy import deepcopy
from os import system
from random import random

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

def writeFile(context:list,filepath:str='./data/gen.ini',mode:str='w'):
    '''写文件:保存数据'''
    with open(filepath,mode) as f:
        f.write(str(context))
        f.write('\n')
#TODO choice()
def choice(pop_size:int,probility:list):
    '''实现np.random.choice()  
    pop_size:种群大小,也是目标size
    probility:概率列表
    '''
    chospop=[]
    for i in range(pop_size):
        if random()<=probility[i]:
            chospop.append(i)
    return chospop