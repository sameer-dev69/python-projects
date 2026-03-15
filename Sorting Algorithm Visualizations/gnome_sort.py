
class GnomeSort:
    def __init__(self, ul):
        self.i = 0
        self.j = 1
        self.temp = 0
        self.list_sorted = False
        self.array = ul
        self.iterations = 0
        self.comparisons = 0
    def sort_frame(self): # each iteration of insertion sort written in a function, this funciton is called in the while loop in visualizer.py
        if self.j == len(self.array):
            self.list_sorted = True
        else:
            if(self.array[self.i] > self.array[self.j]):
                self.temp = self.array[self.i]
                self.array[self.i] = self.array[self.j]
                self.array[self.j] = self.temp
                self.comparisons+=1
                if self.i>=1:
                    self.i-=1
                    self.j-=1
            else:
                self.i+=1
                self.j+=1
            self.iterations +=1
        return self.array # returns state of the array after each iterations, reflected through the bars in visualizations.