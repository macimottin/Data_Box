import numpy
import sys
import matplotlib.pyplot as plt

def line_print():

    for i in range (0, int(sample)):

        print(float(result[i]))

def create_file():

    file = open("sample.txt", "w")

    for i in range (0, int(sample)):
        file.write(str(result[i]) + "\n")
    file.close()

def create_graph():

    n, bins, patches = plt.hist(result, 50, density=True, facecolor='g', alpha=0.75)
    
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.xlim(40, 160)
    plt.ylim(0, 0.03)
    plt.grid(True)
    plt.show()

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
    create_graph()
    
    print("Run again? (write 'yes' to confirm or press enter to finish the app)")

    newRun = input()

    if newRun == str('yes'):
        continue
    
    else:   
     sys.exit()
