fname = input("Enter file name",'w+')
try:
    fhand = open(fname)
except:
    print("File cannot opened:", fname)
    exit()

