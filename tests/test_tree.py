import unittest

from typedtree.node import Node
from typedtree.traversalmode import TraversalMode
from typedtree.tree import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()

    def test_add_node(self):
        node = self.tree.add_node("root")
        self.assertEqual(node.identifier, "root")
        self.assertIn("root", self.tree.nodes)

    def test_add_node_with_parent(self):
        self.tree.add_node("root")
        node = self.tree.add_node("child", parent_pointer="root")
        self.assertEqual(node.identifier, "child")
        self.assertIn("child", self.tree.nodes)
        self.assertEqual(self.tree["child"].parent.pointer, "root")

    def test_get_siblings(self):
        self.tree.add_node("root")
        self.tree.add_node("child1", parent_pointer="root")
        self.tree.add_node("child2", parent_pointer="root")
        siblings = self.tree.get_siblings("child1")
        self.assertEqual(len(siblings), 2)
        self.assertIn(self.tree["child2"], siblings)

    def test_display(self):
        self.tree.add_node("root")
        self.tree.add_node("child", parent_pointer="root")
        # This test just ensures that the display method runs without error
        self.tree.display("root")

    def test_traverse_depth(self):
        self.tree.add_node("root")
        self.tree.add_node("child1", parent_pointer="root")
        self.tree.add_node("child2", parent_pointer="root")
        nodes = list(self.tree.traverse("root", mode=TraversalMode.DEPTH))
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].identifier, "root")
        self.assertEqual(nodes[1].identifier, "child1")
        self.assertEqual(nodes[2].identifier, "child2")

    def test_traverse_breadth(self):
        self.tree.add_node("root")
        self.tree.add_node("child1", parent_pointer="root")
        self.tree.add_node("child2", parent_pointer="root")
        nodes = list(self.tree.traverse("root", mode=TraversalMode.BREADTH))
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].identifier, "root")
        self.assertEqual(nodes[1].identifier, "child1")
        self.assertEqual(nodes[2].identifier, "child2")

    def test_len(self):
        self.tree.add_node("root")
        self.tree.add_node("child", parent_pointer="root")
        self.assertEqual(len(self.tree), 2)


if __name__ == "__main__":
    unittest.main()
