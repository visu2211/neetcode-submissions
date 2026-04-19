# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return " ".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None
        
        nodes = data.split(" ")
        root = TreeNode(int(nodes[0]))
        child_p = 1
        q = deque([root])
        while q:
            node = q.popleft()
            if nodes[child_p] != "N":
                node.left = TreeNode(int(nodes[child_p]))
                q.append(node.left)
            child_p += 1
            if nodes[child_p] != "N":
                node.right = TreeNode(int(nodes[child_p]))
                q.append(node.right)
            child_p += 1
        return root