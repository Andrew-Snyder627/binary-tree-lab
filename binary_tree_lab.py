from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    # Recursively get depth of left and right subtree
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1 # Add 1 to include the current node

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    return root # Split point. One node on each side, or root is p or q
