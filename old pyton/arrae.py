import array as arr
a = arr.array('i',[1,2,3])
print ("/nathe new created array is,: ", end="")
for i in range (0,3):
    print (a[i], end= "")
print()
b = arr.array('d',[1.5,3.2,3.3])

print ("/nThe new created array is:", end="")
for i in range (0,3):
    print (b[i], end="")