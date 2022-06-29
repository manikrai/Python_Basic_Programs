class leap_year:

        def checkleapyear(self):
            self.year = int(input("Enter Any Year: "))
            if self.year / 1000 != 0 and self.year / 1000 < 10:
                print("Entered Number Is Four Digit Number")
            else:
                print("Entered Number Is Not Four Digit Number")

        def Yearmethod(self):
            self.checkleapyear()
            if self.year / 1000 != 0 and self.year / 1000 < 10:
                if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
                    print("{} is a leap year".format(self.year))
                else:
                    print("{} is not a leap year".format(self.year))


output = leap_year()
output.Yearmethod()
