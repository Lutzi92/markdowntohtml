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
from split_delimiter import split_nodes_delimiter

class test_delimiter(unittest.TestCase):
    def testcase1(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        print(new_nodes)
    def testcase2(self):
        node = TextNode("This is text with a *italic block* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        print(new_nodes)
    def testcase3(self):
        node = TextNode("This is text with a **bold block** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        print(new_nodes)