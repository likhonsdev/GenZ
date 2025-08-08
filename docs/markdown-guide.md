# Markdown Formatting Guide

## Basic Formatting

### Text Styling

- **Bold text**: `**bold**` or `__bold__`
- *Italic text*: `*italic*` or `_italic_`
- ***Bold and italic***: `***bold and italic***`
- ~~Strikethrough~~: `~~strikethrough~~`
- <ins>Underline</ins>: `<ins>underline</ins>`

### Paragraphs and Line Breaks

- For a new paragraph, leave a blank line between text blocks
- For a line break without paragraph, end a line with two spaces  
  or use a backslash\
  like this

### Lists

Unordered list:
- Item 1
- Item 2
  - Nested item
  - Another nested item

Ordered list:
1. First item
2. Second item
   1. Nested numbered item
   2. Another nested item

### Task Lists

- [x] Completed task
- [ ] Pending task
- [ ] Another pending task

## Block Elements

### Blockquotes

> Single level quote
>> Nested quote
>>> Deep nested quote

### Code Blocks

Inline code: `console.log('Hello World')`

Fenced code block:
```python
def hello_world():
    print("Hello, World!")
```

### Tables

| Header 1 | Header 2 | Header 3 |
|----------|:--------:|---------:|
| Left     | Center   | Right    |
| aligned  | aligned  | aligned  |

## Links and Images

### Links

- Basic link: [Link text](https://example.com)
- Link with title: [Link text](https://example.com "Title text")
- Reference link: [Link text][reference]

[reference]: https://example.com

### Images

- Basic image: ![Alt text](image.jpg)
- Image with title: ![Alt text](image.jpg "Image title")
- Linked image: [![Alt text](image.jpg)](https://example.com)

## Advanced Formatting

### Footnotes

Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.

### Alert Boxes

> [!NOTE]
> Useful information that users should know about.

> [!WARNING]
> Critical content demanding immediate user attention.

> [!IMPORTANT]
> Essential information required for user success.

### Collapsed Sections

<details>
<summary>Click to expand/collapse</summary>

This content is hidden until expanded.
</details>

### Mathematical Expressions

When included with proper extensions, you can write math:

Inline: $E = mc^2$

Block:
$$
\frac{d}{dx}e^x = e^x
$$

### Diagrams

When supported, you can create diagrams using Mermaid:

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

### HTML Support

<div align="center">
  <h3>Centered content using HTML</h3>
  <p>You can use HTML when Markdown isn't enough</p>
</div>

## Best Practices

1. Keep your Markdown clean and consistent
2. Use reference links for frequently used URLs
3. Include alt text for images
4. Use appropriate heading levels
5. Don't skip heading levels
6. Use line breaks wisely
7. Indent nested elements properly
8. Document your Markdown structure
9. Test your Markdown in the target platform
10. Keep a style guide handy
