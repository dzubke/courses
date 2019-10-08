# standard libraries
from typing import List, DefaultDict
from collections import defaultdict, Counter
import sys
import inspect  # used to see the size of the stack

sys.setrecursionlimit(10000) # increases the recusion limit to see if that can avoid a maximum recusion error


class SCCGraph():
    
    def __init__(self, graph_list: List[List[int]]):
        # there is a problem with taking in the graph_list as an arguement. in how it is now, it's like is a class with inheritance.
        """This class object contains a directed graph and the methods within this class will run Kosaraju's algorithm to detected the strongly connected  
            components (SCC) of the graph object.

        Parameters
        ---------

        graph_list

        Attributes
        -----------
        graph: DefaultDict[int, List[int]]
            the graph_list representation is converted to a dict representation by assigns the first element of the list (tail-node) as the key of the dict and
            appending all of the head-nodes that share the tail-node to a list in the value of the dict
                
        n: int = len(graph)
            the number of nodes in the graph. 
        
        v_explored: List[int]
            a list that marks if a vertex is explored. the list is zero-indexed, so the 1 node has the index zero (0)
        
        f_time: List[int]
            the finishing time of each node in the graph, this list is also zero indexed
        
        t: int = 0
            count how many nodes they have finished exploring - it is the count of the current finishing time
        
        l_node: List[int]
            the leader node of each node in the graph. nodes in each SCC will have the same leader node, this list is also zero indexed
        
        leader: int = 0
            the most recent source vertex from which a DFS was initiated - it is used to identify the leader node


        Note
        -------
        all of the lists holding values about nodes like v_explored, f_time, l_node are all zero-indexed meaning that node 1 has the index zero (0)
        """
        
        self.graph: DefaultDict[int, List[int]] = defaultdict(list)  # the graph in a dictionary representation

        for edge in graph_list:                                 # loops over every directed edge in the graph_list representation
            self.graph[edge[0]].append(edge[1])                  # assigns the tail-node (edge[0]) as the dict key and appends the head-node (edge[1]) to the list of the tail node

        self.ftime_graph: DefaultDict[int, List[int]] = defaultdict(list)  # the graph with the new node values from the finishing times
        self.fill_missing_nodes()

        self.n: int =  len(self.graph)                                    # the number of nodes in the graph
        
        # I will rap

        self.v_explored: List[bool]  = [False for i in range (self.n)]    # a list of whether a given node has been explored (True if explored, False otherwise)

        self.t: int = 0                                              # the counter for the finishing time
        self.f_time: List[int] = [0 for i in range (self.n)]                         # finishing time of each node                                       

        self.l_node: List[int] = [0 for i in range (self.n)]                         # leader node of each node
        self.leader: int = 0                                         # the counter for the leader node      
    

    def kosaraju_SCC(self):
        """
        """

        # psuedo-code

        # 1 run DFS_backward on graph G (equivalent to running DFS on G_reverse) to compute the finishing time of each vertex
        for i in range(self.n, 0, -1):     # the index of the for-loop references the node numbers, and so is one-indexed meaning i runs from n to 1
            if not self.v_explored[i-1]:        # v_explored is zero-indexed so, if (i-1)th vale in v_explored (the i-th node) is False, it has not been explored
                self.DFS_backward(i)            # calling DFS on the i-th node

        #2 reassign the node values of the graph with their finishing times
        self.assign_finishing_time(self.f_time)
 

        # 3 run DFS on the new graph G 
        self.v_explored = [False for i in range (self.n)]       # reinitialize v_explored back to all false
        for i in range(self.n, 0, -1):     # the index of the for-loop references the node numbers, and so is one-indexed meaning i runs from n to 1
            if not self.v_explored[i-1]:        # v_explored is zero-indexed so, if (i-1)th vale in v_explored (the i-th node) is False, it has not been explored
                self.leader = i                      # assign the source vertex variable to the i-th node
                self.DFS(i)                        # calling DFS on the i-th node


    def DFS(self, node_i: int):
        """the depth-first search algorithm

        Parameters
        ----------
        node_i: int
            the node ID from which DFS is called
        """
        # print(f"dfs on node_i: {node_i} begins")
        self.v_explored[node_i - 1] = True          # set the v_explored value to True means the i-th node (i-1 index in v_explored) has been explored
        self.l_node[node_i - 1] = self.leader       # assigning the leader node of node_i to the value in s
        # print(f"leader: {self.leader}")
        for j in self.ftime_graph[node_i]:                # looping over all of the head-nodes that node_i has an out-going edge toward
            if not self.v_explored[j-1]:            # if the j-th node (j-1 indexed in v_explored) hasn't beeen explored,
                self.DFS(j)                         # call DFS on node j
                # print(f"dfs called on: {j}")
        # self.t += 1                                 # increment the t-counter for the finishing time
        # print(f"t of: {self.t} for node: {node_i}")
        # self.f_time[node_i-1] = self.t                # assign the value of the finishing time counter t to the finishing time variable f_time for node_i
        # print(f"dfs on node_i: {node_i} ends")
        # print("")


    def DFS_backward(self, node_i):
        """the depth-first search algorithm that goes backward along the edges to simulate running DFS on a reverse graph.
        """

        # print(f"\n dfsback: fs_backward on node_i: {node_i} begins")
        self.v_explored[node_i - 1] = True          # set the v_explored value to True means the i-th node (i-1 index in v_explored) has been explored
        
        # debugging code that checks the number of nodes explored
        if sum(self.v_explored) % 100 == 0:
            print(f"count of v_explored: {sum(self.v_explored)}")
            print(f"size of current stack is: {len(inspect.stack())}")

        keys_with_nodei = [key for key, val in self.graph.items() if node_i in val]     # a list of nodes which are 'head-nodes' of edges with node_i as a tail-node 
        # print(f"dfsback: keys with node_i: {keys_with_nodei}")

        for j in keys_with_nodei:                # looping over all of the head-nodes that node_i has an out-going edge toward
            # print(f"dfsback: DFS_backward j's: {j}")
            if not self.v_explored[j-1]:            # if the j-th node (j-1 indexed in v_explored) hasn't beeen explored,
                # print(f"dfsback: dfs_backward called on: {j}")
                self.DFS_backward(j)                         # call DFS on node j
        
        self.t += 1                                 # increment the t-counter for the finishing time
        # print(f"dfsback: t of: {self.t} for node: {node_i}")
        self.f_time[node_i-1] = self.t                # assign the value of the finishing time counter t to the finishing time variable f_time for node_i
        # print(f"dfsback: dfs_backward on node_i: {node_i} ends")
        # print("")


    def assign_finishing_time(self, in_f_time):
        """This function renames the nodes in self.graph with the finishing times in self.f_time
        """
       # print(f"ftime list: {in_f_time}")
       # this for-loop will swap the nodes and f_time nodes in the list in each dictionary. 

        for key, dict_list in self.graph.items():
            ftime_nodes = [l_val for i, l_val in enumerate(in_f_time) if i + 1 in dict_list]

            self.ftime_graph.update({in_f_time[key-1]: ftime_nodes})
            
            # print(f"key: {key}, dict_list: {dict_list}, ftime nodes: {ftime_nodes}")
            # self.graph[key] = ftime_nodes
            # self.graph.update({key: ftime_nodes})
    
    def fill_missing_nodes(self):
        """this functions fills in missing nodes in the keys of the dictionary and the values are empty lists
        """

        for i in range(max(self.graph.keys())):
            if i+1 not in self.graph.keys():
                self.graph[i+1] = []
          

            



    
