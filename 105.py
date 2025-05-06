"""
LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal

Description:
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

Constraints:
- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- All the values of `inorder` are unique.
- `preorder` and `inorder` are guaranteed to be valid traversals of the same binary tree.
"""

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