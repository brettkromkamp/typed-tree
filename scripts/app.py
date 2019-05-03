"""
app.py script (for functional testing purposes).

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typedtree.traversalconstant import TraversalConstant
from typedtree.tree import Tree

tree = Tree()

# A node without a parent pointer is by definition the root node
tree.add_node('Harry', node_type='male')

tree.add_node('Jane', parent_pointer='Harry', node_type='female', edge_type='daughter')
tree.add_node('Bill', parent_pointer='Harry', node_type='male', edge_type='son')
tree.add_node('Joe', parent_pointer='Jane', node_type='male', edge_type='son')
tree.add_node('Diane', parent_pointer='Jane', node_type='female', edge_type='friend')
tree.add_node('George', parent_pointer='Diane', node_type='male', edge_type='colleague')
tree.add_node('Mary', parent_pointer='Diane', node_type='female', edge_type='friend')
tree.add_node('Jill', parent_pointer='George')
tree.add_node('Carol', parent_pointer='Jill', node_type='female', edge_type='friend')
tree.add_node('Grace', parent_pointer='Bill', node_type='female')
tree.add_node('Mark', parent_pointer='Jane', edge_type='brother')

print('***** TREE STRUCTURE *****')
tree.display('Harry')

print('***** DEPTH-FIRST ITERATION *****')
for identifier in tree.traverse('Harry'):
    node = tree[identifier]
    print(f"{node.identifier} [{node.type or '*Undefined*'}]")

print('***** BREADTH-FIRST ITERATION *****')
for identifier in tree.traverse('Harry', mode=TraversalConstant.BREADTH):
    node = tree[identifier]
    print(f"{node.identifier} [{node.type or '*Undefined*'}]")
