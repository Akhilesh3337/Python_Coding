class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.ans


# Assuming you have a TreeNode class defined as follows:
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Example to test the function:
# Constructing a binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3