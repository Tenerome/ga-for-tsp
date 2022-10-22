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
    print("程序开始,迭代进化..")
    tsp=TSP(0.62,0.063,90)#最三个最佳的参数
    tsp.init()
    dis_list,pop_list=tsp.evolution()
    print("迭代完毕,正在处理图片..")
    drawLine(dis_list)
    lastDraw(pop_list[-1],dis_list[-1])
    popDraw(pop_list,dis_list,300)
    picsTogif()
    print("图片处理完毕")
    writeFile(dis_list,r'./data/list.ini')
    writeFile(pop_list,r'./data/pop.ini')
    print("保存数据完毕")

if __name__=="__main__":
    main()
