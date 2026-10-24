phonebook = {
"sara": "45874598",
"david": "34686844",
"surya": "458537583"
}

phonebook["Riddhi"]="34578567365"

name =input("enter a name to search:")
print (phonebook)

print("number:", phonebook.get(name, "Not Found"))