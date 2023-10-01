class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is None:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_node = self.find_min(root.right)
            root.key = min_node.key
            root.right = self.delete(root.right, min_node.key)

        self.update_height(root)

        balance = self.balance_factor(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search_key(self, key):
        return self.search(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def display(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:
                self.display(node.left, level + 1, "L-- ")
                self.display(node.right, level + 1, "R-- ")

def main():
    avl_tree = AVLTree()

    avl_tree.root = avl_tree.insert(avl_tree.root, 10)
    avl_tree.root = avl_tree.insert(avl_tree.root, 20)
    avl_tree.root = avl_tree.insert(avl_tree.root, 30)
    avl_tree.root = avl_tree.insert(avl_tree.root, 40)
    avl_tree.root = avl_tree.insert(avl_tree.root, 50)
    avl_tree.root = avl_tree.insert(avl_tree.root, 25)

    print("Initial AVL Tree:")
    avl_tree.display(avl_tree.root)

    key_to_search = 30
    search_result = avl_tree.search_key(key_to_search)

    if search_result:
        print(f"Node with key {key_to_search} found in the tree.")
    else:
        print(f"Node with key {key_to_search} not found in the tree.")

    key_to_delete = 30
    avl_tree.root = avl_tree.delete_key(key_to_delete)
    print(f"Deleted node with key {key_to_delete}.")

    print("\nAVL Tree after deletion:")
    avl_tree.display(avl_tree.root)

if __name__ == "__main__":
    main()
