# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        q = deque()
        q.append(root)

        s = []

        while q:
            cur = q.popleft()
            
            if cur:
                s.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                s.append("null")
        
        while s and s[-1] == "null":
            s.pop()
            
        return ','.join(s)
        

    def deserialize(self, data):
        data = data.split(",")
        if not data or not data[0] or data[0] == "null":
            return None
        
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)

        i = 1

        while q:
            node = q.popleft()

            if i < len(data) and data[i] != "null":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1

            if i < len(data) and data[i] != "null":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i += 1

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))