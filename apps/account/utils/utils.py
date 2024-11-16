from random import randint


class Utils:
    @staticmethod
    def code_generator():
        return str(randint(100000, 999999))
