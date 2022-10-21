from matplotlib import pyplot as plt
from copy import deepcopy
from City import *

def dataTransform(gen:list):
    '''转换数据函数'''
    city=City()
    x=[];y=[];t=[]
    for i in gen:
        x.append(city.city_x[i])
        y.append(city.city_y[i])
        t.append(city.city_name[i])
    return x,y,t

def genDraw(gen:list):
    '''根据一个基因画路线图'''
    x,y,t=dataTransform(gen)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(20,10),dpi=65)
    plt.axis("off")
    #画点
    plt.plot(x,y,'bo',markersize=4)
    #标记
    for i in range(len(x)):
        plt.text(x[i],y[i],t[i],fontsize=15)
    #画线
    x=deepcopy(x);y=deepcopy(y)
    x.append(x[0])
    y.append(y[0])
    plt.plot(x,y,color='r',linewidth=1)
    return plt

def popDraw(best_pop_list:list,best_dis_list:list,picnum:int):
    '''根据种群画图  \n
        参数picnum是绘制gif所用的图片数量\n
        picnum必须不大于迭代次数
    '''
    #加个判断
    if picnum>len(best_dis_list):
        print("Error:picnum必须不大于迭代次数ga_num")
    else:
        for i in range(picnum):
            plt=genDraw(best_pop_list[i])
            plt.title("最短距离:{}".format(best_dis_list[i]),fontsize=30,color='pink')
            plt.savefig('./pics/%d.png' %((i+1)))
            plt.close() #要关闭,不然会占内存 

def lastDraw(last_gen:list,last_dis:float):
    '''保存最后的结果图片:收敛距离'''
    plt=genDraw(last_gen)
    plt.title("收敛距离:{}".format(last_dis),fontsize=30,color='pink')
    plt.savefig('./pics/last.jpg')
    plt.close()

def drawLine(best_dis_list:list):
    '''画折线图,参数list是y值'''
    y=best_dis_list
    x=[i+1 for i in range(len(y))]
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x,y)
    plt.ylabel('最短距离')
    plt.xlabel('迭代次数')
    plt.savefig("./pics/Line.jpg")
    plt.close()
