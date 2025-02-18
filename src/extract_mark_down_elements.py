import re


def extract_mark_down_images(text):
    regex_for_image_alt = r"!\[(.*?)\]"
    regex_for_image_url = r"\(\s*(https?:\/\/[\w.-]+(?:\/[\w\-.%]+)*\.(?:jpg|jpeg|png|gif|webp|bmp|svg)|\/[\w\-.%\/]+(?:jpg|jpeg|png|gif|webp|bmp|svg)|\.\.?\/[\w\-.%\/]+(?:jpg|jpeg|png|gif|webp|bmp|svg))\s*\)"

    return list(zip(re.findall(regex_for_image_alt, text), re.findall(regex_for_image_url, text)))


def extract_mark_down_links(text):
    regex_for_anchor_text = r"\[(.*?)\]"
    regex_for_link = r"\(\s*(https?:\/\/[\w.-]+(?:\/[\w\-.%?=&#@]*)*|\/[\w\-.%?=&#@]*|\.\.?\/[\w\-.%?=&#@]*)\s*\)"
    return list(zip(re.findall(regex_for_anchor_text, text), re.findall(regex_for_link, text)))
