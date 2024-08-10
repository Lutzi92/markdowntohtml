from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)

def split_nodes_delimiter(old_nodes,delimiter, text_type):
    new_nodes= []
    for old_node in old_nodes:
        split_string= old_node.text.split(delimiter)
        left_string = split_string[0]
        middle_string = split_string[1]
        right_string = split_string[2]
        new_nodes.append(TextNode(left_string,old_node.text_type,))
        new_nodes.append(TextNode(middle_string, text_type,))
        new_nodes.append(TextNode(right_string,old_node.text_type,))
    return new_nodes