from pygraphviz import *

def createimg(set1,set2):
    A=AGraph(directed=True)
    length1=len(set1)
    length2=len(set2)
    lst1=list()
    lst2=list()
    A.add_node(0,label='R')
    for i in range(length1):
        A.add_node(i+1,label=set1[i])
        A.add_edge(0,i+1)
        lst1.append(i+1)
    for i in range(1,length1+1):
        for j in range(1,length2+1):
            A.add_node(length1+length2*(i-1)+j,label=set2[j-1])
            A.add_edge(i,length1+length2*(i-1)+j)
            lst2.append(length1+length2*(i-1)+j)
    B=A.add_subgraph(1,name='S0',rank='same')
    B=A.add_subgraph(lst1,name='S1',rank='same')
    B=A.add_subgraph(lst2,name='S2',rank='same')
    A.graph_attr['rank']='same'
    A.node_attr['shape'] = 'circle'
    A.write('img.dot')
    C=AGraph('img.dot')
    C.layout(prog='dot')
    C.draw('img.png')
