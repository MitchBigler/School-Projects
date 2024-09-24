'''
Project Name: Project 2: Sort Test Code
Author: George Rudolph
Date: 3 Jul 2020
To run test_search from command line:
python -m pytest test_sort.py
or
python3 -m pytest test_sort.py
'''
import pytest
from sorting_algorithms import selection_sort, insertion_sort, mergesort, quicksort, is_sorted
from random import seed, sample


def test_is_sorted():
    data_size = 100000
    seed(5)
    data = sample(range(data_size * 3), k=data_size)
    assert not is_sorted(data)
    data.sort()
    assert is_sorted(data)
    with pytest.raises(TypeError):
        is_sorted("Hello")
    with pytest.raises(TypeError):
        is_sorted([1, 4, 6, "Fred", 8])

def test_selection_sort1():
    short_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_list = short_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = selection_sort(short_list)
    assert sorted_list == test_list

def test_selection_sort2():
    data_size = 1000
    seed(8)
    data = sample(range(data_size * 3), k=data_size)
    long_list = data.copy()
    test_list = long_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = selection_sort(long_list)
    assert sorted_list == test_list

def test_quicksort1():
    short_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_list = short_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = quicksort(short_list)
    assert test_list == sorted_list

def test_quicksort2():
    data_size = 1000
    seed(8)
    data = sample(range(data_size * 3), k=data_size)
    long_list = data.copy()
    test_list = long_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = quicksort(long_list)
    assert sorted_list == test_list

def test_mergesort1():
    short_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_list = short_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = mergesort(short_list)
    assert sorted_list == test_list

def test_mergesort2():
    data_size = 1000
    seed(8)
    data = sample(range(data_size * 3), k=data_size)
    long_list = data.copy()
    test_list = long_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = mergesort(long_list)
    assert sorted_list == test_list

def test_insertion_sort1():
    short_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_list = short_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = insertion_sort(short_list)
    assert sorted_list == test_list

def test_insertion_sort2():
    data_size = 1000
    seed(8)
    data = sample(range(data_size * 3), k=data_size)
    long_list = data.copy()
    test_list = long_list.copy()
    test_list.sort()
    sorted_list, comparisons, swaps = insertion_sort(long_list)
    assert sorted_list == test_list

def test_hidden1():
    data_size = 1000
    seed(10)
    data = sample(range(data_size * 3), k=data_size)
    long_list = data.copy()
    test_list = long_list.copy()
    test_list.sort()
    ins_sorted_list, ins_comparisons, ins_swaps = insertion_sort(long_list)
    assert ins_sorted_list == test_list
    long_list = data.copy()
    sel_sorted_list, sel_comparisons, sel_swaps = selection_sort(long_list)
    assert sel_sorted_list == test_list
    long_list = data.copy()
    quick_sorted_list, quick_comparisons, quick_swaps = quicksort(long_list)
    assert quick_sorted_list == test_list
    long_list = data.copy()
    merge_sorted_list, merge_comparisons, merge_swaps = mergesort(long_list)
    assert merge_sorted_list == test_list
    assert sel_comparisons >= ins_comparisons and ins_comparisons >= quick_comparisons and quick_comparisons >= merge_comparisons
