from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, props=None, tag=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")

        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
