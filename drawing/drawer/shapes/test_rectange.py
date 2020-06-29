from .canvas import CanvasShape
from .rectangle import RectangleShape


class TestRectangleShape():
    def setup(self):
        strokes = ['20', '4']
        self.canvas_shape = CanvasShape()
        self.canvas_shape.build(strokes)
        self.rectangle_shape = RectangleShape()

    def test_it_does_not_build_with_invalid_data(self):
        strokes = []
        self.rectangle_shape.build(strokes)
        assert self.rectangle_shape.x1 == 0
        assert self.rectangle_shape.y1 == 0
        assert self.rectangle_shape.x2 == 0
        assert self.rectangle_shape.y2 == 0

    def test_it_builds_shape_data(self):
        strokes = ['16', '1', '20', '3']
        self.rectangle_shape.build(strokes)
        assert self.rectangle_shape.x1 == 16
        assert self.rectangle_shape.y1 == 1
        assert self.rectangle_shape.x2 == 20
        assert self.rectangle_shape.y2 == 3

    def test_it_validates_invalid_stroke_length(self):
        strokes = []
        is_valid = self.rectangle_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_invalid_stroke_zero_value(self):
        strokes = ['16', '1', '20', '0']
        is_valid = self.rectangle_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_invalid_stroke_equality_values(self):
        strokes = ['1', '2', '1', '2']
        is_valid = self.rectangle_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_rectangle_is_backward(self):
        strokes = ['20', '2', '1', '1']
        is_valid = self.rectangle_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_is_not_a_rectangle(self):
        strokes = ['1', '2', '1', '3']
        is_valid = self.rectangle_shape.validate(strokes)
        assert is_valid == False

    def test_it_draws_in_canvas(self):
        expected_drawing = ('----------------------\n' +
                            '|    xxxxxxxxxxx     |\n' +
                            '|    x         x     |\n' +
                            '|    x         x     |\n' +
                            '|    xxxxxxxxxxx     |\n' +
                            '----------------------\n')

        strokes = ['5', '1', '15', '4']
        self.rectangle_shape.build(strokes)
        self.rectangle_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing

    def test_it_does_not_draw_in_canvas_if_it_does_not_fill(self):
        expected_drawing = ('----------------------\n' +
                            '|                    |\n' +
                            '|                    |\n' +
                            '|                    |\n' +
                            '|                    |\n' +
                            '----------------------\n')

        strokes = ['16', '90', '20', '4']
        self.rectangle_shape.build(strokes)
        self.rectangle_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing
