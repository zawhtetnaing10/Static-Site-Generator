from markdown_to_html import markdown_to_html
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {template_path}")

    # read markdown
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()

    # read template
    template_file = open(template_path, "r")
    template = template_file.read()

    # convert to html body and title
    html_content = markdown_to_html(markdown).to_html()
    title = extract_title(markdown)
    updated_html = template.replace(r" {{ Title }} ", title).replace(
        r"{{ Content }}", html_content)

    # write to destination
    dest_directory = os.path.dirname(dest_path)
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory, exist_ok=True)

    with open(dest_path, "w") as dest:
        dest.write(updated_html)
