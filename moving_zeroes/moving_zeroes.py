'''
Input: a List of integers
Returns: a List of integers
'''
from collections import deque

def moving_zeroes(arr):
    # Your code here
    new_arr = []
    for item in arr:
        if item in arr:
            if item != 0:
                new_arr.insert(0, item)
            else:
                new_arr.append(item)
    return new_arr

def moving_zeroes_next(arr):
    new_arr = deque()
    for item in arr:
        if item != 0:
            new_arr.appendleft(item)
        else:
            new_arr.append(item)

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")