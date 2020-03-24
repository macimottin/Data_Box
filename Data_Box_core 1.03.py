import numpy
import sys

def line_print():

    for i in range (0, int(sample)):

        print(float(result[i]))

def create_file():

    file = open("sample.txt", "w")

    for i in range (0, int(sample)):
        file.write(str(result[i]) + "\n")
    file.close()

print('This program generates random data with normal statistic behavior')

while True:

    # Request mean value
    print('Please inform the mean value')
    mean = input()
    try:
        mean = float(mean)
    except ValueError:
        print('must be an integer or float')
        continue

    # Request standard deviation
    print('Please inform the standard deviation')
    stdev = input()
    try:
        stdev = float(stdev)
    except ValueError:
        print('must be an integer or float')
        continue

    # Request sample size
    print('Please inform the sample size')
    sample = input()
    try:
        sample = int(sample)

    except ValueError:
        print('must be an integer')
        continue

    result = numpy.random.normal(float(mean),float(stdev),int(sample))
    line_print()
    create_file()

    print("Run again? (write 'yes' to confirm or press enter to finish the app)")

    newRun = input()

    if newRun == str('yes'):
        continue
    
    else:   
     sys.exit()
