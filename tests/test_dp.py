from multiprocessing.sharedctypes import Value
from algorithms.dp import (
    assign_unique_caps,
    tsp,
    max_profit_naive, max_profit_optimized,
    climb_stairs, climb_stairs_optimized,
    count,
    combination_sum_topdown, combination_sum_bottom_up,
    edit_distance,
    egg_drop,
    fib_recursive, fib_list, fib_iter,
    hosoya_testing,
    house_robber,
    Job, schedule,
    Item, get_maximum_value,
    longest_increasing_subsequence,
    longest_increasing_subsequence_optimized,
    longest_increasing_subsequence_optimized2,
    int_divide,find_k_factor,
    planting_trees, regex_matching
)


import unittest
import math

'''
This class test the dynamic programming with bit masking algorithm
defined in algorithms/dp/bitmasking.py
'''
class TestBitmaskingCapAssignment(unittest.TestCase):
    # === Relates to requirement R1.1 "No cap sets" ===
    # Checks that a value error is raised when the nr of cap sets is 0.
    def test_no_cap_sets(self):
        with self.assertRaises(ValueError):
            assign_unique_caps([],0)

    # === Relates to requirement R1.2 "Person without caps" ===
    # Checks that the output is 0 when there is one or more empty cap sets. This means there is 
    # at least one person that cannot be assigned a cap.
    def test_person_without_caps(self):
        self.assertEquals(assign_unique_caps([[1,2,3], [], [2,5,6]],6), 0)

    # === Relates to requirement R1.3 "No unique cap assignment" ===
    # Checks that the output is 0 when there are no unique cap assignments, even though all of the 
    # cap sets contain at least one cap.
    def test_no_unique_cap_assignment(self):
        self.assertEquals(assign_unique_caps([[1,2,3], [4], [4]], 5), 0)
        
    # === Relates to requirement R1.4 "One or more unique cap assignments" ===
    # Checks that the output is greater than 0 (and corresponds to the correct number of 
    # unique assignments) when the cap sets allow for at least one unique assignment.
    def test_one_or_more_unique_cap_assignments(self):
        self.assertEquals(assign_unique_caps([[1,2,3], [4], [1,2]], 6), 4)
    
    # === Relates to requirement R1.5 "Too Many People" ===
    # Checks that if the amount of people (i.e. cap sets) are too large we raise a value error.
    def test_too_many_people(self):
        with self.assertRaises(ValueError):
            assign_unique_caps([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]],11)    

    # === Relates to requirement R1.6 "Faulty CapIds" ===
    # Checks that if one of the cap ids are supplied in the wrong format a value error is raised.
    def test_faulty_string(self):
        with self.assertRaises(ValueError):
            assign_unique_caps([[1],['2']],2)
    
    # === Relates to requirement R1.7 "Faulty collection input" ===
    # Checks that a value error is raised when the list of caps is provided as the wrong type of collection.
    def test_faulty_collection(self):
        with self.assertRaises(ValueError):
            assign_unique_caps([[1],{2}],2)

     # === Relates to requirement R1.8 "CapId too low" ===
    # Checks that the highest supplied capId matches the cap with the highest id.
    def test_too_many_sets(self):
        with self.assertRaises(ValueError):
            assign_unique_caps([[1],[2]],1)
        
