import unittest
import htmlnode

class TestParentNode(unittest.TestCase):

    def test_init(self):
        child1 = htmlnode.LeafNode("span", "Hello World")
        grandchild1 = htmlnode.LeafNode("p", "grandchild")
        child_father = htmlnode.ParentNode("div", [grandchild1])
        test_node = htmlnode.ParentNode("div", [child1, child_father])
        self.assertEqual(test_node.tag, "div")
        self.assertEqual(test_node.value, None)
        self.assertEqual(test_node.children, [child1, child_father])
        self.assertEqual(test_node.props, None)

    def test_props_to_html(self):
        child1 = htmlnode.LeafNode("span", "Hello World")
        test_node = htmlnode.ParentNode("div", [child1],{'name': 'test_div','attr':'test'})
        self.assertEqual(test_node.props_to_html(), 'name=\"test_div\" attr=\"test\"')

    def test_tag_error(self):
        child1 = htmlnode.LeafNode("span", "Hello World")
        test_node = htmlnode.ParentNode(None, [child1],{'name': 'test_div','attr':'test'})
        error = None
        try: 
            test_node.to_html()
        except Exception as e:
            error = e
        self.assertEqual(str(error), "All parent nodes must have a tag")

    def test_child(self):
        test_node = htmlnode.ParentNode("div", None, {'name': 'test_div','attr':'test'})
        error = None
        try: 
            test_node.to_html()
        except Exception as e:
            error = e
        self.assertEqual(str(error), "All parent nodes must have children")

if __name__ == "__main__":
    unittest.main()
