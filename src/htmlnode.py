class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self. children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_html = ""
        for item in self.props:
            props_html = props_html+" "+item
        return props_html
    
    def __repr__(self) -> str:
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        html_string =""
        if self.value==None:
            raise ValueError
        if self.tag==None:
            return self.value
        html_string= "<"+self.tag+">"+self.props_to_html()+" <"+self.tag+">"
        return html_string