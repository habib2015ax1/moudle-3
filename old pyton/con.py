class employe:
    def __init__(self, name, id, slary):
        print ("employe object created")
        self.name = name
        self.id = id
        self.slary =slary
    def __del__(self):
        print ("object destroyed")

ali = employe ('ali','996512','15000')
jad = employe('jad','81991221','4000')


print (ali.name)
print (ali.id)
print (ali.slary)
print(jad.name)
print (jad.id)
print (jad.slary)

    