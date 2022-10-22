class City():
    '''城市类:  
    先加载数据loadCity(fp),参数默认为"data.txt"  
    cityDistance(x,y)获取两个城市之间的距离  
    
    genDistance(gen)传入一个列表,返回总距离
    '''
    city_x=[]
    city_y=[]
    city_name=[]
    city_size=0
    filepath=""
    def __init__(self,filepath:str="./data/china.txt"):
        self.loadCity(filepath)

    #加载数据
    def loadCity(self,filepath:str):
        '''filepath:文件路径'''
        file=open(filepath).readlines()
        arr=[file[i].strip('\n').split('\t') for i in range(len(file))]#split去除中间的,strip去前后的
        for i in arr:
            self.city_name.append(i[0])
            self.city_x.append(eval(i[1]))
            self.city_y.append(eval(i[2]))
        self.city_size=len(arr)

    #计算两个城市之间的距离,这里用欧式距离,即两个点之间的直线距离
    def cityDistance(self,c1:int,c2:int):
        '''c1,c2是城市列表的序号,返回两个城市间的距离'''
        d=((self.city_x[c1]-self.city_x[c2])**2+(self.city_y[c1]-self.city_y[c2])**2)**0.5
        return d
        
    #计算一个基因的总距离,即基因中的线路表示的距离
    def genDistance(self,gen:list):
        '''gen是pop的一个基因,返回值为这个基因表示的路径长度'''
        distance=0.0
        for i in range(-1,self.city_size-1):#用-1到len-1刚好是所有的距离
            i1,i2=gen[i],gen[i+1]
            distance+=self.cityDistance(i1,i2)
        return distance

