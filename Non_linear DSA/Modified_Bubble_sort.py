class Bubble_sort:
    def __init__(self,numbers= None):
        self.num = numbers if numbers is not None else []

    def sorting(self):
        val = len(self.num)-1
        self.num = self.rsorting(self.num,val)

    def rsorting(self, values, val):
        if val <= 0:
            return values
        pointer = 0
        swap_flage = False
        return self.comp_val(values, pointer, val, swap_flage)
    
    def comp_val(self, values, pointer, val, swap_flage):
        if values[pointer] > values[pointer +1]:
            values[pointer],values[pointer +1] = values[pointer +1],values[pointer]
            swap_flage = True


        if pointer +1 < val:
            return self.comp_val(values, pointer + 1, val, swap_flage)
        if not swap_flage:
            return values
        return self.rsorting(values, val -1)
    
s1 = Bubble_sort([24,58,11,67,92,43])
s1.sorting()
print(s1.num)