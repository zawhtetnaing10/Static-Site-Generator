import os
import shutil
from generate_page import generate_page


def main():
    # get public and static paths
    static_path = "static"
    public_path = "public"

    # remove items from public
    if not os.path.exists(public_path):
        os.makedirs(public_path, exist_ok=True)

    # Copy all the contents from static to public
    # TODO: - un comment this after testing generate page
    copy_from_static_to_public(static_path)

    generate_page("content/index.md", "template.html", "public/index.html")


def copy_from_static_to_public(current_path):
    paths = os.listdir(current_path)
    for path in paths:
        inner_path = f"{current_path}/{path}"

        public_path_to_copy = inner_path.replace("static", "public", 1)
        if os.path.exists(inner_path) and os.path.isfile(inner_path):
            shutil.copy(inner_path, public_path_to_copy)
        else:
            if os.path.exists(public_path_to_copy):
                shutil.rmtree(public_path_to_copy)
            os.makedirs(public_path_to_copy, exist_ok=True)
            copy_from_static_to_public(inner_path)


main()
