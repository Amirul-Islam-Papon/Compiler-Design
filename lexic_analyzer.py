import re

# List of keywords
keywords = {'if', 'else', 'int', 'float', 'char', 'void', 'main'}

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

# Regex patterns
patterns = {
    'comment_multiline': re.compile(r'/\*.*?\*/', re.DOTALL),
    'comment_single': re.compile(r'//.*'),
    'logical_operator': re.compile(r'(>=|<=|==|!=|>|<)'),
    'arithmetic_operator': re.compile(r'[\+\-\*/=]'),
    'punctuation': re.compile(r'[;:,]'),
    'parenthesis': re.compile(r'[()\[\]{}]'),
    'constant': re.compile(r"\b\d+(\.\d+)?\b|'.'"),
    'identifier': re.compile(r'\b[a-zA-Z_]\w*\b')
}

def remove_comments(code):
    code = re.sub(patterns['comment_multiline'], '', code)
    code = re.sub(patterns['comment_single'], '', code)
    return code

def classify(code):
    code = remove_comments(code)

    # Extract tokens
    tokens['Logical Operator'].update(patterns['logical_operator'].findall(code))
    tokens['Arithmetic Operator'].update(patterns['arithmetic_operator'].findall(code))
    tokens['Punctuation'].update(patterns['punctuation'].findall(code))
    tokens['Parenthesis'].update(patterns['parenthesis'].findall(code))
    tokens['Constant'].update(patterns['constant'].findall(code))

    all_identifiers = patterns['identifier'].findall(code)

    for word in all_identifiers:
        if word in keywords:
            tokens['Keyword'].add(word)
        else:
            tokens['Identifier'].add(word)

def display_output():
    for category, items in tokens.items():
        formatted_items = ', '.join(sorted(set(str(i[0] if isinstance(i, tuple) else i) for i in items)))
        print(f"{category} ({len(items)}): {formatted_items}")

# ====================
# MAIN EXECUTION BLOCK
# ====================

# Option 1: Read from console


# Option 2: Read from file (uncomment to use file)
with open('input.c', 'r') as f:
     source_code = f.read()

classify(source_code)
display_output()