class TestBitmaskingTSP(unittest.TestCase):
    # === Relates to requirement R2.1 "No nodes" ===
    # Checks that a ValueError is raised when the list of nodes is empty
    def test_no_nodes(self):
        nodes = []
        nbRow = 0
        nbColumn = 0
        with self.assertRaises(ValueError):
            tsp(nodes, nbRow, nbColumn)

    # === Relates to requirement R2.2 "One node" ===
    # Checks that the output is 0 when there is only one node
    def test_one_node(self):
        nodes = [['*']]
        nbRow = 1
        nbColumn = 1
        self.assertEquals(tsp(nodes, nbRow, nbColumn), 0)

    # === Relates to requirement R2.3 "Positive path length" ===
    # Checks that the output is a positive number that corresponds to the length of the 
    # shortest Euler circuit
    def test_positive_path_length(self):
        nodes = [
            ['.', '.', '.', '.', '.', '*', '.'],
            ['.', '.', '.', '#', '.', '.', '.'],
            ['.', '*', '.', '#', '.', '*', '.'],
            ['.', '.', '.', '.', '.', '*', '.']
        ]
        nbRow = 4
        nbColumn = 7
        self.assertEquals(tsp(nodes, nbRow, nbColumn), 16)
        
    # === Relates to requirement R2.4 "No solution" ===
    # Checks that the output is inf when there is at least one unreachable node 
    def test_no_solution(self):
        nodes = [
            ['.', '.', '.', '#', '.', '.', '.'], 
            ['.', '.', '.', '#', '.', '*', '.'], 
            ['.', '.', '.', '#', '.', '.', '.'], 
            ['.', '*', '.', '#', '.', '*', '.'], 
            ['.', '.', '.', '#', '.', '.', '.']
        ]
        nbRow = 5
        nbColumn = 7
        self.assertEquals(tsp(nodes, nbRow, nbColumn), math.inf)
        
        
    # === Relates to requirement R2.5 "Faulty dimensions" ===
    # Checks a ValueError is raised when the dimensions of the graph don't correspond to 
    # the dimension parameters
    def test_faulty_dimensions(self):
        nodes = [
            ['.', '.', '.', '.', '.', '*', '.'],
            ['.', '.', '.', '#', '.', '.', '.'],
            ['.', '*', '.', '#', '.', '*', '.'],
            ['.', '.', '.', '.', '.', '*', '.']
        ]
        nbRow = 3
        nbColumn = 7
        with self.assertRaises(ValueError):
            tsp(nodes, nbRow, nbColumn)
        nbRow = 4
        nbColumn = 8
        with self.assertRaises(ValueError):
            tsp(nodes, nbRow, nbColumn)
        
    # === Relates to requirement R2.6 "Wrong collection type" ===
    # Checks that a value error is raised when the collection of nodes is of the wrong type.
    def test_wrong_collection_type(self):
        nodes = [
            {'.', '.', '.', '.', '.', '.', '*'}
        ]
        nbRow = 1
        nbColumn = 7
        with self.assertRaises(ValueError):
            tsp(nodes, nbRow, nbColumn)
    
    # === Relates to requirement R2.7 "Wrong node type" ===
    # Checks that a value error is raised when a node is of the wrong type.
    def test_wrong_node_type(self):
        nodes = [
            ['.', '.', '.', '.', '.', 'X', '*']
        ]
        nbRow = 1
        nbColumn = 7
        with self.assertRaises(ValueError):
            tsp(nodes, nbRow, nbColumn)

    # === Relates to requirement R2.8 "Too many houses" ===
    # Checks that a value error is raised when too many houses are provided.
    def test_too_many_houses(self):
        nodes = [
            ['*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*']
        ]
        nbRow = 2
        nbColumn = 7
        with self.assertRaises(ValueError):
            tsp(nodes, nbRow, nbColumn)
    
        
