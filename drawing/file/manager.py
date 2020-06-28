import os

class FileManager:
    def __init__(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        self.root_path = os.path.join(current_path, '../../')

    def format_input_data(self, file_data):
        formated_data = []
        lines = file_data.split('\n')
        for line in lines:
            formated_data.append(line.split())
        return formated_data

    def get_input_file_data(self):
        file = open(self.root_path + 'input.txt', 'r')
        file_data = file.read()
        file.close()
        return self.format_input_data(file_data)

    def format_output_data(self, file_data):
        return file_data

    def write_output_file(self, data):
        file = open(self.root_path + 'output.txt', 'w')
        formated_data = self.format_output_data('hola123')
        file.write(formated_data)
        file.close()
