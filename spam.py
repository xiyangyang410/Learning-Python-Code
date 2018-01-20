class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstance():
        print("Number of instances created: ", Spam.numInstances)
