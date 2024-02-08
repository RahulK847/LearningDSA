class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recu(self.root, value)

    def insert_recu(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recu(node.left, value)
        elif value > node.val:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recu(node.right, value)
        else:
            pass

    def inorder_traversal(self):
        result = []
        self.inorder_recu(self.root, result)
        print("Inorder Traversal: ", result)

    def inorder_recu(self, node, result):
        if node:
            self.inorder_recu(node.left, result)
            result.append(node.val)
            self.inorder_recu(node.right, result)

    def preorder_traversal(self):
        result = []
        self.preorder_recu(self.root, result)
        print("Preorder Traversal: ", result)

    def preorder_recu(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_recu(node.left, result)
            self.preorder_recu(node.right, result)

    def postorder_traversal(self):
        result = []
        self.postorder_recu(self.root, result)
        print("Postorder Traversal: ", result)

    def postorder_recu(self, node, result):
        if node:
            self.preorder_recu(node.left, result)
            self.preorder_recu(node.right, result)
            result.append(node.val)

    def get_leaf_node(self):
        print(self.leaf_node_recu(self.root))

    def leaf_node_recu(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        leaf_nodes = []
        leaf_nodes += self.leaf_node_recu(root.left)
        leaf_nodes += self.leaf_node_recu(root.right)
        return leaf_nodes

    def height(self, node=None):
        if node is None:
            node = self.root
        print("Height: ", self.height_recu(node))

    def height_recu(self, node):
        if node is None:
            return 0
        left_height = self.height_recu(node.left)
        right_height = self.height_recu(node.right)
        return 1 + max(left_height, right_height)

    def k_dist(self, k):
        print("Nodes which are K distance  away from Root Node:", end=" ")

        self.k_dist_recu(k, self.root)

    def k_dist_recu(self, k, root):
        if root is None:
            return 0
        if k == 0:
            print(root.val, end=" ")
        self.k_dist_recu(k - 1, root.left)
        self.k_dist_recu(k - 1, root.right)


bt = BinaryTree()
bt.insert(1)
bt.insert(10)
bt.insert(20)
bt.insert(5)
bt.insert(30)
bt.insert(34)
bt.get_leaf_node()
bt.inorder_traversal()
bt.preorder_traversal()
bt.postorder_traversal()
bt.height()
bt.k_dist(2)
