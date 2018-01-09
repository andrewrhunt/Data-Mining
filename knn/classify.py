import pandas
import numpy as np


def classify(k, email, trainexs):
    distances = sorted([getDistance(email, trains[i]) for i in range(1, traindf.shape[0])], key=lambda x: x[1])
    votes = [distances[i][2] for i in range(0, k)]
    return np.average(votes)

def getDistance(test, train):
    distances = [pow(test[i]-train[i], 2) for i in range(1, len(test))]
    return train[0], np.sqrt(np.sum(distances)), train[len(train)-1]

if __name__ == "__main__":
    # Read in training data and testing data to numpy arrays
    traindf = pandas.read_csv('spam_train.csv', sep=',')
    testdf = pandas.read_csv('spam_test.csv', sep=',')

    # Create a set of test examples for training.
    tests = [np.array(testdf.loc[i]) for i in range(0, testdf.shape[0])]
    trains = [np.array(traindf.loc[i]) for i in range(0, traindf.shape[0])]

    distances = sorted([getDistance(tests[0], trains[i]) for i in range(1, traindf.shape[0])], key=lambda x: x[1])
    k = [distances[i][2] for i in range(0, 5)]
    print(np.average(k))
    print(k)
    print(classify(5, tests[0], trains))
    print(classify(5, tests[1], trains))

    classifications = [classify(5, tests[i], trains) for i in range(0, len(tests))]
    print(classifications)

    print("Distances: ")
    for i in range(0, 5):
        print(distances[i])


'''
1. Choose K
2. For any instance XsubNew, find K closest training measures wrt a distance measure
3. Classify XsubNew with the majority vote among the K points
'''