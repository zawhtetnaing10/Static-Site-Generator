from textnode import TextNode
from textnode import TextType
from extract_mark_down_elements import extract_mark_down_images
from extract_mark_down_elements import extract_mark_down_links
import re

FULL_IMAGES_REGEX = r"!\[[^\]]*\]\(https?:\/\/[\w.-]+(?:\/[\w\-.%]+)*\.(?:jpg|jpeg|png|gif|webp|bmp|svg)\)"
FULL_LINKS_REGEX = r"\[[^\]]+\]\(\s*(?:https?:\/\/[^\s)]+|\/[\w\-.%?=&#@]+|\.\.?\/[\w\-.%?=&#@]*|[\w\-.%?=&#@]+\/[\w\-.%?=&#@]*)\s*\)"


def split_nodes_images(old_nodes):
    return split_nodes_element(old_nodes, FULL_IMAGES_REGEX)


def split_nodes_link(old_nodes):
    return split_nodes_element(old_nodes, FULL_LINKS_REGEX)


def split_nodes_element(old_nodes, regex):
    result = old_nodes
    while (find_first_index_with_element_regex(result, regex) != None):
        # find the text with delimiter
        index_with_element = find_first_index_with_element_regex(
            result, regex)
        text_to_process = result[index_with_element].text

        # find image elements
        index_of_regex = re.search(regex, text_to_process).start()
        matching_text = re.findall(regex, text_to_process)[
            0]  # Get the first matching element

        elements = None
        if regex == FULL_IMAGES_REGEX:
            elements = extract_mark_down_images(matching_text)
        else:
            elements = extract_mark_down_links(matching_text)
        if not elements:
            raise Exception("invalid element")
        alt_text, url = elements[0]

        # find before and after text
        before_text = text_to_process[0:index_of_regex]
        after_text = text_to_process[index_of_regex +
                                     len(matching_text): len(text_to_process)]

        # create nodes
        first_text_node = TextNode(text=before_text, text_type=TextType.TEXT)

        element_node = None
        if regex == FULL_IMAGES_REGEX:
            element_node = TextNode(
                text=alt_text, text_type=TextType.IMAGES, url=url)
        else:
            element_node = TextNode(
                text=alt_text, text_type=TextType.LINK, url=url)

        second_text_node = TextNode(text=after_text, text_type=TextType.TEXT)
        new_text_nodes = [first_text_node, element_node, second_text_node]
        filterd_not_empty = list(
            filter(lambda x: len(x.text) > 0, new_text_nodes))

        # replace the original node with new nodes
        result[index_with_element:index_with_element+1] = filterd_not_empty

    return result


def find_first_index_with_element_regex(nodes, element_regex):
    index = None
    for i in range(0, len(nodes)):
        if re.search(element_regex, nodes[i].text) != None:
            return i
    return index
