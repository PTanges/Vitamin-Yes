class profile:
    def __init__(self, email, password, name_first):
        self.email = email
        self.password = password
        self.name_first = name_first

        self.height, self.weight, self.BMI = 0

        self.hrsleep, self.hrexercise = 0
        self.calories = 0

        self.age, self.sex = 0
        self.pregnant = False

    # this should prolly have data verification?? ill get to it when i get to it
    def SetBMI(self, weight, height):
        self.BMI = weight / (height * height)

    def SetHeight(self, height):
        self.height = float(height) # BMI requires height in meters. add conversion later if we input height in ft/in instead
        if self.weight > 0: # prevent passing garbage data to setbmi
            self.SetBmi(self, self.weight, self.height)

    def SetWeight(self, weight):
        self.weight = float(weight) # BMI requires weight in kg. add conversion later if we input weight in lbs
        if self.height > 0:
            self.SetBmi(self, self.weight, self.height)

    def SetHrSleep(self, hrsleep):
        self.hrsleep = hrsleep

    def SetHrExercise(self, hrexercise):
        self.hrexercise = hrexercise

    def SetCalories(self, calories):
        self.calories = calories

    def SetAge(self, age):
        self.age = age # add datetime var birthday + function to auto-increment on birthday? ehh might be a bit much for just a class project

    def SetSex(self, sex):
        self.sex = sex

    def SetPregnant(self, pregnant):
        self.pregnant = pregnant