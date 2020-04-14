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