import pandas as pd
from dijkstar import Graph, find_path
import copy
def node_pos(pos):
    citi=get_cities()
    citi2=get_cities_2()

    pl_po={
        'Hinthada':[95.210,17.56],'Pathein':[94.573,17.14],'Labutta':[94.884,15.87],'Pyapon':[95.621,15.942],'Mawlamyine':[97.47,15.821],
        'Hpa-an':[97.75,17.42],'Kawkareik':[98.735,16.469],'Myawaddy':[99.648,16.717],'Kyaukyu': [93.521,19],'Magway' :[95.032,20.43],
        'Minbu': [94.639,19.95],'Bawlakhe':[97.663,18.94],'Loikaw':[97.614,19.61],'Meiktila':[96.051,21.026],'Sagaing':[95.620,21.84],
        'Pyinoolwin':[96.626,22.22],'Yinmarbin':[94.933,21.87],'Kyaukse':[96.193,21.32],'Nyaung-U':[95.244,20.923],'Falam':[93.609,23.23],
        'Hopang':[99.024,23.575],'Laukkaing':[99.001,24.091],'Tachileik':[99.821,20.06]
    }
    for k,v in pl_po.items():
        citi2[k]=v
    #print(citi2)
    return citi2
def label_pos(pos):
    pos2=copy.deepcopy(pos)
    print('BEFORE',pos)
    for k,v in pos2.items():
        print(k,cal_len(k))
        pos2[k]=[v[0]+cal_len(k),v[1]+0.07]
    #print(citi2)
    print('AFTER',pos2)
    return pos2
def cal_len(cit):
    cit_len=((len(cit)/1.9)-1)*0.07
    return cit_len

def get_cities_2():
    citi=get_cities()
    df = pd.read_excel('data/node_dataset_3.xlsx')
    citi2={}
    #print('NODE',get_LL(df[ (df['Node 1'] == 'Yangon') | (df['Node 2'] == 'Minbu')],'Minbu'))
    for x in citi:
        #print(x,)
        #print(x,get_LL(df[ (df['Node 1'] == x) | (df['Node 2'] == x)],x))
        citi2[x]=get_LL(df[ (df['Node 1'] == x) | (df['Node 2'] == x)],x)
        #citi2[x]=
    return citi2
def get_LL(df,city):
    df=df.to_numpy()
    for x in df:
        #print(x,city)
        if x[1]==city:  return [x[3],x[4]]
        if x[2]==city:  return [x[5],x[6]]
def get_cities():
    df = pd.read_excel('data/node_dataset_3.xlsx')

    citi= list(df['Node 1'])+list(df['Node 2'])
    citi=list(set(citi))
    citi.sort()
    print('CITY Total',len(citi))
    return citi
def left_nodes(nod,avoid,nods):
    node=copy.deepcopy(nod)
    if avoid:node.append(avoid)
    print(node,nods)
    node=set(node)
    nods=set(nods)
    print(node,nods)
    print(list(nods-node))
    return list(nods - node)
def get_cities_info():
    df = pd.read_excel('data/city_dataset.xlsx')
    return df
def get_datas():
    df = pd.read_excel('data/node_dataset_3.xlsx')
    #df = pd.DataFrame(df, columns=[ 'Node 1', 'Node 2', 'Distance'])
    return df.to_numpy()

def dijkstra(source,destination,avoid):
    df = pd.read_excel('data/node_dataset_3.xlsx')
    graph = Graph()
    
    df2= df[df['Node 1'] != avoid]
    df2= df2[df2['Node 2'] != avoid]

    for ind in df2.index:
        graph.add_edge(df['Node 1'][ind], df['Node 2'][ind],round(df['Distance'][ind], 1) )#int(df['Distance'][ind]
        graph.add_edge(df['Node 2'][ind],df['Node 1'][ind],round(df['Distance'][ind], 1))#int(df['Distance'][ind]
    path=find_path(graph,source,destination)
    print(path)
    return path

def nodes_result(nodes):
    #res=''.join(x+'>> ' for x in nodes)
    res=''
    cc=0
    for x in nodes:
        if cc==4:
            res+=x+' ->\n'
            cc=0
        else:
            res+=x+' -> '
            cc+=1
    return res[:-3]
def nodes_result2(costs,total_cost):
    #coss=[int(x) for x in costs]
    res=''
    cc=0
    for x in costs:
        if cc==7:
            res+=str(x)+' +\n'
            cc=0
        else:
            res+=str(x)+' + '
            cc+=1
    #res=''.join(str(x)+' + ' for x in costs)
    res= res[:-3]+' = '+str("{:.1f}".format(total_cost))+' miles'
    return res
def create_edge(nodes):
    res=[]
    for i in range(len(nodes)-1):
        res.append((nodes[i],nodes[i+1]))
    print('EDGELIST',res)
    return res
#get_cities_2()
