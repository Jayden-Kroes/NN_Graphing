import random

class Data:

    def __init__(self):
        self.positions = []
        self.types = []

    def generate_data(self, type_count, data_length):
        self.type_count = type_count
        self.positions = []
        self.types = []
        for _ in range(data_length):
            x = random.random()
            y = random.random()
            v = random.randint(0, type_count - 1)
            self.positions.append([x, y])
            self.types.append(v)
        # print(self.data)

    def get_data(self):
        return self.positions, self.types

class GridData(Data):
    def __init__(self):
        super().__init__()

    def generate_data(self, type_count, data_width, data_height):
        self.type_count = type_count
        self.positions = []
        self.types = []
        for i in range(data_width):
            for j in range(data_height):
                x = 1.0/data_width * (i+0.5)
                y = 1.0/data_height * (j+0.5)
                v = random.randint(0, type_count - 1)
                self.positions.append([x,y])
                self.types.append(v)
