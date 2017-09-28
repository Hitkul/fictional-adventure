import numpy as np 
import sys
from math import log

def goal_state_found():
    print("goal state found, order of traversal was")
    print(visited)
    exit()

def get_children(root,no_of_elements):
    l_child = r_child = None
    if 2*root <= no_of_elements:
        l_child = 2*root
    if 2*root+1 <= no_of_elements:
        r_child = 2*root+1
    return (l_child,r_child)

def get_root(element):
    return element/2

def dfs(root,no_of_elements):
    visited.append(root)
    if root == goal_state:
        goal_state_found()
    else:
        children = get_children(root,no_of_elements)
        for child in children:
            if child == None:
                return 0
            else:
                dfs(child,no_of_elements)
                visited.append(root)

def bfs(root):
    queue = list()
    queue.append(root)
    while(len(queue)>0):
        temp= queue.pop(0)
        visited.append(temp)
        if temp == goal_state:
            goal_state_found()
        else:
            children = get_children(temp,no_of_elements)
            for child in children:
                if child != None:
                    queue.append(child)
    return 0



def main_dfs():
    dfs(tree[0],no_of_elements)
    print("goal state not found")

def main_bfs():
    bfs(tree[0])
    print("goal state not found")

def main_dfs_l(limit):
    if limit<0:
        print("invalid limit")
        exit()
    if limit>int(log(no_of_elements,2)):
        print("Limit more than depth, excuting DFS")
        main_dfs()
    else:
        sum =0 
        for i in range(limit+1):
            sum+=2**i
        sub_tree = tree[:sum]
        dfs(sub_tree[0],sum)
        print("goal state not found")
        return 0

def main_ids():
    limit = 0
    while(limit<=int(log(no_of_elements,2))):
        print("calling dfs with limit "+str(limit))
        main_dfs_l(limit)
        limit+=1


visited = list()
no_of_elements = 15
goal_state = 10
tree = np.arange(1,no_of_elements+1)
# print(sys.argv[1])
if sys.argv[1] == "dfs":
    main_dfs()
elif sys.argv[1] == "bfs":
    main_bfs()
elif sys.argv[1]=="dfs_l":
    main_dfs_l(int(sys.argv[2]))
elif sys.argv[1]=="ids":
    main_ids()