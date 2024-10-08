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
        if self.props==None or self.props=="":
            return ""
        props_html = ''.join(f" {key}=\"{value}\"" for key, value in self.props.items())
        return props_html
    
    def __repr__(self) -> str:
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)

    def to_html(self):
        
        if self.value==None:
            raise ValueError("Invalid HTML: no value")
        if self.tag==None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag==None:
            raise ValueError("Invalid HTML: no tag")
        if self.children==None:
            raise ValueError("Invalid HTML: no children")
        child_string = ""
        for child in self.children:
            child_string += child.to_html()
            #child_string += f"{child.to_html()}"
        return f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"
    
