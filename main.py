from time import time
from TSP import *
from Draw import *

#装饰器
def runtime(f):
    def inner():
        start=time()
        f()
        end=time()
        print("程序执行时间为:%ds" %(end-start))
    return inner

#主程序
@runtime
def main():
    tsp=TSP()
    tsp.init()
    dis_list,pop_list=tsp.evolution(200)
    drawLine(dis_list)
    popDraw(pop_list,dis_list,200)
    lastDraw(pop_list[-1],dis_list[-1])
    picsTogif()
    # writeFile(dis_list,r'./data/list.ini')
    # writeFile(gen_list)#保存数据,用于复现图片


if __name__=="__main__":
    main()
