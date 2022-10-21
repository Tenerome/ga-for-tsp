from TSP import *
from Draw import *

#分析pop_size和收敛dist的关系
#固定其他参数,ga_num=500
#求不同种群大小下的收敛距离,每个求5次,取平均值画图
def analysisPop():
    pop=[n for n in range(60,120,10)]#20~110
    constringency=[]
    for i in pop:
        tsp=TSP(pop_size=i)
        tsp.init()
        temp=[]
        for j in range(5):
            dis=tsp.evolution(500)[0][-1]#最后一次的最短距离
            temp.append(dis)
        constringency.append(sum(temp)/len(temp))#五次求平均值
    #用种群大小和平均收敛距离画图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(pop,constringency,color='blue')
    plt.axis("auto")
    plt.xlabel("种群大小",color='green')
    plt.ylabel("平均收敛距离",color='green')
    plt.title("种群大小和收敛距离关系图",color="red")
    plt.show()

#确定pop_size=90
# 分析Crate和收敛dist的关系
def analysisCrate():
    # crate=[n/10 for n in range(3,10,1)]  #0.3-0.9
    crate=[n/100 for n in range(55,66,1)] #得到最佳交叉率:0.62
    csgc=[]
    for i in crate:
        tsp=TSP(c_rate=i,pop_size=90)
        tsp.init()
        temp=[]
        for j in range(5):
            dis=tsp.evolution(500)[0][-1]
            temp.append(dis)
        csgc.append(sum(temp)/len(temp))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(crate,csgc,color='blue')
    plt.xlabel("交叉率",color='green')
    plt.ylabel("平均收敛距离",color='green')
    plt.title("交叉率和收敛距离关系图",color="red")
    plt.show()

#pop_size=90,同时c_rate=0.62的条件下,找最佳的变异率
#分析M_rate和收敛距离的关系
def analysisMrate():
    # mrate=[n/100 for n in range(1,10,1)]  #0.01-0.09
    mrate=[n/1000 for n in range(56,65,1)]#得到最佳变异率:0.063
    csgc=[]
    for i in mrate:
        tsp=TSP(c_rate=0.62,m_rate=i,pop_size=90)
        tsp.init()
        temp=[]
        for j in range(5):
            dis=tsp.evolution(500)[0][-1]
            temp.append(dis)
        csgc.append(sum(temp)/len(temp))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(mrate,csgc,color='blue')
    plt.xlabel("交叉率",color='green')
    plt.ylabel("平均收敛距离",color='green')
    plt.title("交叉率和收敛距离关系图",color="red")
    plt.show()

if __name__=="__main__":
    # analysisPop()
    # analysisCrate()
    analysisMrate()

    # tsp=TSP(0.62,0.063,90)