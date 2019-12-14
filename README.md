# Flask-CIFAR-10
This project consists of taking a trained model, specifically image classification with the cifar-10 dataset, and using it in a Flask application for testing and learning purposes.

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

you can read more about by [clicking here](https://www.cs.toronto.edu/~kriz/cifar.html)

I followed [this tutorial](https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/
) to learn how to create the model

#Results

![Screenshot_2019-12-13 CIFAR-10 Browser Test](https://user-images.githubusercontent.com/13570164/70841541-09b35a80-1dfa-11ea-8909-01d57f98b9fa.png)

My main goal was to just train the model, export and integrate with a flask application, but I could see that the classification presented problems when using a high resolution images.


