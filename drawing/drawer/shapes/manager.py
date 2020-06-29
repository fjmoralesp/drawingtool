from .bucket import BucketFillShape
from .canvas import CanvasShape
from .line import LineShape
from .rectangle import RectangleShape

CANVAS_SHAPE_KEY = 'C'
LINE_SHAPE_KEY = 'L'
RECTANGLE_SHAPE_KEY = 'R'
BUCKET_FILL_SHAPE_KEY = 'B'


class ShapesManager():
    allowed_shapes = [
        CANVAS_SHAPE_KEY,
        LINE_SHAPE_KEY,
        RECTANGLE_SHAPE_KEY,
        BUCKET_FILL_SHAPE_KEY,
    ]

    def get_shape_and_strokes(self, shape_data):
        shape = shape_data[0]
        strokes = shape_data[1:]
        return shape, strokes

    def build_shape(self, shape_data):
        shape, strokes = self.get_shape_and_strokes(shape_data)
        if not shape in self.allowed_shapes:
            print('the given shape data was invalid and wont\'t be drew')
            print(shape_data)
            return

        shape_class = self.get_class_for_shape(shape)
        shaper = shape_class()
        shaper.build(strokes)
        return shaper

    def get_class_for_shape(self, shape):
        shape_classes = {
            CANVAS_SHAPE_KEY: CanvasShape,
            LINE_SHAPE_KEY: LineShape,
            RECTANGLE_SHAPE_KEY: RectangleShape,
            BUCKET_FILL_SHAPE_KEY: BucketFillShape,
        }

        return shape_classes[shape]
