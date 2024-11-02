from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthRecurrsion(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        level = 0
        current_lvl = []
        next_lvl = []
        current_lvl.append(root)

        while len(current_lvl) > 0:
            level += 1

            for node in current_lvl:
                if node.left is not None:
                    next_lvl.append(node.left)
                                
                if node.right is not None:
                    next_lvl.append(node.right)

            current_lvl = next_lvl
            next_lvl = []

        return level


    def create_tree(self, tree: list[int], index=0) -> Optional[TreeNode]:
        if index > len(tree):
            return None

        if tree[index] is not None:
            node = TreeNode(tree[index])
            node.left = self.create_tree(tree, 2*index + 1)
            node.right = self.create_tree(tree, 2*(index + 1))

            return node

        return None
    
def main():
    solution = Solution()

    root = [3,9,20,None,None,15,7]
    root_node = solution.create_tree(root, 0)
    r = solution.maxDepth(root_node)
    print(r)

    root = [1,None,2]
    root_node = solution.create_tree(root, 0)
    r = solution.maxDepth(root_node)
    print(r)

if __name__ == "__main__":
    main()

        