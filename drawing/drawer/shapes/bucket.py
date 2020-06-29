import numpy as np
from skimage.morphology import flood_fill

from .base import BaseShape, DrawInCanvas

BUCKET_FILL_KEY = 2


class BucketFillShape(BaseShape, DrawInCanvas):
    shape_name = 'BucketFill'
    shape_strokes = 3
    x = 0
    y = 0
    colour = ''

    def validate(self, strokes):
        is_valid = super().validate(strokes)
        strokes_count = len(strokes)
        return is_valid or (
            (not is_valid and strokes_count == self.shape_strokes) and
            (strokes[0] != '0' and strokes[1] != '0' and strokes[2] == '0'))

    def set_shape_data(self, strokes):
        self.x = int(strokes[0])
        self.y = int(strokes[1])
        self.colour = strokes[2]

    def fills_in_canvas(self):
        return ((self.x >= 0 and self.x <= self.canvas.width)
                and (self.y >= 0 and self.y <= self.canvas.height))

    def get_params(self):
        return [
            self.x,
            self.y,
            self.colour,
        ]

    def set_shape_in_canvas(self):
        """
        The fill feature is achieve by using a flood fill type algorithm
        see: https://en.wikipedia.org/wiki/Flood_fill
        """

        filled_canvas_copy = self.perform_flood_fill()
        self.fill_canvas(filled_canvas_copy)

    def perform_flood_fill(self):
        """
        skimage´s flood_fill method seems to work only with numbers
        maybe with more time I could find an efficient way to implement it
        for now it works just well in this way.

        The best solution here would be to find the way to achieve flood_fill
        to work with chararrays, doing that, the perform_flood_fill and fill_canvas
        methods wouldn´t be necessary anymre, and all of this could be done in one line
        """
        column = self.x - 1
        row = self.y - 1
        canvas_copy = self.canvas.canvas.copy()
        canvas_copy[canvas_copy != b' '] = b'1'
        canvas_copy[canvas_copy == b' '] = b'0'
        fillable_canvas = np.array(canvas_copy, dtype=np.int32)
        return flood_fill(fillable_canvas, (row, column), BUCKET_FILL_KEY)

    def fill_canvas(self, filled_canvas_copy):
        """
        not the best solution, maybe with 2 days more
        I could find another better solution
        """
        for rowIndex, row in enumerate(filled_canvas_copy):
            for columnIndex, column in enumerate(row):
                if column == BUCKET_FILL_KEY:
                    self.canvas.canvas[rowIndex][columnIndex] = self.colour
