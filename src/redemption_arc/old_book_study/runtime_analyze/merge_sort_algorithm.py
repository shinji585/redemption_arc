import pytest


def merge_sort(A: list) -> list: 
    
    if len(A) > 1: 
        print(f'Splitting {A}')
        mid = len(A) // 2 # this is the position of the value in the middle, it function to divide the array into two parts 
        left = A[:mid]
        right = A[mid:]
        # then we pass to the recursive call where the mergesort for left and right happens 
        merge_sort(left)
        merge_sort(right)
        
        
    # then we initialize 3 variables, i is for left positio, j is for the right part, and k is for the original array
    i, j, k = 0,0,0
    while i < len(left) and j < len(right): 
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1 
        else: 
            A[k] = right[j]
            j += 1 
        k += 1
    
    while i < len(left):
        A[k] = left[i]
        i += 1 
        k += 1 
        
    while j < len(right):
        A[k] = right[j]
        j += 1 
        k += 1 
        
    print(f'Merging {A}')
    
    return A





# learning how to write pytest without AI 
@pytest.mark.parametrize(
    "Input_list, expected_output", [
        ([], []),
        ([1], [1]),
        ([4,2,1,3], [1,2,3,4]),
        ([5,5,2,8,2], [2,2,5,5,8]),
    ]
)
def test_merge_sort(input_list: list, expected_output):
    assert merge_sort(input_list) == expected_output 