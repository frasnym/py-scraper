def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
