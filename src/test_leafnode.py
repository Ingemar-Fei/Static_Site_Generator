import unittest
import htmlnode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html(self):
        node = htmlnode.LeafNode("p", "Hello, world!", {'id':"test"})
        self.assertEqual(node.to_html(), '<p id="test">Hello, world!</p>')

    def test_leaf_to_html_value(self):
        node = htmlnode.LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_tag(self):
        node = htmlnode.LeafNode("a",None, {"href": "https://www.google.com"})
        val_error = None
        try:
            node.to_html()
        except ValueError as e:
            val_error = e
        finally:
            self.assertEqual(val_error.__str__(),'All leaf nodes must have a value')
if __name__ == "__main__":
    unittest.main()
