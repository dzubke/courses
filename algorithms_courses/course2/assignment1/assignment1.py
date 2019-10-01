# standard libraries
from typing import List, DefaultDict
from collections import defaultdict
from dataclasses import dataclass


@dataclass()
class SSCGraph():
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
    graph: DefaultDict[int, List[int]] = defaultdict(list)  # the graph in a dictionary representation
    for edge in graph_list:                                 # loops over every directed edge in the graph_list representation
        graph[edge[0]].append(edge[1])                  # assigns the tail-node (edge[0]) as the dict key and appends the head-node (edge[1]) to the list of the tail node

    n: int =  len(graph)                                    # the number of nodes in the graph
    
    v_explored: List[bool]  = [False for i in range (n)]    # a list of whether a given node has been explored (True if explored, False otherwise)

    t: int = 0                                              # the counter for the finishing time
    f_time: List[int] = [0 for i in range (n)]                         # finishing time of each node                                       

    l_node: List[int] = [0 for i in range (n)]                         # leader node of each node
    leader: int = 0                                         # the counter for the leader node      

        @classmethod
        def list_to_dict(self, graph_list: List[List[int]]) -> None:
            """this method converts an adjacency representation of a directed graph into a dictionary representation

            Parameters
            ----------
            graph_list: List[List[int]]
                in the list representation of a directed graph, each sub-list in the list of lists represented a directed edge where the tail-node is 
                the first element of the sub-list and the second element of the list is the head-node

            """
            init_graph = DefaultDict[int, List[int]] = defaultdict(list)  # the graph in a dictionary representation
            for edge in graph_list:                                 # loops over every directed edge in the graph_list representation
                init_graph[edge[0]].append(edge[1])           
            return SSCGraph(values_in_dict['name'], age=values_in_dict['age'])


    def kosaraju_SCC(self):
        """
        """

        # psuedo-code
        # 1 run DFS_backward on graph G (equivalent to running DFS on G_reverse) to compute the finishing time of each vertex
        # 2 ? reassign the node values of the graph with their finishing times ? 
        # 2 run DFS on graph G 

        for i in range(self.n, 0, -1):     # the index of the for-loop references the node numbers, and so is one-indexed meaning i runs from n to 1
            if not self.v_explored[i-1]:        # v_explored is zero-indexed so, if (i-1)th vale in v_explored (the i-th node) is False, it has not been explored
                self.leader = i                      # assign the source vertex variable to the i-th node
                # DFS(i)                        # calling DFS on the i-th node


    def DFS(self, node_i: int):
        """the depth-first search algorithm

        Parameters
        ----------
        node_i: int
            the node ID from which DFS is called
        """

        self.v_explored[node_i - 1] = True          # set the v_explored value to True means the i-th node (i-1 index in v_explored) has been explored
        self.l_node[node_i - 1] = self.leader       # assigning the leader node of node_i to the value in s
        for j in self.graph[node_i]:                # looping over all of the head-nodes that node_i has an out-going edge toward
            if not self.v_explored[j-1]:            # if the j-th node (j-1 indexed in v_explored) hasn't beeen explored,
                self.DFS(j)                         # call DFS on node j
        self.t += 1                                 # increment the t-counter for the finishing time
        self.f_time[node_i] = self.t                # assign the value of the finishing time counter t to the finishing time variable f_time for node_i


    def DFS_backward(self):
        """the depth-first search algorithm that goes backward along the edges to simulate running DFS on a reverse graph.
        """

    
def main():
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




if __name__ == "__main__": main()