import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_init(self):
        test_text = "Text Node for init func"
        test_type = (TextType.NORMAL,"normal")
        test_url = None
        node = TextNode(test_text,test_type[0])
        self.assertEqual(
                (node.text, node.text_type, node.url),
                (test_text, test_type[1], test_url)
                )

    def test_types(self):
        test_text = "Text Node for distinguish types"
        test_type1 = (TextType.NORMAL,"normal")
        test_type2 = (TextType.BOLD,"bold")
        test_url = None
        node1 = TextNode(test_text,test_type1[0])
        node2 = TextNode(test_text,test_type2[0])
        self.assertNotEqual(
                node1,
                node2
                )
        
if __name__ == "__main__":
    unittest.main()
