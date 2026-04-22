with open("Chapter8/Writemode.txt","r") as f:
    data=f.read()
    data1=f.readline()
    data2=f.readlines()

    print(data,data1,data2)