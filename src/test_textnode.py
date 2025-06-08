import unittest
from textnode import TextNode, TextType
import textnode



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
        html_node = textnode.text_node_to_html_node(node)
        self.assertEqual(
                html_node.tag,
                None
        )
    
    def test_text_node_to_html_node_Bold(self):
        node = TextNode("This is a text node", TextType.LINK, 'www.bilibili.com')
        html_node = textnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {'href':  'www.bilibili.com'})

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = textnode.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
                new_nodes[0],
                TextNode("This is text with a ", TextType.TEXT)
        )
        self.assertEqual(
                new_nodes[1],
                TextNode("code block", TextType.CODE)
        )
        self.assertEqual(
                new_nodes[2],
                TextNode(" word", TextType.TEXT)
        )

    def test_images_from_text(self):
        test_set = [{
            'text':"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            'res':[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        },{
            "text":"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            "res":[("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        },{
            "text":"This is text with a ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "res":[('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        }]
        for test in test_set:
            self.assertEqual(textnode.extract_markdown_images(test["text"]), test["res"])

    def test_extract_markdown_links(self):
        test_set = [{
        "text":"This is text with a [rick roll](https://www.youtube.com/watch?v=dQw4w9WgXcQ) and [obi wan](https://www.youtube.com/watch?v=8YjFbEfU4S4)",
        "res":[("rick roll", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"), ('obi wan', 'https://www.youtube.com/watch?v=8YjFbEfU4S4')]
        }]
        for test in test_set:
            self.assertEqual(textnode.extract_markdown_links(test["text"]), test["res"])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = textnode.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

        
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = textnode.split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ],
            new_nodes,
        )

        
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = textnode.text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
            nodes,
        )

if __name__ == "__main__":
    unittest.main()

    