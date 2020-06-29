from .canvas import CanvasShape
from .line import LineShape


class TestLineShape():
    def setup(self):
        strokes = ['20', '4']
        self.canvas_shape = CanvasShape()
        self.canvas_shape.build(strokes)
        self.line_shape = LineShape()

    def test_it_does_not_build_with_invalid_data(self):
        strokes = []
        self.line_shape.build(strokes)
        assert self.line_shape.x1 == 0
        assert self.line_shape.y1 == 0
        assert self.line_shape.x2 == 0
        assert self.line_shape.y2 == 0

    def test_it_builds_shape_data(self):
        strokes = ['1', '2', '6', '2']
        self.line_shape.build(strokes)
        assert self.line_shape.x1 == 1
        assert self.line_shape.y1 == 2
        assert self.line_shape.x2 == 6
        assert self.line_shape.y2 == 2

    def test_it_validates_invalid_stroke_length(self):
        strokes = []
        is_valid = self.line_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_invalid_stroke_zero_value(self):
        strokes = ['1', '0', '6', '2']
        is_valid = self.line_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_invalid_stroke_equality_values(self):
        strokes = ['1', '2', '1', '2']
        is_valid = self.line_shape.validate(strokes)
        assert is_valid == False

    def test_it_draws_in_canvas(self):
        expected_drawing = (
            '----------------------\n' +
            '|                    |\n' +
            '|xxxxxx              |\n' +
            '|                    |\n' +
            '|                    |\n' +
            '----------------------\n'
        )

        strokes = ['1', '2', '6', '2']
        self.line_shape.build(strokes)
        self.line_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing

    def test_it_does_not_draw_in_canvas_if_it_does_not_fill(self):
        expected_drawing = (
            '----------------------\n' +
            '|                    |\n' +
            '|                    |\n' +
            '|                    |\n' +
            '|                    |\n' +
            '----------------------\n'
        )

        strokes = ['50', '2', '6', '2']
        self.line_shape.build(strokes)
        self.line_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing

    def test_it_draws_vertical_line(self):
        expected_drawing = (
            '----------------------\n' +
            '|     x              |\n' +
            '|     x              |\n' +
            '|     x              |\n' +
            '|     x              |\n' +
            '----------------------\n'
        )

        strokes = ['6', '1', '6', '4']
        self.line_shape.build(strokes)
        self.line_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing

    def test_it_draws_horizontal_line(self):
        expected_drawing = (
            '----------------------\n' +
            '|                    |\n' +
            '|xxxxxxxxxxxxxxxxxxxx|\n' +
            '|                    |\n' +
            '|                    |\n' +
            '----------------------\n'
        )

        strokes = ['1', '2', '20', '2']
        self.line_shape.build(strokes)
        self.line_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing
