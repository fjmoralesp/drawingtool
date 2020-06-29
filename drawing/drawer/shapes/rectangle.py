from .base import BaseShape, DrawInCanvas

RECTANGLE_SHAPE_CHARACTER = 'x'


class RectangleShape(BaseShape, DrawInCanvas):
    shape_name = 'Rectangle'
    shape_strokes = 4
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def validate(self, strokes):
        is_valid = super().validate(strokes)
        # this casing was unexpected, sadly have no enough time to refactor this
        casted_stroke = [int(stroke) for stroke in strokes]

        if is_valid and (casted_stroke[0] > casted_stroke[2] or casted_stroke[1] > casted_stroke[3]):
            self.invalid_message = 'Strokes are invalid, rectangle is backward?'
            return False

        if is_valid and (casted_stroke[0] == casted_stroke[2] or casted_stroke[1] == casted_stroke[3]):
            self.invalid_message = 'Strokes are invalid, the result shape won\'t be a rectangle'
            return False
        return is_valid

    def set_shape_data(self, strokes):
        self.x1 = int(strokes[0])
        self.y1 = int(strokes[1])
        self.x2 = int(strokes[2])
        self.y2 = int(strokes[3])

    def fills_in_canvas(self):
        return ((self.x1 >= 0 and self.x1 <= self.canvas.width)
                and (self.y1 >= 0 and self.y1 <= self.canvas.height)
                and (self.x2 >= 0 and self.x2 <= self.canvas.width)
                and (self.y2 >= 0 and self.y2 <= self.canvas.height))

    def get_params(self):
        return [
            self.x1,
            self.y1,
            self.x2,
            self.y2,
        ]

    def set_shape_in_canvas(self):
        self.canvas.canvas[self.y1 - 1:self.y2,
                           self.x1 - 1] = RECTANGLE_SHAPE_CHARACTER
        self.canvas.canvas[self.y1 - 1:self.y2,
                           self.x2 - 1] = RECTANGLE_SHAPE_CHARACTER
        self.canvas.canvas[self.y1 - 1][self.x1 -
                                        1:self.x2] = RECTANGLE_SHAPE_CHARACTER
        self.canvas.canvas[self.y2 - 1][self.x1 -
                                        1:self.x2] = RECTANGLE_SHAPE_CHARACTER
