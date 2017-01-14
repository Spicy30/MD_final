# python 2, sklearn LR
# take one crossroad as one training data

import numpy as np
from sklearn import linear_model  

# features list
features_idx_AM = range(5, 11) + range(13, 33)
features_idx_PM = range(5, 11) + range(33, 53)

# input
X = []
Y = []
# test
tX = []
tY = []

# get data, make feature matrix 
# only one year's AM for now
with open("../new/info_reduced.txt") as f:
    features = ((f.readline())[:-1]).split(',')
    features_AM = [features[i] for i in range(len(features)) if i in features_idx_AM]
    features_PM = [features[i] for i in range(len(features)) if i in features_idx_PM]
    for line in f:
        features = (line[:-1]).split(',')
        X.append([int(features[i]) for i in range(len(features)) if i in features_idx_AM])
        tX.append([int(features[i]) for i in range(len(features)) if i in features_idx_PM])

# get data, make label matrix
with open('../new/102_count_reduced.txt') as f:
    f.readline()
    for line in f:
        Y.append(int(line[:-1].split(',')[1]))
        tY.append(int(line[:-1].split(',')[2]))

feature_size = len(features_idx_AM)
X = np.array(X, dtype=np.float32)
Y = np.array(Y, dtype=np.float32)
Y = Y / Y.sum()
tX = np.array(tX, dtype=np.float32)
tY = np.array(tY, dtype=np.float32)
tY = tY / tY.sum()
print X
print Y
print X.shape, Y.shape
print ''

regr = linear_model.LinearRegression()
regr.fit(X, Y)
#print 'coefficients:', regr.coef_

# predict training data
pred_train = regr.predict(X)
print 'possibilities of train (AM):\n', Y
print 'predict of train (AM):\n', pred_train, pred_train.sum()
print 'error:', np.abs(pred_train - Y).sum(), '\n'

# predict test data
pred_test = regr.predict(tX)
print 'possibilities of test(PM):\n', tY
print 'predict of test (PM):\n', pred_test, pred_test.sum()
print 'error:', np.abs(pred_test - tY).sum(), '\n'

