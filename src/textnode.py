import enum
import htmlnode

class TextType(enum.Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, another_node):
        if self.text_type.value == another_node.text_type.value and \
        self.text == another_node.text and \
        self.url == another_node.url :
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    match  text_node.text_type:
        case TextType.TEXT:
            return htmlnode.LeafNode(None, text_node.text)
        case TextType.BOLD:
            return htmlnode.LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return htmlnode.LeafNode("i", text_node.text)
        case TextType.CODE:
            return htmlnode.LeafNode("code", text_node.text)
        case TextType.LINKS:
            return htmlnode.LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGES:
            return htmlnode.LeafNode("img", "", props={"src": text_node.url,"alt": text_node.text})
        case _:
            raise ValueError("Invalid TextType")
