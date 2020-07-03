# convert file path
def make_pythonreadable_windows_path(windows_path = [r'C:\Users\mehedee\Documents']):
    python_path = ''
    for character in windows_path:
        if character == '\\':
            python_path += '/'
        else:
            python_path += character
    return python_path

    
print(make_pythonreadable_windows_path([r'C:\Users\mehedee\Documents']))