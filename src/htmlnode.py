class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise  NotImplementedError
    
    def props_to_html(self):
        return ' '.join(list(map(lambda x,y: f'{x}="{y}"', self.props.keys(), self.props.values())))

    def __repr__(self):
        return f'tag:{self.tag}\nvalue:{self.value}\nchildren:{self.children}\nprops:{self.props}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('All leaf nodes must have a value')
        else:
            prefix = f'<{self.tag}{f" {self.props_to_html()}"if self.props else ''}>' if self.tag else ''
            suffix = f'</{self.tag}>' if self.tag else ''
            return prefix + self.value + suffix 

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError('All parent nodes must have a tag')
        elif not  self.children:
            raise ValueError('All parent nodes must have children')
        else:
            prefix = f'<{self.tag}{f" {self.props_to_html()}"if self.props else ''}>' if self.tag else ''
            suffix = f'</{self.tag}>' if self.tag else ''
            return prefix + { child.to_html() for child in self.children} + suffix
        