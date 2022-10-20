from random import shuffle
from random import random
from random import randint
from City import *
from Func import *
class TSP():
    '''TOUSE:  

    先执行init(filepath)函数,可以指定文件路径,默认为"data.txt"  

    之后进行迭代进化evolution()
    '''
    pop=[] #种群数组
    pop_size=-1 #种群大小
    c_rate=-1 #交叉率
    m_rate=-1 #变异率
    ga_num=-1 #最大迭代次数
    fitness=[] #适应度数组
    best_dist=-1 #记录最短距离
    best_gen=[] #记录目前最优旅行方案
    city=City() #城市类

    #初始化参数
    def __init__(self,c_rate:float=0.5,m_rate:float=0.05,pop_size:int=100):
        '''best_gen:最优的基因;flag:标志初始迭代;target_dis:目标距离
        c_rate:交叉率,默认0.5;m_rate:变异率:默认0.05  
        pop_size:种群大小,默认100;ga_num:迭代次数,默认300  
        '''
        self.fitness=[0 for i in range(self.pop_size)]
        self.c_rate=c_rate
        self.m_rate=m_rate
        self.pop_size=pop_size

    #创建种群,就是将个体添加到种群中
    #返回一个二维列表,列表的每项都是从0到city_size
    def createPop(self,size:int):
        '''size是种群pop一维的shape,返回一个种群pop'''
        pop=[]
        for i in range(size):
            gen=list(range(self.city.city_size))
            shuffle(gen)
            pop.append(gen)
        return pop

    #计算种群适应度
    def getFitness(self,pop:list):
        '''参数pop是种群,返回一个列表gf,装载整个种群的适应度'''
        gf=[]  #记录适应度
        for i in range(len(pop)):
            gen=pop[i] #取一个基因
            dis=self.city.genDistance(gen)
            dis=self.best_dist/dis #适应度用当前最优距离/该个体的距离,比值越接近1,适应度越高
            gf.append(dis)
        return gf
    
    #交叉:单点交叉
    def cross(self,parent1:list,parent2:list):#交叉p1,p2的部分基因
        '''参数p1,p2是待交叉的两个基因'''
        if random()>self.c_rate: #如果此时生成的概率大于交叉率,则不交叉
            return parent1
        index1=randint(0,self.city.city_size-1)
        index2=randint(index1,self.city.city_size-1)#[0,1,2...index1...index2...citysize-1]
        tempGene=parent2[index1:index2]#截取的基因片段,从index1到index2
        newGene=[]
        p1len=0
        for g in parent1:
            if p1len==index1:
                newGene.extend(tempGene)#插入基因片段
            if g not in tempGene:
                newGene.append(g)
            p1len+=1
        return newGene

    #反转基因,反转基因i到j之间的基因片段
    def reverse_gen(self,gen:list,i:int,j:int):
        if i>=j:    #错误顺序
            return gen
        if j>self.city.city_size-1:#过界
            return gen
        tempGene=gen[i:j]
        tempGene.reverse()
        newGene=gen[0:i]+tempGene+gen[j:self.city.city_size]
        return newGene

    #变异:反转基因变异
    def mutate(self,gen:list):
        if random()>self.m_rate:#如果大于变异率,则不变异
            return gen
        index1=randint(0,self.city.city_size-1)
        index2=randint(index1,self.city.city_size-1)#还是生成随机片段
        newGene=self.reverse_gen(gen,index1,index2)#利用翻转基因来变异
        return newGene
    ## 淘汰算法
    #选择种群,优胜劣汰法则,好的基因保留下来,差的基因进行交叉和变异
    #选出fitness的最大值和平均数,低于平均数的基因,就和最好的基因交叉,然后变异
    def selectPop(self,pop:list):
        best_f_index=self.fitness.index(max(self.fitness))#最大值的位置
        av=sum(self.fitness)/len(self.fitness)
        for i in range(self.pop_size):
            if i!=best_f_index and self.fitness[i]<av:
                pi=self.cross(pop[best_f_index],pop[i])
                pi=self.mutate(pi)
                pop[i]=pi
        return pop
    #轮盘赌:按概率选择算子
    
    def selectPop2(self,pop:list):#换选择算子
        probility=[]
        for i in range(len(self.fitness)):
            probility.append(self.fitness[i] / sum(self.fitness))
        index_list=choice(self.pop_size,probility)
        choispop=[]
        for i in index_list:
            choispop.append(pop[i])
        return choispop
        

    #主程序,迭代进化种群
    def evolution(self,ga_num:int=300):#尽量多个模块,多用参数和返回值,不要把功能都堆在一个函数中
        '''ga_num:最大迭代次数,默认为300  

           返回值是最优基因列表和最优距离列表,用来绘图
        '''
        self.ga_num=ga_num
        best_dis_list=[] #用来画折线图的y值
        best_pop_list=[] #用每代的最优基因来画路线图

        for i in range(self.ga_num):
            best_f_index=self.fitness.index(max(self.fitness))#适应度最好的
            worst_f_index=self.fitness.index(min(self.fitness))#适应度最差的
            local_best_gen=self.pop[best_f_index]#局部最优基因
            local_best_dist=self.city.genDistance(local_best_gen)#局部最短距离 

            self.best_gen=local_best_gen
            self.best_dist=self.city.genDistance(self.best_gen)

            #比较替换
            if local_best_dist<self.best_dist:#如果出现了更优化的解,则替换
                self.best_dist=local_best_dist
                self.best_gen=local_best_gen
            # else:
            #     self.pop[worst_f_index]=self.best_gen#如果没有更优解,就把当前best当成全局最优,并用最优替换最差的
            #主遗传程序,随机交叉,变异:选择种群-计算适应度-交叉-变异
            self.pop=self.selectPop(self.pop)
            self.fitness=self.getFitness(self.pop)
            for j in range(self.pop_size):
                r=randint(0,self.pop_size-1)
                if j!=r:
                    self.pop[j]=self.cross(self.pop[j],self.pop[r])#交叉第j和r个基因
                    self.pop[j]=self.mutate(self.pop[j])
            
            #每次迭代完后
            self.best_dist=self.city.genDistance(self.best_gen)#记录最短距离
            print("迭代%d次,最短距离:%s" % (i,self.best_dist))
            best_dis_list.append(self.best_dist) #添加折线图的y值
            best_pop_list.append(self.best_gen) #添加基因,用于画图

        #把用来画图的list返回
        return best_dis_list,best_pop_list

    #初始化
    def init(self,filepath:str="./data/china.txt"):
        self.city.loadCity(filepath)
        self.pop=self.createPop(self.pop_size)#创建种群
        self.fitness=self.getFitness(self.pop)#计算适应度

