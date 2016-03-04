Title: Watch Tiny Neural Nets Learn
Date: 2016-03-01 23:30
Modified: 2016-03-04 20:00
Category: Machine Learning
Tags: Machine Learning, Neural Nets, Keras, Introduction
Summary: In this post I'll show you some animations of tiny neural nets learning. Finding the right neural net for a
         given problem needs experience and experimentation. I'll show you the steps and missteps it took me to find
         a good net to predict a noisy sine function.

In this post I'll show you some animations of tiny neural nets learning. Finding the right neural net for a
given problem needs experience and experimentation. I'll show you the steps and missteps it took me to find
a good net to predict a noisy sine function.

I'll assume you already know the very basics of neural nets in Keras, which you can read up on in my post
[First Steps With Neural Nets in Keras]({filename}../2016q1/first steps with neural nets in keras.md).

This is the training data for the tiny nets. It's a sine plus some normally distributed error.

{% notebook 2016q1/watch-tiny-neural-nets-learn.ipynb cells[0:1] %}

Let's first try a net with 1 layer of 60 neurons. The model has 120 parameters. The 60 weights
from the input to the 60 neurons and the 60 weights form the neurons to the output.

{% notebook 2016q1/watch-tiny-neural-nets-learn.ipynb cells[1:6] %}

This is how the predictions of the net look during each training iteration.

{% video /videos/2016q1/tiny-sine-one-layer.mp4 400 300 /images/2016q1/tiny-sine-one-layer.png %}

The net quickly learns the first hill of the sine function. This corresponds to the training error
decreasing rapidly during the first few iterations. Then it gets stuck in a local optimum. The
training error remains in the range fo 0.2 without any signs of improvement over the last 17000 iterations.

Let's try another configuration of the net. Let's have two layers of 10 neurons each. This net has again 120
parameters. The 10 weights from the input to the first 10 neurons, the weights for the 100 connections
from the first 10 to the second 10 neurons and the 10 from the second neurons to the output.

{% notebook 2016q1/watch-tiny-neural-nets-learn.ipynb cells[7:8] %}

{% video /videos/2016q1/tiny-sine-two-layer.mp4 400 300 /images/2016q1/tiny-sine-two-layer.png %}

This looks better. But the way the training error improved looks like it could have gotten stuck again.
As it looks like a problem of a local optimum, let's try using a different optimizer. A reommended optimizer
is `Adam`. You can find a readable explanation and the recommendation in
[this Stanford lecture](http://cs231n.github.io/neural-networks-3/#ada).

{% notebook 2016q1/watch-tiny-neural-nets-learn.ipynb cells[9:10] %}

{% video /videos/2016q1/tiny-sine-one-layer-adam.mp4 400 300 /images/2016q1/tiny-sine-one-layer-adam.png %}

This time we see steady decrease in the training error. And the final prediction looks close to optimal.
A 2-layer network worked better before, let's see how the 2 layers work with the new optimizer.

{% notebook 2016q1/watch-tiny-neural-nets-learn.ipynb cells[11:12] %}

{% video /videos/2016q1/tiny-sine-two-layer-adam.mp4 400 300 /images/2016q1/tiny-sine-two-layer-adam.png %}

Pretty much the same picture here. In this example the choice of optimizer was more important than the number of
layers. Keep in mind that this was only a simple example to illustrate some properties of neural nets. They really
start to shine in more complex tasks like image or text recognition.