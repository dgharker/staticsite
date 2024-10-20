import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_textrep(self):
        props = {}
        props["a"] = "bcde"
        props["b"] = "edcb"
        node = HTMLNode("<b>","This is bold text",None, props)
        text = str(node)
        test_text = """(
        tag: <b>,
        value: This is bold text,
        children: None,
        props:  a="bcde" b="edcb",
        )
        """
        self.assertEqual(text,test_text)
        




if __name__ == "__main__":
    unittest.main()
