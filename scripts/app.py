"""
TreeConstant enumeration.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typedtree.tree import Tree
from typedtree.treeconstant import TreeConstant


tree = Tree()

tree.add_node('Harry', node_type='male')  # root node
tree.add_node('Jane', parent='Harry', node_type='female')
tree.add_node('Bill', parent='Harry', node_type='male')
tree.add_node('Joe', parent='Jane', node_type='male')
tree.add_node('Diane', parent='Jane', node_type='female')
tree.add_node('George', parent='Diane', node_type='male')
tree.add_node('Mary', parent='Diane', node_type='female')
tree.add_node('Jill', parent='George', node_type='female')
tree.add_node('Carol', parent='Jill', node_type='female')
tree.add_node('Grace', parent='Bill', node_type='female')
tree.add_node('Mark', parent='Jane', node_type='male')

tree.display('Harry')
print('***** DEPTH-FIRST ITERATION *****')
for identifier in tree.traverse('Harry'):
    print(identifier)

print('***** BREADTH-FIRST ITERATION *****')
for node in tree.traverse('Harry', mode=TreeConstant.BREADTH):
    print(node)