class TestBuySellStock(unittest.TestCase):
    def test_max_profit_naive(self):
        self.assertEqual(max_profit_naive([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit_naive([7, 6, 4, 3, 1]), 0)

    def test_max_profit_optimized(self):
        self.assertEqual(max_profit_optimized([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit_optimized([7, 6, 4, 3, 1]), 0)


class TestClimbingStairs(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(2), 2)
        self.assertEqual(climb_stairs(10), 89)

    def test_climb_stairs_optimized(self):
        self.assertEqual(climb_stairs_optimized(2), 2)
        self.assertEqual(climb_stairs_optimized(10), 89)


class TestCoinChange(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count([1, 2, 3], 4), 4)
        self.assertEqual(count([2, 5, 3, 6], 10), 5)


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum_topdown(self):
        self.assertEqual(combination_sum_topdown([1, 2, 3], 4), 7)

    def test_combination_sum_bottom_up(self):
        self.assertEqual(combination_sum_bottom_up([1, 2, 3], 4), 7)


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance('food', 'money'), 4)
        self.assertEqual(edit_distance('horse', 'ros'), 3)


class TestEggDrop(unittest.TestCase):
    def test_egg_drop(self):
        self.assertEqual(egg_drop(1, 2), 2)
        self.assertEqual(egg_drop(2, 6), 3)
        self.assertEqual(egg_drop(3, 14), 4)


class TestFib(unittest.TestCase):
    def test_fib_recursive(self):
        self.assertEqual(fib_recursive(10), 55)
        self.assertEqual(fib_recursive(30), 832040)

    def test_fib_list(self):
        self.assertEqual(fib_list(10), 55)
        self.assertEqual(fib_list(30), 832040)

    def test_fib_iter(self):
        self.assertEqual(fib_iter(10), 55)
        self.assertEqual(fib_iter(30), 832040)


class TestHosoyaTriangle(unittest.TestCase):
    """[summary]
    Test for the file hosoya_triangle

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_hosoya(self):
        self.assertEqual([1], hosoya_testing(1))
        self.assertEqual([1,
                         1, 1,
                         2, 1, 2,
                         3, 2, 2, 3,
                         5, 3, 4, 3, 5,
                         8, 5, 6, 6, 5, 8],
                         hosoya_testing(6))
        self.assertEqual([1,
                          1, 1,
                          2, 1, 2,
                          3, 2, 2, 3,
                          5, 3, 4, 3, 5,
                          8, 5, 6, 6, 5, 8,
                          13, 8, 10, 9, 10, 8, 13,
                          21, 13, 16, 15, 15, 16, 13, 21,
                          34, 21, 26, 24, 25, 24, 26, 21, 34,
                          55, 34, 42, 39, 40, 40, 39, 42, 34, 55],
                         hosoya_testing(10))


class TestHouseRobber(unittest.TestCase):
    def test_house_robber(self):
        self.assertEqual(44, house_robber([1, 2, 16, 3, 15, 3, 12, 1]))


class TestJobScheduling(unittest.TestCase):
    def test_job_scheduling(self):
        job1, job2 = Job(1, 3, 2), Job(2, 3, 4)
        self.assertEqual(4, schedule([job1, job2]))


class TestKnapsack(unittest.TestCase):
    def test_get_maximum_value(self):
        item1, item2, item3 = Item(60, 10), Item(100, 20), Item(120, 30)
        self.assertEqual(220, get_maximum_value([item1, item2, item3], 50))

        item1, item2, item3, item4 = Item(60, 5), Item(50, 3), Item(70, 4), Item(30, 2)
        self.assertEqual(80, get_maximum_value([item1, item2, item3, item4],
                                               5))


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
        self.assertEqual(5, longest_increasing_subsequence(sequence))


class TestLongestIncreasingSubsequenceOptimized(unittest.TestCase):
    def test_longest_increasing_subsequence_optimized(self):
        sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
        self.assertEqual(5, longest_increasing_subsequence(sequence))


class TestLongestIncreasingSubsequenceOptimized2(unittest.TestCase):
    def test_longest_increasing_subsequence_optimized2(self):
        sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
        self.assertEqual(5, longest_increasing_subsequence(sequence))


class TestIntDivide(unittest.TestCase):
    def test_int_divide(self):
        self.assertEqual(5, int_divide(4))
        self.assertEqual(42, int_divide(10))
        self.assertEqual(204226, int_divide(50))


class Test_dp_K_Factor(unittest.TestCase):
    def test_kfactor(self):
        # Test 1
        n1 = 4
        k1 = 1
        self.assertEqual(find_k_factor(n1, k1), 1)

        # Test 2
        n2 = 7
        k2 = 1
        self.assertEqual(find_k_factor(n2, k2), 70302)

        # Test 3
        n3 = 10
        k3 = 2
        self.assertEqual(find_k_factor(n3, k3), 74357)

        # Test 4
        n4 = 8
        k4 = 2
        self.assertEqual(find_k_factor(n4, k4), 53)

        # Test 5
        n5 = 9
        k5 = 1
        self.assertEqual(find_k_factor(n5, k5), 71284044)


class TestPlantingTrees(unittest.TestCase):
    def test_simple(self):
        # arrange
        trees = [0, 1, 10, 10]
        L = 10
        W = 1

        # act
        res = planting_trees(trees, L, W)

        # assert
        self.assertEqual(res, 2.414213562373095)

    def test_simple2(self):
        # arrange
        trees = [0, 3, 5, 5, 6, 9]
        L = 10
        W = 1

        # act
        res = planting_trees(trees, L, W)

        # assert
        self.assertEqual(res, 9.28538328578604)
    
class TestRegexMatching(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(regex_matching.is_match(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(regex_matching.is_match(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(regex_matching.is_match(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(regex_matching.is_match(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(regex_matching.is_match(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(regex_matching.is_match(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(regex_matching.is_match(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(regex_matching.is_match(s, p))


if __name__ == '__main__':
    unittest.main()
