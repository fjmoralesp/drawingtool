import numpy as np
from .base import BaseShape

class CanvasShape(BaseShape):
    drawing = ''
    shape_name = 'Canvas'
    canvas = []
    width = 0
    height = 0
    shape_strokes = 2
    canvas_drawing_was_updated = False

    def validate(self, strokes):
        is_valid = super().validate(strokes)
        if not is_valid:
            self.invalid_message += '\n' + self.shape_name + ' wasn\'t drew, the program can\'t continue'
        return is_valid

    def set_shape_data(self, strokes):
        self.width = int(strokes[0])
        self.height = int(strokes[1])
        self.build_cavas()

    def build_cavas(self):
        self.canvas = np.chararray((self.height, self.width))
        self.canvas[:] = ' '
        self.build_canvas_drawing()

    def build_canvas_drawing(self):
        canvas_header = '--'
        canvas_footer = '--'
        for dash in range(self.width):
            canvas_header += '-'
            canvas_footer += '-'
        self.build_drawing(canvas_header, canvas_footer)

    def update_canvas_drawing(self):
        self.canvas_drawing_was_updated = True
        splited_drawing = self.drawing.split('\n')
        canvas_header = splited_drawing[0]
        canvas_footer = splited_drawing[-2]
        self.build_drawing(canvas_header, canvas_footer)

    def build_drawing(self, header, footer):
        canvas_rows = self.canvas.decode().tolist()
        rows_data = []
        for row in canvas_rows:
            rows_data.append(('|' + ''.join(row) + '|'))
        self.drawing = header + '\n' + '\n'.join(rows_data) + '\n' + footer + '\n'

    def get_drawing(self):
        self.canvas_drawing_was_updated = False
        return self.drawing
