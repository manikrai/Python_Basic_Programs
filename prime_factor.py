class factor:
    def primefactor(self):
        num = int(input("Enter Any Number To Get Its Prime Factor: "))
        i = 0
        while i <= num:
            i = i + 1
            if num % i == 0:
                print(i, "Is a Prime factor Of ", num)


output = factor()
output.primefactor()
