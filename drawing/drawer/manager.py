from .shapes.manager import CANVAS_SHAPE_KEY, ShapesManager


class DrawerManager():
    def __init__(self):
        self.shapes_manager = ShapesManager()

    def draw(self, drawing_commands):
        output_data = []
        if self.commands_are_valid(drawing_commands):
            canvas_shape_data, shapes_data = self.get_shapes_data(
                drawing_commands)
            canvas = self.shapes_manager.build_shape(canvas_shape_data)
            output_data = self.draw_shape(canvas, output_data)
            for shape_data in shapes_data:
                shaper = self.shapes_manager.build_shape(shape_data)
                output_data = self.draw_shape(shaper,
                                              output_data,
                                              use_canvas=True,
                                              canvas=canvas)
        return output_data

    def commands_are_valid(self, drawing_commands):
        canvases = self.count_canvases(drawing_commands)
        if canvases == 0:
            print(
                'you haven\'t provided a canvas, the program can\'t continue')
            # Fast return, common in JS not sure in python
            return False

        if canvases > 1:
            print('you have provided multiple canvas,'
                  ' the program can\'t continue')
            # Fast return, common in JS not sure in python
            return False
        return True

    def count_canvases(self, drawing_commands):
        canvases = 0
        for command in drawing_commands:
            if CANVAS_SHAPE_KEY in command:
                canvases += 1
        return canvases

    def get_shapes_data(self, drawing_commands):
        canvas_shape_data = []
        shapes_data = drawing_commands.copy()
        for index, command in enumerate(drawing_commands):
            if CANVAS_SHAPE_KEY in command:
                del shapes_data[index]
                canvas_shape_data = command
        return canvas_shape_data, shapes_data

    def draw_shape(self, shaper, output_data, use_canvas=False, canvas=None):
        new_output_data = output_data
        if shaper.has_shape_data:
            if use_canvas and canvas:
                shaper.draw_in_canvas(canvas)
                if canvas.canvas_drawing_was_updated:
                    drawing = canvas.get_drawing()
                    new_output_data.append(drawing)
            else:
                drawing = shaper.get_drawing()
                new_output_data.append(drawing)
        return new_output_data
