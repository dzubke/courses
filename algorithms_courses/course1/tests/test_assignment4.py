# standard libraries 
import unittest
import sys
from collections import defaultdict

# project libraries
from assignment4.assignment4 import RandomCut

sys.path.insert(1, '/Users/dustin/CS/projects/courses/algorithms_course/assignment4')


class TestRandomCut(unittest.TestCase):

    def test___init__(self):
        in_graph = [[1, 2, 3, 4, 5, 6], [2, 1, 4, 6], [3, 1, 4], [4, 1, 2, 3], [5, 1], [6, 1, 2]]
        
        cutgraph = RandomCut(in_graph)

        self.assertEqual(type(cutgraph.graph), defaultdict)
        self.assertEqual(len(cutgraph.graph), 6)
        self.assertEqual(cutgraph.graph[1], [2, 3, 4, 5, 6] )

    def test__del_selfloops(self):
        """Tests the private _del_selfloops method"""

        in_graph = [[1, 2, 3, 4, 5, 6, 1], [2, 1, 4, 6], [3, 1, 4], [4, 1, 2, 3], [5, 1], [6, 1, 2]]
        
        cutgraph = RandomCut(in_graph)

        cutgraph._del_selfloops()

        self.assertEqual(cutgraph.graph[1], [2, 3, 4, 5, 6] )
    
    def test__replace(self):
        """Tests the private _replace() method"""
        in_graph = [[1, 2, 3, 4, 5, 6], [2, 1, 4, 6], [3, 1, 4], [4, 1, 2, 3], [5, 1], [6, 1, 2]]
        
        cutgraph = RandomCut(in_graph)

        cutgraph._replace(1, 6)

        self.assertEqual(cutgraph.graph, {1: [2, 3, 4, 5, 1], 2: [1, 4, 1], 3: [1, 4], 4: [1, 2, 3], 5: [1], 6: [1, 2]})
        

    def test__add(self):
        """Tests the private_add() method"""
        in_graph = [[1, 2, 3, 4, 5, 6], [2, 1, 4, 6], [3, 1, 4], [4, 1, 2, 3], [5, 1], [6, 1, 2]]
        
        cutgraph = RandomCut(in_graph)

        cutgraph._add(1, 6)

        self.assertEqual(cutgraph.graph, {1: [2, 3, 4, 5, 6, 1, 2], 2: [1, 4, 6], 3: [1, 4], 4: [1, 2, 3], 5: [1], 6: [1, 2]})


    def test_contract(self):
        """Tests the contract() sub-routine which merges/contracts the edges of a graph"""
        in_graph = [[1, 2, 3, 4, 5, 6], [2, 1, 4, 6], [3, 1, 4], [4, 1, 2, 3], [5, 1], [6, 1, 2]]
        
        cutgraph = RandomCut(in_graph)

        cutgraph.contract(1, 6)

        self.assertEqual(cutgraph.graph, {1: [2, 3, 4, 5, 2], 2: [1, 4, 1], 3: [1, 4], 4: [1, 2, 3], 5: [1]})


    def test_nodes_pick(self):
        """I can't think of great ways to test a method that randomly selects the pair of nodes to be contracted
            I could use an inequality but think that seems a bit silly. For now, I'll wait.
        """
        pass