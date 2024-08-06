import unittest

from textnode import TextNode


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
if __name__ == "__main__":
    unittest.main()