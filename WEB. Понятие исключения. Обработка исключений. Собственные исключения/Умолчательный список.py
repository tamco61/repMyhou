class DefaultList(list):
    def __init__(self, standart):
        super().__init__()
        self.standart = standart
        
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return self.standart