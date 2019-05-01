"""
TreeConstant enumeration.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from tree.tree import Tree
from tree.treeconstant import TreeConstant


tree = Tree()

tree.add_node("Harry")  # root node
tree.add_node("Jane", "Harry")
tree.add_node("Bill", "Harry")
tree.add_node("Joe", "Jane")
tree.add_node("Diane", "Jane")
tree.add_node("George", "Diane")
tree.add_node("Mary", "Diane")
tree.add_node("Jill", "George")
tree.add_node("Carol", "Jill")
tree.add_node("Grace", "Bill")
tree.add_node("Mark", "Jane")

tree.display("Harry")
print("***** DEPTH-FIRST ITERATION *****")
for node in tree.traverse("Harry"):
    print(node)

print("***** BREADTH-FIRST ITERATION *****")
for node in tree.traverse("Harry", mode=TreeConstant.BREADTH):
    print(node)
