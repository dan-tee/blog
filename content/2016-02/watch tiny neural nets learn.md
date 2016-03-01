Title: Watch Tiny Neural Nets Learn
Date: 2016-02-28 16:00
Modified: 2016-08-27 16:00
Category: Machine Learning
Tags: Machine Learning, Neural Nets, Keras, Introduction
Status: draft

Neural networks are often treated as black boxes. If we look at a tiny one, we can still understand
what's happening inside. In this post I'll show you some animations of a tiny neural net learning
to approximate a noisy sine function and we'll look inside to understand what is happening. I'll assume you
already know the very basics of neural nets in Keras, which you can read up on in my post
[First Steps With Neural Nets in Keras]({fileName}./first steps with neural nets in keras.md).

This is the training data for the tiny nets. It's a sine plus some normally distributed error.

{% notebook watch-tiny-neural-nets-learn.ipynb cells[0:1] %}

Let's first try a net with 1 hidden layer and 100 hidden neurons.

{% notebook watch-tiny-neural-nets-learn.ipynb cells[1:6] %}

This is how the predictions of the net look during each training iteration.

{% video /videos/tiny-sine-standard.mp4 400 300 /images/tiny-sine-standard.png %}

The net quickly learns the first hill of the sine function. This corresponds to the training error
decreasing rapidly during the first few iterations. Then it gets stuck in a local optimum. The
training error remains in the range fo 0.2 without any signs of improvement over the last 7000 iterations.

{% notebook watch-tiny-neural-nets-learn.ipynb cells[7:8] %}

{% video /videos/tiny-sine-tuned.mp4 400 300 /images/tiny-sine-tuned.png %}