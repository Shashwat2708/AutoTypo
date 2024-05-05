def remove_comments(code, language):
    if language == "JAVA":
        # Remove single-line comments
        code = '\n'.join([line for line in code.split('\n') if not line.strip().startswith('//')])
        # Remove multi-line comments
        code = '\n'.join([line for line in code.split('\n') if not line.strip().startswith('/*') and not line.strip().endswith('*/')])
    elif language == "Python":
        # Remove single-line comments
        code = '\n'.join([line for line in code.split('\n') if not line.strip().startswith('#')])
    return code