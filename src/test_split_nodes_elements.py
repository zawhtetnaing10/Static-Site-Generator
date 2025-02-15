import unittest
from textnode import TextNode
from textnode import TextType
from split_nodes_elements import split_nodes_link
from split_nodes_elements import split_nodes_images


class TestSplitNodeElements(unittest.TestCase):
    def test_image_nodes_one_image(self):
        input = [TextNode(
            text="There's only one image. The image is ![the only image](https://www.bootdev.com/434343.jpeg)", text_type=TextType.TEXT
        )]
        correct_output = [
            TextNode("There's only one image. The image is ",
                     text_type=TextType.TEXT),
            TextNode(text="the only image", text_type=TextType.IMAGES,
                     url="https://www.bootdev.com/434343.jpeg")
        ]
        self.assertListEqual(split_nodes_images(input), correct_output)

    def test_image_nodes_two_images(self):
        input = [TextNode(
            text="There are two images. First image is ![first image](https://www.i.imagur.com/4343.png). The second one is ![second image](https://www.youtube.com/454454.gif)", text_type=TextType.TEXT)]
        correct_output = [
            TextNode("There are two images. First image is ",
                     text_type=TextType.TEXT),
            TextNode(text="first image", text_type=TextType.IMAGES,
                     url="https://www.i.imagur.com/4343.png"),
            TextNode(text=". The second one is ", text_type=TextType.TEXT),
            TextNode(text="second image", text_type=TextType.IMAGES,
                     url="https://www.youtube.com/454454.gif")
        ]
        self.assertListEqual(split_nodes_images(input), correct_output)

    def test_multiple_nodes_with_images(self):
        input = [
            TextNode(
                "There are two images. First image is ![first image](https://www.i.imagur.com/4343.png). The second one is ![second image](https://www.youtube.com/454454.gif)", text_type=TextType.TEXT),
            TextNode(
                "There's a third image apprantly. It is ![third image](https://www.youtube.com/345323.png)", text_type=TextType.TEXT)
        ]
        correct_output = [
            TextNode("There are two images. First image is ",
                     text_type=TextType.TEXT),
            TextNode(text="first image", text_type=TextType.IMAGES,
                     url="https://www.i.imagur.com/4343.png"),
            TextNode(text=". The second one is ", text_type=TextType.TEXT),
            TextNode(text="second image", text_type=TextType.IMAGES,
                     url="https://www.youtube.com/454454.gif"),
            TextNode(text="There's a third image apprantly. It is ",
                     text_type=TextType.TEXT),
            TextNode(text="third image", text_type=TextType.IMAGES,
                     url="https://www.youtube.com/345323.png")
        ]
        self.assertListEqual(split_nodes_images(input), correct_output)

    def test_link_nodes_two_links(self):
        input = [TextNode(
            text="This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT)]
        correct_output = [
            TextNode("This is text with a link ", text_type=TextType.TEXT),
            TextNode(text="to boot dev", text_type=TextType.LINK,
                     url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="to youtube", text_type=TextType.LINK,
                     url="https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(split_nodes_link(input), correct_output)

    def test_link_nodes_one_link(self):
        input = [TextNode(
            text="There's only one link. It is [to google](https://www.google.com)", text_type=TextType.TEXT
        )]
        correct_output = [
            TextNode("There's only one link. It is ", text_type=TextType.TEXT),
            TextNode("to google", text_type=TextType.LINK,
                     url="https://www.google.com")
        ]
        self.assertListEqual(split_nodes_link(input), correct_output)

    def test_multiple_nodes_with_links(self):
        input = [TextNode(
            text="This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT),
            TextNode(
                text="There's a third link. [to facebook](https://www.facebook.com)", text_type=TextType.TEXT),
            TextNode(text="final link", text_type=TextType.LINK,
                     url="https://www.finallink.com")
        ]
        correct_output = [
            TextNode("This is text with a link ", text_type=TextType.TEXT),
            TextNode(text="to boot dev", text_type=TextType.LINK,
                     url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="to youtube", text_type=TextType.LINK,
                     url="https://www.youtube.com/@bootdotdev"),
            TextNode("There's a third link. ", text_type=TextType.TEXT),
            TextNode("to facebook", text_type=TextType.LINK,
                     url="https://www.facebook.com"),
            TextNode(text="final link", text_type=TextType.LINK,
                     url="https://www.finallink.com")
        ]
        self.assertListEqual(split_nodes_link(input), correct_output)
