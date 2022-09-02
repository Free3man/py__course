class Sorting:
    def __init__(self, numbers):
        self.numbers = numbers

    def bubbleSort(self):
        swapProcess = False
        for i in range(1, len(self.numbers)):
            if self.numbers[i-1] > self.numbers[i]:
                swapProcess = True
                self.numbers[i-1], self.numbers[i] = self.numbers[i], self.numbers[i-1]
                self.iteration += 1


        if swapProcess:
            self.bubbleSort()
        else:
            return self.numbers


countList = Sorting([73, 26, 89, 12, 45, 58])
print(countList.bubbleSort())
