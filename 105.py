# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(p, i):
            if not i: return None

            pivot = i.index(p[0])

            node = TreeNode(p[0])
            node.left = dfs(p[1:pivot + 1], i[:pivot])
            node.right = dfs(p[pivot + 1:], i[pivot + 1:])

            return node
        
        return dfs(preorder, inorder)