from file.manager import FileManager
from drawer.manager import DrawerManager

file_manager = FileManager()
drawer_manager = DrawerManager()
drawing_commands = file_manager.get_input_file_data()
output_data = drawer_manager.draw(drawing_commands)
file_manager.write_output_file(output_data)
