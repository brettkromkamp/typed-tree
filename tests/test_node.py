import unittest

from typedtree.node import Edge, Node


class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        node = Node(identifier="root")
        self.assertEqual(node.identifier, "root")
        self.assertIsNone(node.payload)
        self.assertEqual(node.children, [])

    def test_node_with_payload(self):
        node = Node(identifier="root", payload={"key": "value"})
        self.assertEqual(node.payload, {"key": "value"})

    def test_node_add_child(self):
        parent_node = Node(identifier="parent")
        child_node = Node(identifier="child")
        edge = Edge(pointer=child_node, type="child")
        parent_node.add_child(edge)
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0], edge)

    def test_node_payload_setter(self):
        node = Node(identifier="root")
        node.payload = {"new_key": "new_value"}
        self.assertEqual(node.payload, {"new_key": "new_value"})

    def test_node_with_parent(self):
        parent_node = Node(identifier="parent")
        edge = Edge(pointer=parent_node, type="parent")
        child_node = Node(identifier="child", parent=edge)
        self.assertEqual(child_node.parent, edge)


if __name__ == "__main__":
    unittest.main()
