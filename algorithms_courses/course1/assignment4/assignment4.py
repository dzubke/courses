# assignment4.py

# standard libraries
from collections import defaultdict
from typing import DefaultDict, List, Tuple
from random import choice
from math import log, ceil
import csv



def random_cut(graph_list):
    """The random cut algorithm. This function will run the random_cutHelper function which will performm the selection and contraction of edges in the graph
    to determine a cut. This random_cutHelper function will be run n^2 * log (n), where n is the number of nodes in the graph, to ensure that one iteration
    of the random_cutHelper will output the minimum cut. The smallest cut value will be stored and compared to every run of the random_cutHelper

    Parameters
    ----------
    graph_list: List[int]
        the input list representation of the graph.

    Returns
    --------
    min_cut: int
        the number of edges cut by the minimum cut of the graph

    """
    
    cutgraph = RandomCut(graph_list)
    
    n = len(cutgraph.graph)

    iterations: int = ceil( n * log(n) )  # the min number of iterations of the random_cutHelper must be run to ensure the minimum cut is returned

    min_cut: int = float('inf')       # the number of edges cut through the minimum cut, set to positive infinity

    for i in range(100):
        
        cutgraph = RandomCut(graph_list)        # the graph need to be re-instantiated because the random_cutHelper will reduce the graph to only 2-vertices

        cutgraph._del_selfloops()
        temp_min_cut = cutgraph.random_cutHelper()      # performs a min_cut on the graph

        if temp_min_cut < min_cut:
            min_cut = temp_min_cut

    return min_cut


class RandomCut():


    def __init__(self, graph_list: List[List[int]]):
        """ Initializes the RandomCut object. To create the graph attribute, this function takes in a list representation of a graph an converts 
            it into the dictionary representation defined in the RandomCut class. In the list representation,  the first column identifies a node 
            of the graph and the rest of the integers in the row represent the nodes that the first-column node is connected to. The dictionary 
            representation has the node-id as the key in the dictionary and the values are a list of integer id's of nodes that the key-node is connected to.
        
        Parameters
        ----------
        graph_list: List[int]
            the input list representation of the graph.


        Attributes
        ----------
        in_graph: DefaultDict[int, List[int]]
            dictionary representing a graph where the keys identify the nodes or vertices of the graph and the integers in the list signify the nodes 
            the key node is connected to (or where this is an edge between)

        """
        # initializing the graph structure
        self.graph: DefaultDict[int, List[int]] = defaultdict(list)

        for row in graph_list:
            self.graph[row[0]].extend(row[1:])

    def random_cutHelper(self):
        """This helper function to the random_cut algorithm will perform the selection and contraction
        """

        while len(self.graph) > 2:
        # for i in range(2):
            # print(f"iteration {i} graph: {self.graph}")
            # randomly pick an edge (defined by two connected nodes, node1 and node2) to be contracted
            node1, node2 = self.nodes_pick()
            # print(f"picked nodes: {node1}, {node2}")

            # merge/contract node1 and node2 into a single node
            self.contract(node1, node2)

        # count the number of edges in the final cut 
        count_list = []     # count_list is a list with two element which are the number of edges for the two nodes in the final 2-node graph
        
        for node in self.graph:
            count_list.append(len(self.graph[node]))
        
        # each remaining node should have the same number of edges
        assert count_list[0] == count_list[1], "2 nodes have different number of edges"


        return count_list[0]    # returns the number of edges from the first node, which will be the number of cut edges in this running of random_cutHelper



    def nodes_pick(self) -> Tuple[int, int]:
        """Picks a random pair of nodes (node1 and node2) from the graph based on the random seed 'seed' 

        Returns
        --------
        node1: int
            the first node randomly selected from the keys in the graph
        
        node2: int 
            the second node selected amongst the nodes node1 was connected
            

        Notes
        -------
        I'm not actually sure if the approach in this method will pick a truly random pair of nodes
        By only selecting amongst the keys first and then the nodes that the key is connect result in
        a truly random choice? I'm not exaclty sure but I'll settle for that approach for now.

        """
        # choose the first node amongst the keys
        node1 = choice([x for x in self.graph])

        # choose the second node amongst the nodes that node1 is connected to
        node2 = choice([x for x in self.graph[node1]])

        return node1, node2


    def contract(self, node1:int , node2: int):
        """contract sub-routine that merges or contracts two edges of the graph together. This sub-routine will be called on random edges by random_contraction
            the contract algorithm will perform 3 steps. If node1 and node2 are contracted, the routine will:
            1) replace all of the node2 id's in the edge lists of every other node in the graph with the node1 value with the _replace method
            2) add the nodes in the node2 edge list to the edge list of node1 with the _add method
            3) delete all of the self-loops with the _del_selfloop method
            4) remove the dict value with node2 as a key


        Parameters
        ----------
        key1: int
            the node id (key in the dict) of the first node to be contracted

        key2: int
            the node id (key in the dict) of the second node to be contracted


        Returns
        --------
        None
            the routine acts on the self object and doesn't return anything

        """

        # step 1: replace all of the node2 values in the edge lists of the other nodes with the node1 value
        self._replace(node1, node2)

        # step 2: add the nodes in the node2 edge list to the edge list of node1
        self._add(node1, node2)

        # step 3: remove self-loops
        self._del_selfloops()

        # step 4: delete node2 from the graph
        del self.graph[node2]



    
    def _replace(self, node1:int, node2: int):
        """a private routine of the contract method where all the values of key2 in the graph defaultdict are replaced by the key1 value
        """
        for key in self.graph:
            for index, value in enumerate(self.graph[key]):
                if value == node2:
                    self.graph[key][index] = node1
            
            '''
            while node2 in self.graph[key]:
                # instead of reassigning the value of the list where node2 resides, I am deleting the node2 from the list and adding the node1 value

                # self.graph[key] = [value for value in self.graph if  != node2] 
                self.graph[key].remove(node2)       # deletes the node2 value from the row
                self.graph[key].append(node1)       # adds the node1 value 
            '''


    def _add(self, node1: int, node2: int):
        """Adds the edges in the node2 edge list to the edge list of node1

        Parameters
        ---------
        node1: int
            first node whose edge list the edges in node2 will be added to

        node2: int
            the second node whose edges will be added to the edge list of node1

        Returns
        -------
        None
        """

        self.graph[node1].extend(self.graph[node2])


    def _del_selfloops(self):
        """removes the selfloops from the graph"""
        for key in self.graph:
            # while key in self.graph[key]:
                # self.graph[key].remove(key)
            self.graph[key] = [value for value in self.graph[key] if value != key]


