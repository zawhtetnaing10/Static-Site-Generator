from enum import Enum


class TextType(Enum):
    NORMAL_TEXT = "Normal Text"
    BOLD_TEXT = "Bold Text"
    ITALIC_TEXT = "Italic Text"
    CODE = "Code"
    LINK = "Link"
    IMAGES = "Images"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.tex_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
