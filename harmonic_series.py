class harmonic_series:
    def harmonicmethod(self):
        n = int(input("Enter The n Value For Harmonic Series: "))
        if n != 0:
            i = 1
            while i <= n:
                i = i + 1
                print("1/{} + ".format(i))
        else:
            print("You Entered Zero Number You Need To Enter Non Zero Number ")


output = harmonic_series()
output.harmonicmethod()
