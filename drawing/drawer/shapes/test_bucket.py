from .canvas import CanvasShape
from .bucket import BucketFillShape


class TestBucketFillShape():
    def setup(self):
        strokes = ['20', '4']
        self.canvas_shape = CanvasShape()
        self.canvas_shape.build(strokes)
        self.bucket_fill_shape = BucketFillShape()

    def test_it_does_not_build_with_invalid_data(self):
        strokes = []
        self.bucket_fill_shape.build(strokes)
        assert self.bucket_fill_shape.x == 0
        assert self.bucket_fill_shape.y == 0
        assert self.bucket_fill_shape.colour == ''

    def test_it_builds_shape_data(self):
        strokes = ['10', '3', 'o']
        self.bucket_fill_shape.build(strokes)
        assert self.bucket_fill_shape.x == 10
        assert self.bucket_fill_shape.y == 3
        assert self.bucket_fill_shape.colour == 'o'

    def test_it_validates_invalid_stroke_length(self):
        strokes = []
        is_valid = self.bucket_fill_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_invalid_stroke_zero_value(self):
        strokes = ['10', '0', 'o']
        is_valid = self.bucket_fill_shape.validate(strokes)
        assert is_valid == False

    def test_it_validates_valid_zero_value_for_colour(self):
        strokes = ['10', '3', '0']
        is_valid = self.bucket_fill_shape.validate(strokes)
        assert is_valid == True

    def test_it_draws_in_canvas(self):
        expected_drawing = (
            '----------------------\n' +
            '|oooooooooooooooooooo|\n' +
            '|oooooooooooooooooooo|\n' +
            '|oooooooooooooooooooo|\n' +
            '|oooooooooooooooooooo|\n' +
            '----------------------\n'
        )

        strokes = ['1', '1', 'o']
        self.bucket_fill_shape.build(strokes)
        self.bucket_fill_shape.draw_in_canvas(self.canvas_shape)
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

        strokes = ['10', '90', 'o']
        self.bucket_fill_shape.build(strokes)
        self.bucket_fill_shape.draw_in_canvas(self.canvas_shape)
        assert self.canvas_shape.drawing == expected_drawing
