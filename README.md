Here i try to implement the <b> Hand_digit_recognizaton_using_neural_network.</b> <br />
For that i collect datasets form keras mnist data.<br />
Here i try to recognize from 0 to 9 number<br />
Step:<br />
 first i loaded data from keras<br />
 than i reshape them into 28*28<br />
 than i scaling them<br />
 then i trian them using relu and sigmoid activation function<br />
 Here i use 700 neuron for hidden layers,use  optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']  <br />
 also i check my result through the <b>confusin matrix </b> <br />
 Finally i evaluate the accouracy that is: <b> 0.9818000197410583 </b><br />
 $\textcolor{red}{Hand_digit_recognizaton_using_neural_network.}$
