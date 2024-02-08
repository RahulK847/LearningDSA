class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        else:
            # Ignore duplicate keys
            pass

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.val)
            self._inorder_traversal_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result

    def _preorder_traversal_recursive(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result

    def _postorder_traversal_recursive(self, node, result):
        if node:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.val)

    def mirror(self):
        self._mirror_recursive(self.root)

    def _mirror_recursive(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self._mirror_recursive(node.left)
            self._mirror_recursive(node.right)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def minimum(self, node=None):
        current = node or self.root
        while current.left is not None:
            current = current.left
        return current.val

    def maximum(self, node=None):
        current = node or self.root
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            root.key = self.minimum(root.right)
            root.right = self._delete_recursive(root.right, root.key)

        return root

    def height(self, node=None):
        if node is None:
            node = self.root
        return self._height_recursive(node)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def is_balanced(self):
        return self._is_balanced_recursive(self.root)

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return abs(left_height - right_height) <= 1 and \
               self._is_balanced_recursive(node.left) and \
               self._is_balanced_recursive(node.right)

    def level_order_traversal(self):
        result = []
        if self.root is not None:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return result

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    def is_full(self):
        return self._is_full_recursive(self.root)

    def _is_full_recursive(self, node):
        if node is None:
            return True
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            return False
        return self._is_full_recursive(node.left) and self._is_full_recursive(node.right)

    def is_symmetric(self):
        return self._is_symmetric_recursive(self.root, self.root)

    def _is_symmetric_recursive(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.key == right.key) and self._is_symmetric_recursive(left.left, right.right) and self._is_symmetric_recursive(left.right, right.left)

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Inorder Traversal:", tree.inorder_traversal())

# Additional methods
print("Preorder Traversal:", tree.preorder_traversal())
print("Postorder Traversal:", tree.postorder_traversal())

print("Height of the tree:", tree.height())
print("Is the tree balanced?", tree.is_balanced())
print("Level Order Traversal:", tree.level_order_traversal())

print("Number of nodes in the tree:", tree.count_nodes())
print("Is the tree full?", tree.is_full())
print("Is the tree symmetric?", tree.is_symmetric())
