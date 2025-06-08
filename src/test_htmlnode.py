import unittest
import htmlnode

class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = htmlnode.HTMLNode("div", "Hello World")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = htmlnode.HTMLNode("div", "Hello World", None, {'name': "test_div", 'attr': "test"})
        self.assertEqual(node.props_to_html(), 'name=\"test_div\" attr=\"test\"')

    def test_repr(self):
        node = htmlnode.HTMLNode("div", "Hello World", None, {'attr': "test_div"})
        self.assertEqual(node.__repr__(), '<div attr="test_div">Hello World</div>')

if __name__ == "__main__":
    unittest.main()
