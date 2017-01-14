# python 2
# take one crossroad as one training data

import numpy as np
import tensorflow as tf

# features list
features_idx_AM = range(5, 11) + range(13, 33)
features_idx_PM = range(5, 11) + range(33, 53)

# input
X = []
Y = []

# get data, make feature matrix 
# only one year's AM for now
with open("../new/info.txt") as f:
    features = ((f.readline())[:-1]).split(',')
    features_AM = [features[i] for i in range(len(features)) if i in features_idx_AM]
    features_PM = [features[i] for i in range(len(features)) if i in features_idx_PM]
    for line in f:
        features = (line[:-1]).split(',')
        X.append([int(features[i]) for i in range(len(features)) if i in features_idx_AM])
        X.append([int(features[i]) for i in range(len(features)) if i in features_idx_PM])

# get data, make label matrix
with open('../new/102_count.txt') as f:
    f.readline()
    for line in f:
        Y.append(int(line[:-1].split(',')[1]))
        Y.append(int(line[:-1].split(',')[2]))

feature_size = len(features_idx_AM)
X = np.array(X, dtype=np.float32)
Y = np.array(Y, dtype=np.float32)
Y = Y / Y.sum()
print X
print Y
print X.shape, Y.shape


# graph (linear regression to possibility)
graph = tf.Graph()
with graph.as_default():
    # dataset
    tf_train_dataset = tf.constant(X[:,:])
    tf_train_poss = tf.constant(Y[:])
    # variables
    weights = tf.Variable(tf.zeros([feature_size]))
    bias = tf.Variable(tf.zeros([1]))

    logits = tf.reduce_sum(tf.mul(tf_train_dataset, weights), 1) + bias
    print logits
    loss = tf.reduce_mean(tf.square(logits - tf_train_poss))

    optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
    
    train_prediction = logits

num_steps = 10
#train
with tf.Session(graph = graph) as session:
    tf.initialize_all_variables().run()
    for step in range(num_steps):
        _, w, b, l, pred = session.run([optimizer, weights, bias, loss, train_prediction])
        if (step % 1 == 0):
            print 'at step', step, 'loss =', l
            print 'prediction =', pred
            print 'weights =', w
            print 'bias =', b
            print ''

from sklearn import linear_model  
# sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print 'coefficients:', regr.coef_
print 'predict:', regr.predict(X), regr.predict(X).shape

