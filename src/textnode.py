from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TextNode():

    def __init__(self, text, text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, compare) -> bool:
        return ((self.text==compare.text) and (self.text_type==compare.text_type) and (self.url==compare.url))
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def main():
    test = TextNode("tewext","text_type","url")
    print(test.__repr__())
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None,text_node.text,)
        case "bold":
            return LeafNode("b",text_node.text,)
        case "italic":
            return LeafNode("i", text_node.text,)
        case "code":
            return LeafNode("code",text_node.text,)
        case "link":
            return LeafNode("a",text_node.value, {"href":text_node.url})
        case "img":
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Falsch")

main()