import math
import random as rnd 

#!/usr/bin/env python
try:
    import matplotlib.pyplot as plt
except:
    raise
    
import networkx as nx



def create_barabasi_albert_graph(en,em):
    n = en
    m = em
    G = nx.nx.barabasi_albert_graph(n,m)

    node_total = 130
    node_weight =  node_total/ len(G.nodes(data=True))


    edge_total = 96
    edge_weight =  edge_total/ len(G.edges(data=True))


    #G=nx.Graph()
    for n in G.nodes():
        G.add_node(n,weight=node_weight)

    for ee in G.edges(data=True):
        G.add_edge(ee[0],ee[1],weight=edge_weight)


    print G.edges(data=True)
    print G.nodes(data=True)

    return G


def plot_the_graph(G):
    elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
    esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

    pos=nx.spring_layout(G) # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=700)

    # edges
    nx.draw_networkx_edges(G,pos,edgelist=elarge,
                           width=6)
    nx.draw_networkx_edges(G,pos,edgelist=esmall,
                           width=6,alpha=0.5,edge_color='b',style='dashed')
    
    # labels
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

    plt.axis('off')
    plt.savefig("weighted_graph2.png") # save as png
    plt.show() # display


def print_graph(G, pr = 'e'):
    if pr == 'n':
        for iterator in G.nodes_iter(data=True):
            print iterator
    else:
        for iterator in G.edges_iter(data=True):
            print iterator

    
def add_node_info(G):
    d_nodes = {i:{} for i in range(len(G.nodes())) }
    #initialise cv to node weigths (reserve)
    for iterator in G.nodes_iter(data=True):
        d_nodes[iterator[0]]['cv'] =  iterator[1]['weight']
        d_nodes[iterator[0]]['ev'] = iterator[1]['weight']
        d_nodes[iterator[0]]['sv'] = 0

    for iterator in G.edges_iter(data=True):
        d_nodes[iterator[0]]['ev']= d_nodes[iterator[0]]['ev'] - iterator[2]['weight']
        d_nodes[iterator[1]]['ev']= d_nodes[iterator[1]]['ev'] + iterator[2]['weight']
    return d_nodes

def shock_nodes(G, d_nodes, kappa, phi):
    n_shocked_nodes = int(kappa*(len(G.nodes())) )
    print "number of shocked nodes for kappa %f = %d " %(kappa, n_shocked_nodes)
    shocked_nodes = []
    while len(shocked_nodes) < n_shocked_nodes:
        r = rnd.randint(0, len(G.nodes())-1)
        if r not in shocked_nodes:
            shocked_nodes.append(r)
            
    print "Nodes to be shocked : ", shocked_nodes
    for n in shocked_nodes:
        d_nodes[n]['sv'] = d_nodes[n]['ev']*(phi)
        d_nodes[n]['cv'] = d_nodes[n]['cv'] - d_nodes[n]['sv']
    print "Nodes shocked"
        

def check_shock_result(G, d_nodes):
    insolvent_nodes = set([])
    for iterator in G.edges_iter(data=True):
        if d_nodes[iterator[1]]['cv'] <=0 :
            if iterator[1] in insolvent_nodes:
                continue
            print "Node %d bankrupt !!!" %iterator[1]
            d_nodes[iterator[0]]['cv'] = d_nodes[iterator[0]]['cv'] - iterator[2]['weight']
            iterator[2]['weight'] = 0
            insolvent_nodes.add(iterator[1])
    print "Insolvent Nodes : ", insolvent_nodes
    for n in insolvent_nodes:
        G.remove_node(n)
    return insolvent_nodes        
def iterate_shocks(G, d_nodes, k):    
    insolvent_nodes = []
    i = 1
    shock_nodes(G, d_nodes, k, 0.8)
    while(1):
        print 'iteration %d' %i
        tmp = check_shock_result(G,d_nodes)
        if len(tmp) == 0:
            break
        insolvent_nodes.extend(tmp)
        i = i+1
   

def mainCall(n,m,k):
    G = create_barabasi_albert_graph(n,m)
    d_nodes = add_node_info(G)
    print_graph(G, 'e')
    print "---------------------"
    print_graph(G, 'n')

    iterate_shocks(G,d_nodes,k)
    solvent_nodes= G.nodes()
    print "nodes surviving at the end:- ", solvent_nodes
    return solvent_nodes
    
'''
Created on Feb 28, 2015

@author: Saurav
'''
