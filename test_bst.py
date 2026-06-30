from bst_sort import BinaryTreeSort
from hello import greet


def test_greet_default():
    assert greet() == "Hello, dogci!"


def test_greet_custom():
    assert greet("world") == "Hello, world!"


def test_binary_tree_sort_empty():
    assert BinaryTreeSort().sort([]) == []


def test_binary_tree_sort_sorted():
    assert BinaryTreeSort().sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_binary_tree_sort_unsorted():
    assert BinaryTreeSort().sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_binary_tree_sort_duplicates():
    assert BinaryTreeSort().sort([5, 5, 5, 1]) == [1, 5, 5, 5]
