"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.

"""
### Iterative:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        stack = [(root.left,root.right)]
        while stack: 
            n1,n2 = stack.pop()
            if n1 is None and n2 is None:
                continue
            if not n1 or not n2:
                return n1 == n2
            if n1.val != n2.val:
                return False
            stack.append((n1.right,n2.left)) 
            stack.append((n1.left,n2.right))
        return True

### Recursive

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        def recursive_tree(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l and r:
                if l.val != r.val:
                    return False
                else:
                    return recursive_tree(l.left,r.right) and recursive_tree(l.right,r.left)
                   
        return recursive_tree(root.left,root.right)
