class Circle:
    Id = 0
    radius = 0
    color = ""
    display = True

    def __init__(self,id,r,c,d):
        self.Id = id
        self.radius = c
        self.color = c
        self.display = d

    def circumfrence(self):
        return 3.14 * 2 * self.radius