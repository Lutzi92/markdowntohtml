import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class testhmtlnode(unittest.TestCase):
    def testhtml(self):
        html1 = HTMLNode("1","2","3",{"4":"5","5":"6"})
        html2 = HTMLNode("5","6","7","8")
        print(html1.props_to_html())
    def testhtml2(self):
        html3= HTMLNode(None,None,None,{"test":"props","test2": "oder so"})
        print(html3.props_to_html())
    def testhtmml3(self):
        html4=HTMLNode(None,None,None,{"test", "props","oder so"})
        html2 = HTMLNode("5","6","7","8")
        html3 = HTMLNode("5","6","7","8")
        print(html2.__repr__())
class testleafnode(unittest.TestCase):
    
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        #self.assertEqual(
            #node.__repr__(),
            #"#HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        #)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

class testParentnode(unittest.TestCase):
    def testparent1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )   
        node.to_html()
        print(node.to_html())
    def testparent1(self):
        node = ParentNode("p",[ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)   
        node.to_html()
        print(node.to_html())
if __name__ == "__main__":
    unittest.main()