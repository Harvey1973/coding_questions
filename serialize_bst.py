# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = [] 
        result = self.traversal(root,vals)
        print(result)
        return ','.join(result)


    def traversal (self,node,vals):
        if (node) :
            vals.append(str(node.val))
            self.traversal(node.left,vals)
            self.traversal(node.right,vals)
        else :
            vals.append("None")
        return vals
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pos = -1
        data = data.split(',')
        
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
            else:
                data[i] = int(data[i])


        print(data)
        tree,pos = self.build_tree(data,pos)
        return tree

    ''' 
    Rebuilding the tree is tricky, one way to do it is keep a position pointer , traversing the 
    input string 
    '''


    def build_tree(self,data,pos):
        pos = pos + 1
        n = len(data)
        if pos > n or data[pos] == None :
            return None, pos
        root = TreeNode(data[pos])
        root.left,pos = self.build_tree(data,pos)
        root.right,pos = self.build_tree(data,pos)
        return root,pos
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

Node_1 = TreeNode(1)
Node_2 = TreeNode(2)
Node_3 = TreeNode(3)
Node_4 = TreeNode(4)
Node_5 = TreeNode(5)


Node_1.left = Node_2
Node_1.right = Node_3
Node_3.left = Node_4
Node_3.right = Node_5



a = ['1','2','3','#']
obj = Codec()
print(obj.deserialize(obj.serialize(Node_1)))



