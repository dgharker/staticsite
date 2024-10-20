from htmlnode import HTMLNode

#class TextType(Enum):
#    TEXT = "text"
#    BOLD = "bold"
#    ITALIC = "italic"
#    CODE = "code"
#    LINK = "link"
#    IMAGE = "image"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.render_text()
        
        match self.tag:
            case "a":
                if self.props is None:
                    raise ValueError("Link must have an 'href' property set")
                if 'href' not in self.props:
                    raise ValueError("Link must have an 'href' property set")
                return self.render_link()
            case "i":
                return self.render_italic()
            case "b":
                return self.render_bold()
            case "code":
                return self.render_code()
            case "img":
               if self.props is None:
                    raise ValueError("Image must have a 'src' property set")
               if "src" not in self.props:
                    raise ValueError("Image must have a 'src' property set")
               return self.render_image()
            case _:
                raise ValueError(f"Unknown Tag: {self.tag}")


    def render_text(self):
        return f"<p>{self.value}</p>"

    def render_bold(self):
        return f"<b>{self.value}</b>"

    def render_italic(self):
        return f"<i>{self.value}</i>"

    def render_code(self):
        return f"<code>{self.value}</code>"

    def render_link(self):
        return f"<a href=\"{self.props['href']}\">{self.value}</a>"

    def render_image(self):
        src = self.props["src"]
        return f"<img src=\"{src}\" alt=\"{self.value}\"/>"
    
    
