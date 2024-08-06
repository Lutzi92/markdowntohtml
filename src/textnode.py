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

main()