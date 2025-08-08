# Markdown Guide

## Basic Formatting

### Text Styling

| Style | Syntax | Example Output |
|-------|--------|---------------|
| Bold | `**text**` or `__text__` | **text** |
| Italic | `*text*` or `_text_` | *text* |
| Strikethrough | `~~text~~` | ~~text~~ |
| Bold & Italic | `**_text_**` | **_text_** |
| All Bold & Italic | `***text***` | ***text*** |
| Subscript | `<sub>text</sub>` | <sub>text</sub> |
| Superscript | `<sup>text</sup>` | <sup>text</sup> |
| Underline | `<ins>text</ins>` | <ins>text</ins> |

### Quoting Text

To quote text, use the > character:

```
> This is a quote
```

Renders as:
> This is a quote

### Code Formatting

For inline code, use single backticks:
```
Use `git status` to list changes
```

For code blocks, use triple backticks with optional language specification:

\```python
def hello():
    print("Hello, World!")
\```

### Links

Create links with brackets for text and parentheses for URL:
```
[Link Text](URL)
[Visit GitHub](https://github.com)
```

### Images

Insert images similar to links, but with a leading !:
```
![Alt Text](image-url)
```

### Lists

Unordered lists use *, -, or +:
```
* Item 1
* Item 2
  * Subitem 2.1
  * Subitem 2.2
```

Ordered lists use numbers:
```
1. First item
2. Second item
   1. Subitem 2.1
   2. Subitem 2.2
```

### Task Lists

Create checkable task lists:
```
- [x] Completed task
- [ ] Uncompleted task
```

### Tables

Create tables using | and - characters:

```
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Collapsed Sections

Create collapsible sections:

```html
<details>
<summary>Click to expand</summary>

Content goes here...

</details>
```

### Mathematical Expressions

Use LaTeX syntax between $ symbols for inline math or $$ for block math:

```
$E = mc^2$

$$
\frac{d}{dx}e^x = e^x
$$
```

### Diagrams

You can create diagrams using Mermaid:

\```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
\```

### Footnotes

Add footnotes[^1] to your text:

```
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

### Comments

Add hidden comments that won't appear in rendered Markdown:

```
<!-- This comment won't be visible in rendered Markdown -->
```

### Alerts (GitHub Specific)

GitHub supports special alert blocks:

```
> [!NOTE]
> Useful information that users should know.

> [!WARNING]
> Critical content demanding immediate user attention.

> [!TIP]
> Helpful advice for users.

> [!IMPORTANT]
> Essential information users need to succeed.

> [!CAUTION]
> Negative potential consequences of an action.
```

### Escaping Characters

Use backslash (\\) to escape Markdown formatting characters:
```
\*Not italic\*
\`Not code\`
```

### Line Breaks

Add two spaces at the end of a line for a soft break  
Or use a backslash\
For a hard break.

## Best Practices

1. Use consistent formatting throughout your document
2. Include a table of contents for longer documents
3. Preview your Markdown before committing
4. Use reference links for repeated URLs
5. Keep line lengths readable (usually < 80 characters)

## Additional Resources

- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- [CommonMark Spec](https://spec.commonmark.org/)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
