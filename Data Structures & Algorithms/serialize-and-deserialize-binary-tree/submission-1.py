# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        s = []

        def dfs(root):
            if not root:
                s.append("null")
                return None
            
            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(s)
        

    def deserialize(self, data):
        nums = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            if nums[i] == "null":
                i += 1
                return None
            
            node = TreeNode(int(nums[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))