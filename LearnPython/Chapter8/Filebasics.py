#find live word in this file

file = open("Chapter8/file.txt", "r")
data = file.read()
data=data.lower()
if "live " in data:
    print("Yes,live word is present here")
else:
    print("No,live word is not present here")
file.close()


# create new file using w mode write content in file
file = open("Chapter8/file1.txt", "w")
data = file.write(" My name is anil lohar")
file.close()


#append the content in this file(add at end content)
file = open("Chapter8/Writemode.txt", "a")
data = file.write(" My name is anil lohar and i am 21 year old")
file.close()

