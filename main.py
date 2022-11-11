from student import Student
from readfile import parseFiles

##TODO: Make a method that, for each element in the 2D array from readFile.py, constructs a student object and call the str() method on it
        #each of these strings is to be written to the output file, output.txt.
        
def main():
    file = open("output.txt", 'w')
    stringToFile(file)
    return 0

def stringToFile(file):
    studentRecords = parseFiles()

    for element in studentRecords:
        student = str(Student(element[0], element[1], element[2], element[3], element[4], element[5]))
        file.write(student)

    return 0

if __name__ == "__main__":
    main()
else:
    print("no CoCoMo")