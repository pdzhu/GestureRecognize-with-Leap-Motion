# coding=utf-8
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, SpatialDropout1D, MaxPooling1D, Conv1D
from keras.layers import LSTM
from keras.utils import np_utils
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from keras.callbacks import TensorBoard
# Import dataset
dataset = pd.read_csv('/home/pdzhu/GestureRecognitionSourceFiles/temp/99.csv', header=None)
# dataset = pd.read_csv('/home/pdzhu/GestureRecognitionSourceFiles/CSV_la/1.csv', header=None)

# Split to Data samples and labels
x = dataset.iloc[:, 1:44].values
y = dataset.iloc[:, 44].values

# Number of time series to work on is 60
t = 150
n_samples = len(dataset)/t

# Reshape input samples to Nx60x11
x = np.reshape(x, (x.shape[0]/t, t, x.shape[1]))
# x = np.reshape(x, (x.shape[0], len(dataset), x.shape[1]))
print x
# Set labels to these N samples
indices = [ind for ind in range(len(y)) if ind % t == 0]
y = y[indices]
y = map(int, y - 1)  # TODO
y = map(str, y)
# One-hot encode the classes
print y
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(y)
print y
# print type(y)
# y = np_utils.to_categorical(y, 4)
# label_encoder = LabelEncoder()
# y_new = label_encoder.fit_transform(y)
# # y_one_hot = np_utils.to_categorical(y_new)
# # y = y_one_hot
# y = y_new
# print y
# Split data to training and testing data

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)   # 训练集和测试集的分割

# Construct the model
n_neurons = 15
start_time = time.time()
model = Sequential()


# model.add(LSTM(n_neurons, input_shape=(X_train.shape[1], X_train.shape[2])))
# model.add(Dense(output_dim=4, init='uniform', activation='sigmoid'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# model.add(Embedding(top_words,embedding_vector_length,input_length=max_review_length))
model.add(SpatialDropout1D(0.3))
model.add(Conv1D(activation="relu", padding="same", filters=64, kernel_size=5))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(5, activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# print X_train.shape[1]
# print X_train.shape[2]
# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=15)

# Evaluation of the Training time
print "%s Minutes of Execution" % str((time.time()-start_time)/60)

# Save the model for prediction
model.save('/home/pdzhu/GestureRecognitionSourceFiles/model/model_test100.h5')
print "Model Saved"
print model.summary()

# Evaluate the model on CV Data
scores = model.evaluate(X_test, y_test, verbose=0)
print "%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)
