block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines= block.split("\n")
    if block.startswith("# ") or block.startswith("## ")or block.startswith("### ")or block.startswith("#### ")or block.startswith("##### ")or block.startswith("###### ") :
        return block_type_heading
    if block.startswith("```")and block.endswith("```"):
        return block_type_code
    if all(blocks.startswith(">") for blocks in lines):
        return block_type_quote
    if all(blocks.startswith("* ") for blocks in lines):
        return block_type_ulist
    if all(blocks.startswith("- ") for blocks in lines):
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    else:
        return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype==block_type_paragraph:
            pass


    return None