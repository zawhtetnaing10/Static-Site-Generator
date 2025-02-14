from textnode import TextNode
from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = old_nodes

    while (find_first_index_with_delimiter(result, delimiter) != -1):
        # find the text with delimiter
        index_with_delimiter = find_first_index_with_delimiter(
            result, delimiter)
        text_to_process = result[index_with_delimiter].text

        # find indices for delimiter
        first_index = text_to_process.find(delimiter)
        second_index = text_to_process.find(
            delimiter, first_index + len(delimiter))
        if second_index == -1:
            raise Exception("No matching end delimiter found")

        # slice the text into three using the delimiter
        text_with_delimiter = text_to_process[first_index +
                                              len(delimiter):second_index]
        other_text_1 = text_to_process[0:first_index]
        other_text_2 = text_to_process[second_index +
                                       len(delimiter): len(text_to_process)]

        # create new nodes from sliced texts
        new_text_nodes = [TextNode(other_text_1, TextType.TEXT), TextNode(
            text_with_delimiter, text_type), TextNode(other_text_2, TextType.TEXT)]
        filtered_empty_nodes = list(
            filter(lambda x: x.text != "", new_text_nodes))

        # replace the old node with the newly created nodes
        result[index_with_delimiter: index_with_delimiter +
               1] = filtered_empty_nodes

    return result


# find the first index of the node with the selected delimiter
def find_first_index_with_delimiter(nodes, delimiter):
    index = -1
    for i in range(0, len(nodes)):
        if nodes[i].text.find(delimiter) != -1:
            return i
    return index
