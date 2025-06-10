import unittest
import blocks_markdown

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md_text_one = '''

# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item

'''
        res_one = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
            '- This is the first list item in a list block\n- This is a list item\n- This is another list item'
            ]
        md_text_two = """

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

"""
        res_two = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        test_set = [
            (md_text_one,res_one),
            (md_text_two,res_two)
        ]
        for test in test_set: 
            self.assertEqual( 
        blocks_markdown.markdown_to_blocks(test[0]),
        test[1]
        )
    
    def test_block_types(self):
        test_set = {
            blocks_markdown.BlockType.PARAGRAPH: "#This is a paragraph",
            blocks_markdown.BlockType.HEADING: "# This is a heading",
            blocks_markdown.BlockType.QUOTE: "> This is a quote",
            blocks_markdown.BlockType.UNORDERED_LIST: "- This is a list item",
            blocks_markdown.BlockType.ORDERED_LIST: "1. This is a list item",
            blocks_markdown.BlockType.CODE: "```python\nprint('Hello World')\n```"
        }
        for test in test_set: 
            self.assertEqual( 
        blocks_markdown.block_to_block_type(test_set[test]),
        test
        )



if __name__ == "__main__":
    unittest.main()