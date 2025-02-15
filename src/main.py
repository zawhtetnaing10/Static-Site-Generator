from textnode import TextNode
from textnode import TextType
from split_nodes_delimiter import split_nodes_delimiter
from extract_mark_down_elements import extract_mark_down_images
from extract_mark_down_elements import extract_mark_down_links


def main():
    text = "This is an ![invalid image](https://www.invalid.com/aksjdfakf.txt)"
    result = extract_mark_down_images(text=text)

    print(result)


main()
