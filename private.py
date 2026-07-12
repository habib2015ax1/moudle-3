class myClass:
    _privateVar = 27
 

    def _privateMeth(self):
      print("I,m inside my class myClass")

    def hello(self):
      print ("private Variable value:",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth()
