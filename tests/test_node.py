from pathfinder.node import Node

class TestNode:
    def test_node_label(self):
        node = Node("A", 5)
        assert node.label == "A"
