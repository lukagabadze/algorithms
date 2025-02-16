"""
There are 2 ways to store a binary tree

1) Using a class
2) Using an array


This file is gonna show the array implementation
which is what's used in coding problems everywhere
"""


# binary tree stored as a list
# for a node at index i, left child = 2*i + 1, right child = 2*i + 2
binary_tree = [10, 3, 5, 2, 9, 11, 23]
#              0   1  2  3  4  5   6


def traverse(node_ind):
    if node_ind < len(binary_tree):
        value = binary_tree[node_ind]
        left = node_ind * 2 + 1
        right = node_ind * 2 + 2

        print(value, end=" ")
        traverse(left)
        traverse(right)


if __name__ == "__main__":
    traverse(0)
