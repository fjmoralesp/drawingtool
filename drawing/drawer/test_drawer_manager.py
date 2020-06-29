from .manager import DrawerManager


class TestDrawerManager():
    def setup(self):
        self.drawer_manager = DrawerManager()
        self.drawing = [(
            '----------------------\n' +
            '|                    |\n' +
            '|                    |\n' +
            '|                    |\n' +
            '|                    |\n' +
            '----------------------\n'
        )]

    def test_it_gets_output_data(self):
        drawing_commands = [['C', '20', '4']]
        output_data = self.drawer_manager.draw(drawing_commands)
        assert output_data == self.drawing

    def test_it_gets_same_number_of_outputs_from_x_number_of_drawing_commands(self):
        drawing_commands = [['C', '20', '4'], ['L', '1', '2', '6', '2']]
        output_data = self.drawer_manager.draw(drawing_commands)
        assert len(output_data) == len(drawing_commands)

    def test_it_validates_canvas_was_provided(self):
        drawing_commands = [['L', '1', '2', '6', '2']]
        is_valid = self.drawer_manager.commands_are_valid(drawing_commands)
        assert is_valid == False

    def test_it_validates_there_are_not_multiple_canvases(self):
        drawing_commands = [['C', '20', '4'], ['C', '10', '1']]
        is_valid = self.drawer_manager.commands_are_valid(drawing_commands)
        assert is_valid == False

    def test_it_counts_canvases(self):
        drawing_commands = [['C', '20', '4'], ['C', '10', '1']]
        count = self.drawer_manager.count_canvases(drawing_commands)
        assert count == 2

    def test_it_gets_shapes_data(self):
        drawing_commands = [
            ['C', '20', '4'],
            ['L', '1', '2', '6', '2'],
            ['L', '6', '3', '6', '4'],
        ]

        canvas_shape_data, shapes_data = self.drawer_manager.get_shapes_data(drawing_commands)
        assert canvas_shape_data == ['C', '20', '4']
        assert shapes_data == [['L', '1', '2', '6', '2'], ['L', '6', '3', '6', '4'],]

    def test_it_draws_shape(self):
        output_data = []
        canvas_shape_data = ['C', '20', '4']
        canvas = self.drawer_manager.shapes_manager.build_shape(canvas_shape_data)
        new_output_data = self.drawer_manager.draw_shape(canvas, output_data)
        assert new_output_data == self.drawing
