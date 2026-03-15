
class InsertionSort:
    def __init__(self, ul):
        self.i = 1
        self.j = self.i-1
        self.array = ul
        self.key = self.array[self.i]
        self.list_sorted = False
        self.iterations = 0
        self.comparisons = 0
    def sort_frame(self): # each iteration of insertion sort written in a function, this funciton is called in the while loop in visualizer.py
        if self.i< len(self.array):
            if self.j>=0 and self.key < self.array[self.j]:
                self.array[self.j+1] = self.array[self.j]
                self.j-=1
                self.comparisons +=1
            else:
                self.array[self.j+1] = self.key
                self.i +=1
                if self.i != len(self.array):
                    self.key = self.array[self.i]
                self.j = self.i-1
            self.iterations +=1
        else:
            self.list_sorted = True

        return self.array # returns state of the array after each iterations, reflected through the bars in visualizations.