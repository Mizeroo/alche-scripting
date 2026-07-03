##  Regular Expressions

A regular expression, or regex, is a sequence of characters that defines a search pattern. Regex is used to check whether a string contains a certain pattern, to find and extract parts of a string, or to replace parts of a string that match a pattern.

### Common Regex Concepts

- **Literal characters**: match themselves exactly. For example, `cat` matches the word `cat`.
- **Anchors**: `^` marks the start of a string, and `$` marks the end.
- **Character classes**: `\w` matches any word character (letters, digits, underscore), `\d` matches any digit, `\s` matches any whitespace character.
- **Quantifiers**: `+` means one or more, `*` means zero or more, `?` means zero or one, `{n}` means exactly n times.
- **Groups**: parentheses `( )` capture part of a match so it can be reused or extracted later.
- **Alternation**: the pipe symbol `|` means "or", allowing a pattern to match one of several options.
- **Escaping**: a backslash `\` is used before special characters like `.` or `*` when you want to match them literally.

### Common Uses

Regular expressions are commonly used in programming languages to validate input (like emails or phone numbers), search through text, or extract specific data from larger strings.
