import math

class Calc():

    def __init__(self, identification):
        self.identification = identification

    def is_valid_identification(self):
        if len(self.identification) != 10:
            return False
        else:
            multiplier = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            ced_array = map(lambda k: int(k), list(self.identification))[0:9]
            last = int(self.identification[9])
            result = []
            arr = map(lambda x, j: (x, j), ced_array, multiplier)
            for (i, j) in arr:
                if i * j < 10:
                    result.append(i * j)
                else:
                    result.append((i * j)-9)

            if last == int(math.ceil(float(sum(result)) / 10) * 10) - sum(result):
                return True
            else:
                return False
