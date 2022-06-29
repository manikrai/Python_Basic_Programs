class powOf2:
    def __init__(self):
        self.n = 0
        self.i = 1
        self.num = 1

    def powmethod(self):
        self.n = int(input("Enter value Of n for Calculating 2^n: "))
        if self.n >= 31:
            print("This 2^n Program Works For Value Less Than 31")
        else:
            print(self.n)

    def method(self):
        self.powmethod()
        if self.n < 31:
            while self.i < self.n:
                self.i = self.i + 1
                self.num = self.num * 2
                print("Value Of 2^{} Is {}".format(self.n, self.num))


if __name__ == "__main__":
    output = powOf2()
    output.method()
