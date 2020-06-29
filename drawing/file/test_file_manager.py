from .manager import FileManager
from unittest.mock import patch, mock_open


class TestFileManager():
    def setup(self):
        self.file_manager = FileManager()

    def test_it_sets_root_path(self):
        expected_relative_path = 'drawingtool/drawing/file/../../'
        assert expected_relative_path in self.file_manager.root_path

    def test_it_gets_input_file_data(self):
        input_file_path = self.file_manager.root_path + 'input.txt'
        lines_data = ['drawing_data']
        with patch('builtins.open',
                   mock_open(read_data='C 20 4')) as mocked_file:
            drawing_commands = self.file_manager.get_input_file_data()
            mocked_file.assert_called_once_with(input_file_path, 'r')
            assert drawing_commands == [['C', '20', '4']]

    def test_it_formats_input_data(self):
        input_data = 'R 16 1 20 3'
        formated_data = self.file_manager.format_input_data(input_data)
        assert formated_data == [['R', '16', '1', '20', '3']]

    def test_it_writes_output_file(self):
        output_file_path = self.file_manager.root_path + 'output.txt'
        lines_data = ['drawing_data']
        with patch('builtins.open', mock_open()) as mocked_file:
            self.file_manager.write_output_file(lines_data)
            mocked_file.assert_called_once_with(output_file_path, 'w')
            mocked_file().writelines.assert_called_once_with(lines_data)
