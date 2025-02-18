import re


def extract_mark_down_images(text):
    regex_for_image_alt = r"!\[(.*?)\]"
    regex_for_image_url = r"https?:\/\/[\w.-]+(?:\/[\w\-.%]+)*\.(?:jpg|jpeg|png|gif|webp|bmp|svg)"

    return list(zip(re.findall(regex_for_image_alt, text), re.findall(regex_for_image_url, text)))


def extract_mark_down_links(text):
    print(f"Text to extract link ===> {text}")
    regex_for_anchor_text = r"\[(.*?)\]"
    regex_for_link = r"\((https?:\/\/[\w.-]+(?:\/[\w\-.%?=&#@]*)?|\/[\w\-.%?=&#@]+|\.\.?\/[\w\-.%?=&#@]*)\)"
    return list(zip(re.findall(regex_for_anchor_text, text), re.findall(regex_for_link, text)))
