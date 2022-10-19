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
    system('cd ./pics/ && ffmpeg -r 5 -i %d.png -vf palettegen palette.png && ffmpeg -r 5 -i %d.png -i palette.png -lavfi paletteuse output.gif')
    system('cd ./pics/ && del *.png palette.png')
    print("转换完成")

def readFile(filepath:str='./data/gen.ini'):
    '''读文件'''
    with open(filepath,'r') as f:
        con=f.read().rsplit(',')
        gen=[]
        for i in con:
            gen.append(int(i))
        return gen

def writeFile(context:list,filepath:str='./data/gen.ini'):
    '''写文件'''
    context=str(context).strip('[').strip(']')
    with open(filepath,'w') as f:
        f.write(context)