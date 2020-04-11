import random

class Data:

    def __init__(self):
        self.data = []

    def generate_data(self, type_count, data_length):
        self.type_count = type_count
        self.data = []
        for _ in range(data_length):
            x = random.random()
            y = random.random()
            v = random.randint(0, type_count - 1)
            self.data.append([[x, y], v])
        # print(self.data)

    def get_data(self):
        return self.data