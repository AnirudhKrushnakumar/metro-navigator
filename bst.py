class TreeNode:
    """One node of a binary search tree."""

    def __init__(self, key, value):
        """Create a leaf node holding key and value."""
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """A binary search tree of int or string keys (keys cannot be mixed)."""

    def __init__(self):
        """Create an empty tree."""
        self.root = None
        self._size = 0

    def __len__(self):
        """Return the number of keys stored."""
        return self._size

    def is_empty(self):
        """Return True if the tree has no keys."""
        return self._size == 0

    def _validate_key(self, key):
        """Raise TypeError if key is not an int or a string."""
        if not isinstance(key, (int, str)):
            raise TypeError(f"Key must be int or string, got {type(key).__name__}")

    def insert(self, key, value=None):
        """Insert key as a new leaf, or replace its value if the key already exists.

        Raises:
            TypeError: if key is not an int or a string.
        """
        self._validate_key(key)

        if self.root is None:
            self.root = TreeNode(key, value)
            self._size += 1
            return

        # walk down until the key is found or an empty spot appears for a new leaf
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
        """Return True if key is in the tree."""
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
        """Support `key in tree`."""
        return self.contains(key)

    def get(self, key):
        """Return the value stored for key.

        Raises:
            KeyError: if key is not in the tree.
        """
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
        """Support `tree[key]`."""
        return self.get(key)

    def inorder(self):
        """Return the keys in sorted order (left, node, right)."""
        result = []

        def _traverse(node):
            if node is not None:
                _traverse(node.left)
                result.append(node.key)
                _traverse(node.right)
        _traverse(self.root)
        return result

    def preorder(self):
        """Return the keys in preorder (node, left, right)."""
        result = []

        def _traverse(node):
            if node is not None:
                result.append(node.key)
                _traverse(node.left)
                _traverse(node.right)
        _traverse(self.root)
        return result

    def postorder(self):
        """Return the keys in postorder (left, right, node)."""
        result = []

        def _traverse(node):
            if node is not None:
                _traverse(node.left)
                _traverse(node.right)
                result.append(node.key)
        _traverse(self.root)
        return result

    def level_order(self):
        """Return the keys one level at a time, from the root down."""
        if self.root is None:
            return []

        result = []
        # temporary queue of nodes that are waiting to be visited
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
        """Return the (key, value) pair with the smallest key, or None if empty."""
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.key, current.value)

    def find_max(self):
        """Return the (key, value) pair with the largest key, or None if empty."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return (current.key, current.value)

    def min_key(self):
        """Return the smallest key.

        Raises:
            ValueError: if the tree is empty.
        """
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.find_min()[0]

    def max_key(self):
        """Return the largest key.

        Raises:
            ValueError: if the tree is empty.
        """
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.find_max()[0]

    def height(self):
        """Return the number of nodes on the longest root-to-leaf path (0 if empty)."""
        if self.root is None:
            return 0

        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def count_leaves(self):
        """Return the number of nodes that have no children."""
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
        """Return the sorted keys with min_key <= key <= max_key.

        Subtrees that cannot contain a match are skipped. Returns [] if min_key > max_key.
        """
        result = []

        def _range(node):
            if node is None:
                return
            # skip the left subtree when every key in it is too small
            if node.key > min_key:
                _range(node.left)
            if min_key <= node.key <= max_key:
                result.append(node.key)
            # skip the right subtree when every key in it is too large
            if node.key < max_key:
                _range(node.right)
        _range(self.root)
        return result

    def is_valid_bst(self):
        """Return True if every node stays within the bounds set by all its ancestors."""

        def _validate(node, low=None, high=None):
            if node is None:
                return True
            # every node must stay inside the bounds set by all of its ancestors
            if low is not None and node.key <= low:
                return False
            if high is not None and node.key >= high:
                return False
            return _validate(node.left, low, node.key) and _validate(node.right, node.key, high)
        return _validate(self.root)

    def delete(self, key):
        """Delete key from the tree.

        A node with two children is replaced by its inorder successor.

        Returns:
            True if the key was removed, False if it was not in the tree.
        """
        self._validate_key(key)
        deleted = False

        def _remove(node, key):
            nonlocal deleted
            if node is None:
                return None

            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                deleted = True
                # zero or one child: the node is simply replaced by that child
                if node.left is None:
                    self._size -= 1
                    return node.right
                elif node.right is None:
                    self._size -= 1
                    return node.left

                # two children: use the inorder successor (smallest key in the right subtree)
                successor = node.right
                while successor.left is not None:
                    successor = successor.left

                node.key = successor.key
                node.value = successor.value
                # remove the successor's old node; its right child gets reattached
                node.right = _remove(node.right, successor.key)

            return node

        self.root = _remove(self.root, key)
        return deleted