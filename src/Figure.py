class Figure:
    # class contructor
    def __init__(self, name, angl):
        self.name = name
        self.angl = angl

    def get_name(self):
        return self.name

    def get_angl(self):
        return self.angl

    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
