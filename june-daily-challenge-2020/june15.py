class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return None
        elif root.val == val: return root
        else:
            if val < root.val: return self.searchBST(root.left, val)
            if val > root.val:  return self.searchBST(root.right, val)
