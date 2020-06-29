from .canvas import CanvasShape
from .manager import ShapesManager


class TestShapesManager():
    def setup(self):
        self.shapes_manager = ShapesManager()

    def test_it_gets_shape_and_strokes(self):
        shape_data = ['C', '20', '4']
        shape, strokes = self.shapes_manager.get_shape_and_strokes(shape_data)
        assert shape == 'C'
        assert strokes == ['20', '4']

    def test_it_builds_shape(self):
        shape_data = ['C', '20', '4']
        shaper = self.shapes_manager.build_shape(shape_data)
        assert type(shaper) is CanvasShape

    def test_it_does_not_build_shape_for_unknown_shape_type(self):
        shape_data = ['potato', '20', '4']
        shaper = self.shapes_manager.build_shape(shape_data)
        assert shaper == None

    def test_it_gets_class_for_shape(self):
        shape = 'C'
        shape_class = self.shapes_manager.get_class_for_shape(shape)
        assert shape_class == CanvasShape
