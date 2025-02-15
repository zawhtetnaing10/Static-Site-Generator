import unittest
from extract_mark_down_elements import extract_mark_down_images
from extract_mark_down_elements import extract_mark_down_links


class TestExtractMarkdownElements(unittest.TestCase):
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_mark_down_images(text)
        correct_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                          ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(result, correct_output)

    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_mark_down_links(text)
        correct_output = [("to boot dev", "https://www.boot.dev"),
                          ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(result, correct_output)

    def test_image_invalid_image_url(self):
        text = "This is a text with ![invalid image](https://www.invalid.com/kajdkfakf.txt)"
        result = extract_mark_down_images(text)
        self.assertListEqual(result, [])

    def test_link_with_invalid_link_url(self):
        text = "This is an [invalid link](askjdf;asjfajsfdj;ajs;fdkja;)"
        result = extract_mark_down_links(text)
        self.assertListEqual(result, [])
