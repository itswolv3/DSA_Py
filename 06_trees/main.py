from tree import BinarySearchTree

my_bst = BinarySearchTree()
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)

print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)

print(my_bst.contains(2))
