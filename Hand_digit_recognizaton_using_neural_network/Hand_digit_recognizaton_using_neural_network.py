#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


(X_train,Y_train),(X_test,Y_test)=keras.datasets.mnist.load_data()


# In[5]:


len(X_train)


# In[8]:


plt.matshow(X_train[0])


# In[42]:


X_train = X_train / 255.0
X_test = X_test / 255.0


# In[43]:


X_train[0]


# In[44]:


#scaling
x_train = X_train.reshape(len(X_train), 28*28)
x_test = X_test.reshape(len(X_test), 28*28)




# In[45]:


x_train[0]


# In[69]:


model = keras.Sequential([
    keras.layers.Dense(700, input_shape=(784,), activation='relu'), #here neuraon number=700
    keras.layers.Dense(10, activation='sigmoid') #here 10 last layer output number
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, Y_train, epochs=5)


# In[70]:


y_predict=model.predict(x_test)


# In[76]:


model.evaluate(x_train, Y_train)


# In[74]:


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
y_pred = model.predict(x_test)
y_pred_classes = y_pred.argmax(axis=1)

# Generate the confusion matrix
cm = confusion_matrix(Y_test, y_pred_classes)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
disp.plot(cmap=plt.cm.Blues)
plt.show()


# In[77]:


model.evaluate(x_test,Y_test)


# In[ ]:




