"""
TreeConstant enumeration.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typedtree.tree import Tree
from typedtree.treeconstant import TreeConstant


tree = Tree()

tree.add_node('Harry', node_type='male')  # root node
tree.add_node('Jane', parent_pointer='Harry', node_type='female', edge_type='daughter')
tree.add_node('Bill', parent_pointer='Harry', node_type='male', edge_type='son')
tree.add_node('Joe', parent_pointer='Jane', node_type='male', edge_type='son')
tree.add_node('Diane', parent_pointer='Jane', node_type='female', edge_type='friend')
tree.add_node('George', parent_pointer='Diane', node_type='male', edge_type='colleague')
tree.add_node('Mary', parent_pointer='Diane', node_type='female', edge_type='friend')
tree.add_node('Jill', parent_pointer='George', node_type='female', edge_type='wife')
tree.add_node('Carol', parent_pointer='Jill', node_type='female', edge_type='friend')
tree.add_node('Grace', parent_pointer='Bill', node_type='female', edge_type='sister')
tree.add_node('Mark', parent_pointer='Jane', node_type='male', edge_type='brother')

tree.display('Harry')
print('***** DEPTH-FIRST ITERATION *****')
for identifier in tree.traverse('Harry'):
    print(identifier)

print('***** BREADTH-FIRST ITERATION *****')
for node in tree.traverse('Harry', mode=TreeConstant.BREADTH):
    print(node)
