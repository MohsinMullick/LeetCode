# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        node_map = {}
        children = set()

        for p, c, is_left in descriptions:
            if p not in node_map:
                node_map[p] = TreeNode(p)
            if c not in node_map:
                node_map[c] = TreeNode(c)

            parent = node_map[p]
            child = node_map[c]

            if is_left == 1:
                parent.left = child
            else:
                parent.right = child

            children.add(c)

        # Find root: the node that is not anyone's child
        for val in node_map:
            if val not in children:
                return node_map[val]

        return None  # In case of empty input