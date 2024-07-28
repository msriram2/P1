#empty for now

class Peekaboo:

    def __init__(self, iter_list):
        self.iter_list = iter_list

    def __iter__(self):
        return self

    def __next__(self):
        index = 0
        while self.iter_list[index] != len(self.iter_list):
            return self.iter_list[index]
        else:
            raise StopIteration

    def peek(self):
        final_list = iter(self.iter_list)
        return next(final_list)

    def has_next(self):
        index = 0
        while self.iter_list[index] < len(self.iter_list):
            return True
        else:
            return False