import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_init(self):
        test_text = "Text Node for init func"
        test_type = TextType.TEXT
        test_url = None
        node = TextNode(test_text,test_type)
        self.assertEqual(
                (node.text, node.text_type, node.url),
                (test_text, test_type, test_url)
                )

    def test_types(self):
        test_text = "Text Node for distinguish types"
        test_type1 = TextType.ITALIC
        test_type2 = TextType.BOLD
        node1 = TextNode(test_text,test_type1)
        node2 = TextNode(test_text,test_type2)
        self.assertNotEqual(
                node1,
                node2
                )
        
    def test_text_node_to_html_node_Normal(self):
        test_text = "Text Node"
        test_type = TextType.TEXT
        test_url = None
        node = TextNode(test_text,test_type)
        html_node = text_node_to_html_node(node)
        self.assertEqual(
                html_node.tag,
                None
        )
    
    def test_text_node_to_html_node_Bold(self):
        node = TextNode("This is a text node", TextType.LINKS, 'www.bilibili.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {'href':  'www.bilibili.com'})

if __name__ == "__main__":
    unittest.main()