def main():
    '''
    graph_list = [[1, 4],
                  [2, 8],
                  [3, 6],
                  [4, 7],
                  [5, 2],
                  [6, 9],
                  [7, 1],
                  [8, 5],
                  [8, 6],
                  [9, 3],
                  [9, 7]
                 ]

    test_graph = SCCGraph(graph_list)
    print(test_graph.graph.items())
    # test_graph.DFS(9)
    test_graph.kosaraju_SCC()
    # test_graph.DFS_backward(9)
    print(f"v_explored: {test_graph.v_explored}, finishing time: {test_graph.f_time}, leader: {test_graph.l_node}")

    
    # f_time = [7, 3, 1, 8, 2, 5, 9, 4, 6]
    # test_graph.assign_finishing_time(f_time)
    # print(f"new graph: {test_graph.ftime_graph}")

    '''
    print(f"max recursion limit: {sys.getrecursionlimit()}")
    graph_list = list()
    with open('data.txt',  newline = '') as f:
        for line in f:
            graph_list.append([int(i) for i in line.split()])
        print(f"lenght of graph list: {len(graph_list)}")

        SCC_graph = SCCGraph(graph_list)
        print(f"n-value of dict: {SCC_graph.n}")

        print(f"len of dict graph: {len(SCC_graph.graph)}")
        print(f"len of dict keys: {len(list(SCC_graph.graph.keys()))}")
        print(f"last 10 keys of dict graph: {list(SCC_graph.graph.keys())[-10:]}")
        print(f"max value of keys: {max(SCC_graph.graph.keys())}")


        SCC_graph.kosaraju_SCC()
        SCC_counter = Counter(SCC_graph.l_node)
        print(SCC_counter.most_common(5))
        
        #print(data_list[0:15])












if __name__ == "__main__": main()