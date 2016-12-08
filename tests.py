from keras.datasets import mnist
import numpy as np

from sklearn.linear_model import SGDClassifier

(X_data, X_label), (Y_data, Y_label) = mnist.load_data()

X = []
for img in X_data:
    new_img = []
    for line in img:
        for pixel in line:
            new_img.append(pixel)
    X.append(new_img)

X = X[:1000]

Y = []
for label in X_label:
    Y.append(label)

Y = Y[:1000]


X_test = []
for img in Y_data:
    new_img = []
    for line in img:
        for pixel in line:
            new_img.append(pixel)
    X_test.append(new_img)

X_test = X_test[:100]

Y_test = []
for label in Y_label:
    Y_test.append(label)

Y_test = Y_test[:100]

########################################################################################################################
#                                      Logistic regression
########################################################################################################################

classifier = SGDClassifier(loss='log', alpha=0.001, learning_rate='optimal', eta0=1, n_iter=1000)

# function fit() trains the model
clf = classifier.fit(X, Y)

#
# get the weight of the linear function and
# convert : w0 + w1*x + w2*y=0 into y = mx + b => y = x*w1/w2 - w0/w2
# This is to show the decision boundary
#
w0 = clf.intercept_[0]
w1 = clf.coef_[0][0]
w2 = clf.coef_[0][1]

predictedY = clf.predict(X)
confusion_matrix = np.zeros((10,10), dtype=np.int32)
for it in range(len(Y)):
    good_label = Y[it]
    predicted_label = predictedY[it]
    confusion_matrix[predicted_label][good_label] += 1

print(confusion_matrix)

diff = predictedY - Y
trainingAccuracy = 100*(diff == 0).sum()/np.float(len(Y))
print('Logistic regression training accuracy = ', trainingAccuracy, '%')
