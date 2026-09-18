#this program will be used to solve OAs


from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right


def solution(nums):
    # Write your code here
    pass


if __name__ == "__main__":
    tests = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1, 1],
        [-3, -1, 0, 2, 5],
    ]

    for test in tests:
        print("Input:", test)
        print("Output:", solution(test))
        print()