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
        return f'<{self.tag} {self.props_to_html()}>{self.value}{self.children if self.children else ''}</{self.tag}>'