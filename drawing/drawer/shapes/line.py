from .base import BaseShape, DrawInCanvas

LINE_SHAPE_CHARACTER = 'x'


class LineShape(BaseShape, DrawInCanvas):
    shape_name = 'Line'
    shape_strokes = 4
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def set_shape_data(self, strokes):
        self.x1 = int(strokes[0])
        self.y1 = int(strokes[1])
        self.x2 = int(strokes[2])
        self.y2 = int(strokes[3])

    def fills_in_canvas(self):
        return ((self.x1 >= 0 and self.x1 <= self.canvas.width)
                and (self.y1 >= 0 and self.y1 <= self.canvas.height)
                and (self.x2 >= 0 and self.x2 <= self.canvas.width)
                and (self.y2 >= 0 and self.y2 <= self.canvas.height) and (
                    (self.x1 == self.x2) or (self.y1 == self.y2)
                )  # only horizontal or vertical lines allowed
                )

    def get_params(self):
        return [
            self.x1,
            self.y1,
            self.x2,
            self.y2,
        ]

    def set_shape_in_canvas(self):
        if self.x1 == self.x2:
            self.draw_vertical_line()
            return

        if self.y1 == self.y2:
            self.draw_horizontal_line()
            return

    def draw_vertical_line(self):
        column = self.x1 - 1
        row_range_init = self.y1 - 1
        row_range_end = self.y2
        self.canvas.canvas[row_range_init:row_range_end,
                           column] = LINE_SHAPE_CHARACTER

    def draw_horizontal_line(self):
        row = self.y1 - 1
        column_range_init = self.x1 - 1
        column_range_end = self.x2
        self.canvas.canvas[row][
            column_range_init:column_range_end] = LINE_SHAPE_CHARACTER
