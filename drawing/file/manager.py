import os


class FileManager:
    def __init__(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        self.root_path = os.path.join(current_path, '../../')

    def get_input_file_data(self):
        with open(self.root_path + 'input.txt', 'r') as file:
            file_data = file.read()
        return self.format_input_data(file_data)

    def format_input_data(self, file_data):
        formated_data = []
        lines = file_data.split('\n')
        for line in lines:
            line_data = line.split()
            if line_data:
                formated_data.append(line_data)
        return formated_data

    def write_output_file(self, lines_data):
        with open(self.root_path + 'output.txt', 'w') as file:
            file.writelines(lines_data)
