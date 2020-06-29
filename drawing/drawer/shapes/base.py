from abc import ABC, abstractmethod


class DrawInCanvas(ABC):
    canvas = None

    @abstractmethod
    def fills_in_canvas(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @abstractmethod
    def set_shape_in_canvas(self):
        pass

    def draw_in_canvas(self, canvas):
        self.canvas = canvas
        if not self.fills_in_canvas():
            message = (self.shape_name +
                       ' can\'t be drew, it doesn\'t fill in canvas')
            params = self.get_params()
            print(message)
            print(params)
            return
        self.set_shape_in_canvas()
        self.canvas.update_canvas_drawing()


class BaseShape(ABC):
    invalid_message = ''
    has_shape_data = False

    @property
    @abstractmethod
    def shape_name(self):
        pass

    @property
    @abstractmethod
    def shape_strokes(self):
        pass

    @abstractmethod
    def set_shape_data(self, strokes):
        pass

    def validate(self, strokes):
        strokes_count = len(strokes)
        if not strokes_count == self.shape_strokes:
            self.invalid_message = 'Strokes should be ' + str(
                self.shape_strokes) + ', given ' + str(strokes_count)
            return False

        if '0' in strokes:
            self.invalid_message = 'Storkes values can\'t be 0'
            return False

        if self.shape_strokes == 4 and (strokes[0] == strokes[2]
                                        and strokes[1] == strokes[3]):
            self.invalid_message = (
                self.shape_name +
                ' can\'t be drew, start and end stroke points are the same')
            return False
        return True

    def build(self, strokes):
        if not self.validate(strokes):
            print('the given shape data for ' + self.shape_name +
                  ' is invalid')
            print(self.invalid_message)
            print(strokes)
            return
        self.set_shape_data(strokes)
        self.has_shape_data = True
