class Val_cout():
    def __init__(self,value, count):
        self.value=value
        self.count=count
    def count_plus(self):
        self.count+=1
    def __cmp__(self, other):
        if hasattr(self,other):
            return self.count.__cmp__(other.count)
    def __repr__(self):
        return '{} {}'.format(self.value, self.count)



