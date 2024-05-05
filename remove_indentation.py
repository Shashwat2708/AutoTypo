

def remove_indentation(code, is_not_indented):
    if is_not_indented == "Yes":
        return code  # If the code is already not indented, return it as it is
    elif is_not_indented== "No":
        lines = code.split('\n')  # Split the code into lines
        min_indent = float('inf')  # Initialize minimum indentation to a large number

        # Find the minimum indentation
        for line in lines:
            if line.strip():  # Ignore empty lines
                indent = len(line) - len(line.lstrip())
                min_indent = min(min_indent, indent)

        # Remove the minimum indentation from each line
        cleaned_code = '\n'.join(line[min_indent:] for line in lines)
        return cleaned_code

