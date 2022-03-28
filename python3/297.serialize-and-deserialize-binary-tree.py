#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = []
        queue = [root]
        while queue:
            if queue[0] == None: out.append(queue[0])
            else:
                out.append(queue[0].val)
                queue.append(queue[0].left)
                queue.append(queue[0].right)
            queue = queue[1:]
        s = "]"
        is_num = False
        for i in range(len(out) - 1, -1, -1):
            if is_num and out[i] == None:
                s = ',null' + s
            if out[i] != None:
                is_num = True
                s = ','+ str(out[i]) + s
        s = s[1:]  
        s = '[' + s
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data[1:len(data) - 1]) == 0: return None
        data = data[1:len(data) - 1].split(',')
        head = TreeNode()
        queue = [head]
        for i in data:
            if i != 'null':
                queue[0].val = int(i)
                queue[0].left = TreeNode(val=None)
                queue[0].right = TreeNode(val=None)
                queue.append(queue[0].left)
                queue.append(queue[0].right)
            else:
                queue[0].val = None
            queue = queue[1:]
        def clean(node):
            if node.left != None and node.left.val == None:
                node.left = None
            else:
                clean(node.left)
            if node.right != None and node.right.val == None:
                node.right = None
            else:
                clean(node.right)
        clean(head)        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

