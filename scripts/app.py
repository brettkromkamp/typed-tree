"""
app.py script (for functional testing purposes).

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typedtree.traversalmode import TraversalMode
from typedtree.tree import Tree

tree = Tree()

# A node without a parent pointer is by definition the root node
tree.add_node("Elon Musk", node_type="person")

tree.add_node("Lyndon Rive", parent_pointer="Elon Musk", node_type="person", edge_type="family")
tree.add_node("SpaceX", parent_pointer="Elon Musk", node_type="company", edge_type="founder")
tree.add_node("Tesla", parent_pointer="Elon Musk", node_type="company", edge_type="founder")
tree.add_node(
    "Solar City",
    parent_pointer="Lyndon Rive",
    node_type="company",
    edge_type="co-founder",
)
tree.add_node(
    "Solar Energy Services",
    parent_pointer="Solar City",
    node_type="product",
    edge_type="service",
)
tree.add_node("Falcon 9", parent_pointer="SpaceX", node_type="rocket", edge_type="technology")
tree.add_node("Falcon Heavy", parent_pointer="SpaceX", node_type="rocket", edge_type="technology")
tree.add_node("Dragon", parent_pointer="SpaceX", node_type="space-ship", edge_type="technology")
tree.add_node("Model S", parent_pointer="Tesla", node_type="car", edge_type="product")
tree.add_node("Model X", parent_pointer="Tesla", node_type="car", edge_type="product")
tree.add_node("Model Y", parent_pointer="Tesla", node_type="car", edge_type="product")
tree.add_node("Roadster", parent_pointer="Tesla", node_type="car", edge_type="product")

print("\n***** TREE STRUCTURE *****")
tree.display("Elon Musk")

print("\n***** DEPTH-FIRST ITERATION *****")
for node in tree.traverse("Elon Musk"):
    print(f"{node.identifier} [{node.type or '*Undefined*'}]")

print("\n***** BREADTH-FIRST ITERATION *****")
for node in tree.traverse("Elon Musk", mode=TraversalMode.BREADTH):
    print(f"{node.identifier} [{node.type or '*Undefined*'}]")
