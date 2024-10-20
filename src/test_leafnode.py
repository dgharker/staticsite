import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_test(self):
        node = LeafNode(None,"This is Text",None)
        result = node.to_html()
        expected ="<p>This is Text</p>"
        self.assertEqual(result,expected)

    def test_bold(self):
        node = LeafNode("b","This is bold",None)
        result = node.to_html()
        expected ="<b>This is bold</b>"
        self.assertEqual(result,expected)

    def test_italic(self):
        node = LeafNode("i","This is italic",None)
        result = node.to_html()
        expected ="<i>This is italic</i>"
        self.assertEqual(result,expected)
    
    def test_code(self):
        node = LeafNode("code","This is code",None)
        result = node.to_html()
        expected ="<code>This is code</code>"
        self.assertEqual(result,expected)

    def test_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected ="""<a href="https://www.google.com">Click me!</a>"""
        self.assertEqual(result,expected)        

    def test_img(self):
        node = LeafNode("img","This is alt",{"src": "/img.jpg"})
        result = node.to_html()
        expected ="""<img src="/img.jpg" alt="This is alt"/>"""
        self.assertEqual(result,expected)

    def test_value_none(self):
        node = LeafNode(None,None,None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_img_no_src(self):
        node = LeafNode("img","This is alt",{"srr": "/img.jpg"})
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_link_no_href(self):
        node = LeafNode("a", "Click me!", None)
        with self.assertRaises(ValueError):
            node.to_html()      
