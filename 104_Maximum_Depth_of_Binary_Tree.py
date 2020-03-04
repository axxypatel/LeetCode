"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""

### Iterative 

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(root,1)]
        final = 0
        while stack:
            root,level = stack.pop()
            if not root.left and not root.right: 
                final = max(level,final)
            
            if root.right:
                stack.append((root.right,level+1))
            if root.left:
                stack.append((root.left,level+1))
        return final

### Recursive 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def rt(l):
            if l is None:
                return 0
            return max(rt(l.left)+1,rt(l.right)+1)
        return rt(root)
