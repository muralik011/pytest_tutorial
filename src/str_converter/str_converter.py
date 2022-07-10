class StringConverter:
    def __init__(self, str):
        self.str = str

    def to_float(self):
        return float(self.str)

    def to_int(self):
        return int(self.str)