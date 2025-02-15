from textnode import TextNode
from textnode import TextType
from split_nodes_delimiter import split_nodes_delimiter
from extract_mark_down_elements import extract_mark_down_images
from extract_mark_down_elements import extract_mark_down_links
from split_nodes_elements import split_nodes_element
from split_nodes_elements import split_nodes_images
from split_nodes_elements import split_nodes_link
from split_nodes_elements import FULL_IMAGES_REGEX
from split_nodes_elements import FULL_LINKS_REGEX
import re


def main():
    # text = "There are two images. First image is ![first image](https://www.i.imagur.com/4343.png). The second one is ![second image](https://www.youtube.com/454454.gif)"
    # text_node = TextNode(text=text, text_type=TextType.TEXT)
    # input = [text_node]

    # result = "\n".join(
    #     list(map(lambda x: f"{x}", split_nodes_element(input, FULL_IMAGES_REGEX))))
    # print(f"Result =====> {result}")

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    text_node = TextNode(text=text, text_type=TextType.TEXT)
    input = [text_node]

    result = "\n".join(
        list(map(lambda x: f"{x}", split_nodes_link(input))))
    print(f"Result =====> {result}")


main()
