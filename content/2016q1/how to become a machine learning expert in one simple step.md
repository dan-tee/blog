Title: How To Become A Machine Learning Expert In One Simple Step
Date: 2016-03-20 15:00
Modified: 2016-03-20 15:00
Category: Machine Learning
Tags: Kaggle, Machine Learning, Data Science


The web is full of good explanations of machine learning algorithms. And every second applicant for a
data science position has finished the
[Coursera course on machine learning](https://www.coursera.org/learn/machine-learning).
While it is important to understand the concepts behind the algorithms,
one thing is even more important:

>You need to learn how to **apply** machine learning algorithms

Theory will not help you choose good values for the 16 parameters a standard
implementation of a random forest takes. The default values are good to get started, but which parameters
should you modify depending on your data?

{% img ../../images/2016q1/engineer.jpg 500 %}

Choosing the right features, algorithms and parameters is an art. It's actually more like Karate than
like math. You won't learn it from a book. You learn it by doing, by getting your hands dirty and
applying algorithms to various data sets. By lots of trial and error. By having seen hundreds of successful
applications.

Take the people winning [Kaggle competitions](http://kaggle.com)[^2], for example. One might think they
are the researchers leading in the field of machine learning. But in fact, most of them
spent a lot of time on Kaggle working with actual data. Check by yourself. Kaggle publishes
[profiles of top kagglers](http://blog.kaggle.com/tag/profiling-top-kagglers/) on their blog.

[^2]: [Kaggle](http://kaggle.com) is the largest site hosting machine learning competitions. Companies
publish their data and everybody can compete to make the best prediction from this data.

To get better at applying machine learning techniques, here is the one simple step I recommend. While it is simple
as a concept, it will (of course) take perseverance and many hours of work.

> Participate in Kaggle competitions.

It is easy to get this one wrong though. The prize money and the leaderboard could easily
make you think, it is about winning kaggle competitions. The inglorious truth is, winning is a distraction.
Winning a data science competition needs skills that are not relevant to a data science job.
You need to build overly complex models and squeeze out the last fractions of a
percentage point. Even the winning model of the Netflix prize
[has not been used in practice](http://techblog.netflix.com/2012/04/netflix-recommendations-beyond-5-stars.html).

What makes Kaggle such a great resource for learning is the access to various complex data sets combined with
benchmarks on the leaderboard. The leaderboard will give you an outlook on what’s possible and helps you to put
your model into perspective. This is such a great opportunity. In many machine learning applications it’s hard
to tell if the data allows for better predictions.

{% img ../../images/2016q1/kaggle.png 700 %}

Another great way to learn on Kaggle is to study [winning solutions](https://github.com/dmlc/xgboost/blob/master/demo/README.md#machine-learning-challenge-winning-solutions).
Don’t get scared by their complexity. You
can ignore the stacking of hundreds of models and still learn important tricks from them. Whenever you are stuck
on a particular data set you can visit the Kaggle Forum where others share loads of knowledge.

Personally, I try to build simple models that still come close to the leaderboard: not necessarily in rank,
but in prediction error. I usually join competitions where the features have a description. This
is closer to reality. And in most business applications feature engineering is more important than
your machine learning model.

My chances of winning prize money are as small as in a lottery. Still the money somehow motivates me.
[Prospect theory](https://en.wikipedia.org/wiki/Prospect_theory) gives a
possible explanation. Our brains are not wired to understand infinitesimal probability. We just see winning as a
possibility and dream of the reward. It's great that we can trick us into doing something so useful.

John Foreman wrote a great [blog post](http://analyticsmadeskeezy.com/2012/11/05/check-yo-self-5-things-you-should-know-about-data-science-author-note/)
to put things into perspective. In a job you have to deliver value to the business. This involves many skills
other than machine learning. For example, finding simple models that have enough predictive power,
telling the signal from the noise and marketing your ideas to the rest of the company.

Just to avoid confusion: Kaggle is the best place to advance you practical machine learning skills.
I’m not saying this is all you need to be a good data scientist.
