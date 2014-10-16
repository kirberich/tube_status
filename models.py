class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class Line(object):
    def __init__(self, name, api_code, bg_color, fg_color):
        self.name = name
        self.api_code = api_code
        self.bg_color = bg_color
        self.fg_color = fg_color

    def __repr__(self):
        return self.name
    __unicode__ = __repr__


class Station(object):
    def __init__(self, name, lines=None):
        self.name = name
        self.lines = lines if lines else []


class Map(object):
    pass
