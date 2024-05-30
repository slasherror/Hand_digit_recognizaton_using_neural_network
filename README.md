Here i try to implement the Hand_digit_recognizaton_using_neural_network.
For that i collect datasets form keras mnist data.
Here i try to recognize from 0 to 9 number
Step:
 first i loaded data from keras
 than i reshape them into 28*28
 than i scaling them
 then i trian them using relu and sigmoid activation function
 Here i use 700 neuron for hidden layers,use  optimizer='adam',
 loss='sparse_categorical_crossentropy', metrics=['accuracy']
 also i check my result through the confusin matrix
 Finally i evaluate the accouracy that is:0.9818000197410583
