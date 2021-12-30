import sys
import os

copy = False

def doFile(filename, copy):
    print("Processing file: '" + filename + "'" )
    if(copy):
        os.system("cp " + filename + " " +filename[:-1]+"~") # Copy file to backup it
    f = open(filename, "r")
    file = f.readlines()

    vlnovky = ["a","A","k","K","i", "I", "u", "U", "s", "S", "o", "O", "v", "V"]

    replaced = []

    for line in file:
        for vl in vlnovky:
            tbR = " " + vl + " " # To Be Replaced
            RV = " " + vl + "~"# Replace value
            line = line.replace(tbR, RV)

        replaced.append(line)

    f.close()

    f = open(filename, "w")
    f.writelines(replaced)
    f.close()

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("Málo argumentů")
        quit()
    elif(len(sys.argv) == 2):
        doFile(sys.argv[1], copy)
    else:
        for i in range(1, len(sys.argv)):
            doFile(sys.argv[i], copy)
