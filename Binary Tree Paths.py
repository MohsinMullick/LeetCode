class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            # left subtree
            if node.left:
                dfs(node.left, path + str(node.val) + "->")
            # right subtree
            if node.right:
                dfs(node.right, path + str(node.val) + "->")
        dfs(root, "")
        return result