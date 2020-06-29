import numpy as np
from .canvas import CanvasShape


class TestCanvasShape():
    def setup(self):
        self.canvas_shape = CanvasShape()

    def test_it_does_not_build_with_invalid_data(self):
        strokes = []
        self.canvas_shape.build(strokes)
        assert self.canvas_shape.width == 0
        assert self.canvas_shape.height == 0
        assert self.canvas_shape.canvas == []
        assert self.canvas_shape.drawing == ''

    def test_it_builds_shape_data(self):
        strokes = ['20', '4']
        self.canvas_shape.build(strokes)
        assert self.canvas_shape.width == 20
        assert self.canvas_shape.height == 4
        assert type(self.canvas_shape.canvas) == np.chararray
        assert self.canvas_shape.drawing != ''

    def test_it_validates_invalid_stroke_length(self):
        strokes = []
        is_valid = self.canvas_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_invalid_stroke_zero_value(self):
        strokes = ['0', '4']
        is_valid = self.canvas_shape.validate(strokes)
        assert is_valid == False

    def test_it_updates_canvas_drawing(self):
        expected_drawing = ('----------------------\n' +
                            '|HHHHHHHHHHHHHHHHHHHH|\n' +
                            '|                    |\n' +
                            '|                    |\n' +
                            '|                    |\n' +
                            '----------------------\n')

        strokes = ['20', '4']
        self.canvas_shape.build(strokes)
        self.canvas_shape.canvas[0] = 'H'
        self.canvas_shape.update_canvas_drawing()
        assert self.canvas_shape.drawing == expected_drawing