def main():
    in_graph = [[1, 2, 3, 4, 5, 6, 1],
                [2, 1, 4, 6],
                [3, 1, 4],
                [4, 1, 2, 3],
                [5, 1],
                [6, 1, 2]]
    print(in_graph)

    cutgraph = RandomCut(in_graph)
    print(f"original graph: {cutgraph.graph}")
    print([i for i in cutgraph.graph])
    print(len(cutgraph.graph))
    
    # testing del_selfloop routine
    cutgraph._del_selfloops()
    print(f"deleted the self-loops: {cutgraph.graph}")
    
    # replacing 6 with 1
    cutgraph._replace(1, 6)
    print(f"replaces 6 with 1 in the lists: {cutgraph.graph}")

    # added the edges from node 6 to node 1
    cutgraph._add(1, 6)
    print(f"addes edges in node 6 to node 1: {cutgraph.graph}")

    # testing del_selfloop routine
    cutgraph._del_selfloops()
    print(f"deleted the self-loops again: {cutgraph.graph}")

    # deleting the 6 node from the graph
    del cutgraph.graph[6]
    print(f"deleted node 6: {cutgraph.graph}")
    

    # reinitializing the graph to test the contract sub-routine
    cutgraph = RandomCut(in_graph)
    print(f"original graph: {cutgraph.graph}")

    cutgraph.contract(1,6)
    print(f"contracted the 1 and 6 nodes: {cutgraph.graph}")


    # randomly choosing a key
    node1, node2 = cutgraph.nodes_pick()
    print(f"node1 and node2 are: {node1}, {node2}")


    # reinitializing the graph to test the random_cutHelper function
    cutgraph = RandomCut(in_graph)
    print(f"original graph: {cutgraph.graph}")

    cutgraph.random_cutHelper()
    print(f"contracted graph: {cutgraph.graph}")


    # testing the random_cut algorithm
    in_graph_1 = [[1, 2, 3, 4, 5, 6],
            [2, 1, 4, 6],
            [3, 1, 4],
            [4, 1, 2, 3],
            [5, 1],
            [6, 1, 2]]
    min_cut = random_cut(in_graph_1)
    print(f"min cut is: {min_cut}")


    with open('data.txt',  newline = '') as f:
        filtered = (line.replace('\r', '') for line in f)
        graph_reader = csv.reader(filtered, delimiter='\t')
        graph_list = [[int(num.strip()) for num in row if num != ''] for row in graph_reader]
        #graph_list = [row.remove('') for row in graph_list]

        # graph_list = [[int(num.strip()) for num in row] for row in graph_reader]

        print(graph_list)
    
        min_cut = random_cut(graph_list)
        print(f"YOU DID IT! min cut: {min_cut}")
    


if __name__ == "__main__": main()
