import enum

class TextType(enum.Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, another_node):
        if self.text_type == another_node.text_type and \
        self.text == another_node.text and \
        self.url == another_node.url :
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        
