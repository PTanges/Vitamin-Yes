class profile:
    def __init__(self, name_first, name_last):
        self.name_first = name_first
        self.name_last = name_last
        self.height, self.weight = 0
        self.BMI = 0

        self.age, self.sex = 0

    # this should prolly have data verification?? ill get to it when i get to it
    def GetHeight(self, height):
        self.height = float(height) # BMI requires height in meters. add conversion later if we input height in ft/in instead

    def GetWeight(self, weight):
        self.weight = float(weight) # BMI requires weight in kg. add conversion later if we input weight in lbs

    def GetBMI(self, weight, height):
        self.BMI = weight / (height * height)