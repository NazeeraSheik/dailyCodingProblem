'''A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1  '''

 class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
        
def is_unival(root):
    if root == None:
        return True
    if root.left != None:
        if root.value != root.left.value:
            return False
    if root.right != None:
        if root.value != root.right.value:
            return False
    if (not is_unival(root.left)) & (is_unival(root.right)): 
        return True
    return False

def count_unival_subtrees(root):
    if root == None:
        return 0
    left =count_unival_subtrees(root.left)
    right =count_unival_subtrees(root.right)
    if is_unival(root):
        return 1+left+right
    else:
        return left+right

head=Node(0)
head.left=Node(1)
head.right=Node(0)
head.right.left=Node(1)
head.right.right=Node(0)
head.right.left.left=Node(1)
head.right.left.right=Node(1)
print(count_unival_subtrees(head))
