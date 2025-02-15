def markdown_to_blocks(markdown):
    initial_split = markdown.split("\n\n")
    stripped = list(map(lambda x: x.strip(), initial_split))
    filter_empty = list(filter(lambda x: len(x) > 0, stripped))
    return filter_empty
