class TNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        self._subtreePreorder(self.root)

    def _subtreePreorder(self, p):
        if p is not None:
            print(p.data)
            self._subtreePreorder(p.left)
            self._subtreeProdrder(p.right)

    def height(self):
        self._subtreeHeight(self.root)

    def _subtreeHeight(self, p):
        if p is None:
            return 0
        else:
            hright = self._subtreeHeight(p.right)
            hleft = self._subtreeHeight(p.left)
            return 1+max(hright, hleft)

    def size(self):
        self._subtreeSize(self.root):

    def _subtreeSize(self,p):
        if p is None:
            return 0
        else:
            return 1+self._subtreeSize(p.left) + self._subtreeSize(p.right)

    def _subtreeCountLeaf(self, p):
        if p is None:
            return 0
        elif p.left is None and p.right is None:
            return 1
        else:
            return self._subtreeCountLeaf(p.left) +self._subtreeCountLeaf(p.right)



def binarySearch(a, key):
    left = 0
    right = len(a)-1
    while left<=right:
        mid = (left+right)//2
        if key == a[mid]:
            return True
        elif key <a[mid]:
            right = mid-1
        else:
            left = mid+1
    return False



def binarySearch1(a, key,left, right):
    if left > right:
        return None
    else:
        mid = (left+right)//2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return binarySearch1(a, key, left, mid-1)
        else:
            return binarySearch1(a, key, mid+1, right)
        


    

class TreeNode:
    def __init__(self,key,value,left= None, right = None):
        self.key = key
        self.value=value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def search1(self,key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else
                node = node.right
        return None
    

    def search2(self,key):
        return self._searchBst(self.root,key)

    def _searchBst(self,node,key):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        elif key <node.key:
            return self._searchBst(node.left, key)
        elif key > node.key:
            return self._searchBst(node.right, key)
        else:
            pass
        return None

    def minimum(self):
        node = self.root
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node.key
    def maximum(self):
        node = node.right
        if node is None:
            return None
        while node.right != None:
            node = node.right
        return node.key

    def insert(self,key, value):
        self.root = self._insertSubtree(self.root, key, value)

    def _insertSubtree(self, node, key, value):
        if node == None:
            return TreeNode(key , value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        else:
            pass
        return node

    def _insertSubtree(self, node,key, value):
        if node == None:
            return TreeNode(key, value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        else:
            pass
        return node

    def _minNode(self, node):
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)

    def _minNode1(self,node):
        if node is None:
            return None
        while node.left != None:
            node = node.left

        return node














































