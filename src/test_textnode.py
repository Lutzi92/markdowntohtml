import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node3= TextNode("test3","type3")
        node4 = TextNode("test3","type3")
        self.assertAlmostEqual(node3,node4)
    def test_noeq(self):
        node5 = TextNode("test1", "type1")
        node6 = TextNode("test1", "type2")
        self.assertNotEqual(node5,node6)                
    def test_noeq2(self):
        node5 = TextNode("test1", "type1")
        node6 = TextNode("test2", "type1")
        self.assertNotEqual(node5,node6)          
    def test_noeq3(self):
        node5 = TextNode("test1", "type1","url1")
        node6 = TextNode("test1", "type1")
        self.assertNotEqual(node5,node6)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", "image", "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()