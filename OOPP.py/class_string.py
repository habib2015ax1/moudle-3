class Reverse:
    def __init__(self, s):
        self.s = s

    def show(self):
        print(" ".join(self.s.split()[::-1]))

Reverse("I love Python").show()