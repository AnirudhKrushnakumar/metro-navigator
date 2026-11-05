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

    def get(self, key, default=None):
        self._validate_key(key)
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        if default is not None:
            return default
        raise KeyError(f"Key not found: {key}")

    def __getitem__(self, key):
        return self.get(key)