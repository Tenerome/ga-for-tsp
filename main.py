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
    print("正在处理图片...")
    drawLine(dis_list)
    popDraw(pop_list,dis_list,200)
    lastDraw(pop_list[-1],dis_list[-1])
    picsTogif()
    print("正在保存数据...")
    writeFile(dis_list,r'./data/list.ini')
    writeFile(pop_list,r'./data/pop.ini')
    print("执行完毕")


if __name__=="__main__":
    main()
