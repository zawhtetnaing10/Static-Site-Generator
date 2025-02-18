from markdown_to_html import markdown_to_html
from extract_title import extract_title
import os
import shutil


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Current directory ====> {dir_path_content}")
    paths = os.listdir(dir_path_content)

    for path in paths:
        inner_path = f"{dir_path_content}/{path}"
        print(f"Inner Path =====> {inner_path}")

        splitted_paths = inner_path.split("/")
        splitted_paths[0] = dest_dir_path
        destination_path = "/".join(splitted_paths)

        if os.path.exists(inner_path) and os.path.isfile(inner_path) and inner_path.endswith(".md"):
            destination_file_path = destination_path.replace(".md", ".html")
            print(f"Destination file path {destination_file_path}")
            generate_page(inner_path, template_path, destination_file_path)
        else:
            if os.path.exists(destination_path):
                shutil.rmtree(destination_path)
            os.makedirs(destination_path, exist_ok=True)
            generate_page_recursive(inner_path, template_path, dest_dir_path)


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
