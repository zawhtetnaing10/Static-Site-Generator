class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return None

        result = ""
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
