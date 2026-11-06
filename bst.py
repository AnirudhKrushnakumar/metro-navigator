class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _validate_key(self, key):
        if not isinstance(key, (int, str)):
            raise TypeError(f"Key must be int or string, got {type(key).__name__}")

    def insert(self, key, value):
        self._validate_key(key)

        if self.root is None:
            self.root = TreeNode(key, value)
            self._size += 1
            return

        current = self.root
        while True:
            if key == current.key:
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = TreeNode(key, value)
                    self._size += 1
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(key, value)
                    self._size += 1
                    return
                current = current.right

    def contains(self, key):
        self._validate_key(key)
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def __contains__(self, key):
        return self.contains(key)

    def get(self, key):
        self._validate_key(key)
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        raise KeyError(f"Key not found: {key}")

    def __getitem__(self, key):
        return self.get(key)

    def inorder(self):
        result = []
        def _traverse(node):
            if node is not None:
                _traverse(node.left)
                result.append(node.key)
                _traverse(node.right)
        _traverse(self.root)
        return result

    def preorder(self):
        result = []
        def _traverse(node):
            if node is not None:
                result.append(node.key)
                _traverse(node.left)
                _traverse(node.right)
        _traverse(self.root)
        return result

    def postorder(self):
        result = []
        def _traverse(node):
            if node is not None:
                _traverse(node.left)
                _traverse(node.right)
                result.append(node.key)
        _traverse(self.root)
        return result

    def level_order(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return result

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.key, current.value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return (current.key, current.value)

    def min_key(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.find_min()[0]

    def max_key(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.find_max()[0]

    def height(self):
        if self.root is None:
            return 0
        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def count_leaves(self):
        if self.root is None:
            return 0
        def _count(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return _count(node.left) + _count(node.right)
        return _count(self.root)

    def range_query(self, min_key, max_key):
        result = []
        def _range(node):
            if node is None:
                return
            if node.key > min_key:
                _range(node.left)
            if min_key <= node.key <= max_key:
                result.append(node.key)
            if node.key < max_key:
                _range(node.right)
        _range(self.root)
        return result

    def is_valid_bst(self):
        def _validate(node, low=None, high=None):
            if node is None:
                return True
            if low is not None and node.key <= low:
                return False
            if high is not None and node.key >= high:
                return False
            return _validate(node.left, low, node.key) and _validate(node.right, node.key, high)
        return _validate(self.root)

    def delete(self, key):
        self._validate_key(key)
        deleted = [False]

        def _remove(node, key):
            if node is None:
                return None

            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                deleted[0] = True
                if node.left is None:
                    self._size -= 1
                    return node.right
                elif node.right is None:
                    self._size -= 1
                    return node.left

                successor = node.right
                while successor.left is not None:
                    successor = successor.left

                node.key = successor.key
                node.value = successor.value
                node.right = _remove(node.right, successor.key)

            return node

        self.root = _remove(self.root, key)
        return deleted[0]