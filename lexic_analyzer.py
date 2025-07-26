import re

# Keyword list (C language)
keywords = {
    'if', 'else', 'int', 'float', 'char', 'void', 'return',
    'while', 'for', 'do', 'break', 'continue', 'switch', 'case',
    'default', 'struct', 'typedef', 'union', 'static', 'const'
}

# Token categories
tokens = {
    'Keyword': set(),
    'Identifier': set(),
    'Constant': set(),
    'Arithmetic Operator': set(),
    'Logical Operator': set(),
    'Punctuation': set(),
    'Parenthesis': set()
}

# Regular expression patterns
patterns = {
    'comment_multiline': re.compile(r'/\*.*?\*/', re.DOTALL),
    'comment_single': re.compile(r'//.*'),
    'logical_operator': re.compile(r'(>=|<=|==|!=|&&|\|\||!|>|<)'),
    'arithmetic_operator': re.compile(r'[\+\-\*/=]'),
    'punctuation': re.compile(r'[;:,]'),
    'parenthesis': re.compile(r'[()\[\]{}]'),
    'constant': re.compile(r"\b\d+(?:\.\d+)?\b|'.'"),  
    'identifier': re.compile(r'\b[a-zA-Z_]\w*\b')
}

#Remove comments, unnecessary whitespace and newlines
def remove_comments(code):
    code = re.sub(patterns['comment_multiline'], '', code)
    code = re.sub(patterns['comment_single'], '', code)
    return code

def remove_whitespace(code):
    return re.sub(r'\s+', ' ', code).strip()

def remove_extra_newlines(code):
    return re.sub(r'\n+', '\n', code).strip()

# Token classification logic
def classify(code):
    code = remove_comments(code)
    code = remove_whitespace(code)
    code = remove_extra_newlines(code)

    # Extract and store constants first
    constants = patterns['constant'].findall(code)
    tokens['Constant'].update(constants)

    # Remove constants from code to prevent misclassification
    for c in constants:
        value = c[0] if isinstance(c, tuple) else c
        code = code.replace(value, ' ')  

    # Extract other tokens
    tokens['Logical Operator'].update(patterns['logical_operator'].findall(code))
    tokens['Arithmetic Operator'].update(patterns['arithmetic_operator'].findall(code))
    tokens['Punctuation'].update(patterns['punctuation'].findall(code))
    tokens['Parenthesis'].update(patterns['parenthesis'].findall(code))

    all_identifiers = patterns['identifier'].findall(code)

    for word in all_identifiers:
        if word in keywords:
            tokens['Keyword'].add(word)
        else:
            tokens['Identifier'].add(word)

# Output display
def display_output():
    for category, items in tokens.items():
        formatted_items = ', '.join(sorted(
            str(i[0] if isinstance(i, tuple) else i) for i in items
        ))
        print(f"{category} ({len(items)}): {formatted_items}")


# Main Execution
if __name__ == "__main__":
    try:
        with open('input.c', 'r') as f:
            source_code = f.read()
        classify(source_code)
        display_output()
    except FileNotFoundError:
        print("Error: 'input.c' file not found.")
