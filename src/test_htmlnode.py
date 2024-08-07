import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class testhmtlnode(unittest.TestCase):
    def testhtml(self):
        html1 = HTMLNode("1","2","3",{"4","5","6"})
        html2 = HTMLNode("5","6","7","8")
        print(html1.props_to_html())
    def testhtml2(self):
        html3= HTMLNode(None,None,None,{"test", "props","oder so"})
        print(html3.props_to_html())
    def testhtmml3(self):
        html4=HTMLNode(None,None,None,{"test", "props","oder so"})
        html2 = HTMLNode("5","6","7","8")
        html3 = HTMLNode("5","6","7","8")
        print(html2.__repr__())
class testleafnode(unittest.TestCase):
    def testlead1(self):
        leaf1=LeafNode("a","wert",None,{"link"})
        print(leaf1.to_html())
if __name__ == "__main__":
    unittest.main()