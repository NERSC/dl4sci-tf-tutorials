# DL4Sci School TensorFlow tutorials

This repository contains the hands-on introductory deep learning tutorial examples for the
Deep Learning for Science school at Berkeley Lab: https://dl4sci-school.lbl.gov/

These jupyter notebooks come from the official TensorFlow 2.0 tutorials at
https://www.tensorflow.org/beta.

We made minor updates so attendees could run them on Cori GPU without modification.

## Contents

* [Setup on Cori GPU](https://github.com/NERSC/dl4sci-tf-tutorials#getting-setup-on-cori-gpu)
* [Setup on Collab](https://github.com/NERSC/dl4sci-tf-tutorials#running-on-collab)
* [Introductory examples](https://github.com/NERSC/dl4sci-tf-tutorials#introductory-hands-on-notebooks)
* [Advanced examples](https://github.com/NERSC/dl4sci-tf-tutorials#optional-advanced-notebooks)

## Getting setup on Cori GPU

Open https://jupyter-dl.nersc.gov/ and log in with your training account
credentials.

Start a terminal by scrolling to the bottom of the Launcher window and clicking
the `Terminal` button under `Other`.

Using the terminal, clone this repository to download all of the tutorial
notebooks:

`git clone https://github.com/NERSC/dl4sci-tf-tutorials.git`

Now you can use the Jupyter file browser to navigate the repository and launch
notebooks.

You can test that things are working on a Cori GPU node by running the
[Test.ipynb](Test.ipynb) notebook.

## Running on Collab

If you have issues with Cori GPU or if you simply prefer you can run these
examples in the cloud on Google's Collab service. Simply go to the TF webpage
for the specific example (links below) and click `Run in Google Collab`.
Note that you may not get access to a GPU on Collab, but the TF tutorials are
designed to execute quickly regardless.

## Introductory hands-on notebooks

For a good introduction to implementing models in TensorFlow using the recommended
Keras API, we recommend working through at least the first few examples below.

The overfitting/underfitting and save/restore examples also demonstrate very
practical use-cases that you may want to work through.

Finally, depending on time, you can also try out the advanced examples according
to your preference.

For each example, see if you can successfully modify the code and take note of how results change.

### Basic classification

[basic_classification.ipynb](basic_classification.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/basic_classification

Quiz questions:
1. Why did we divide the image data by 255?
2. Which activation function did we use for our hidden layer of the network? Could we have used a different one?
3. Which activation function did we use for the output layer of the network? Could we have used a different one?

Challenges:
1. Try to modify the network architecture by adding/removing layers, changing the size of the layers, etc.
2. Try changing the optimizer algorithm; can you figure out how to modify the default *learning rate*?
3. See if you can improve the test set accuracy. How good of a model can you train?


### Convolutional neural networks

[intro_to_cnns.ipynb](intro_to_cnns.ipynb)

https://www.tensorflow.org/beta/tutorials/images/intro_to_cnns

This example is similar to the previous one but demonstrates how to setup CNNs so is valuable to work through as well.

Quiz questons:
1. What benefit do we get from using max-pooling in our network?
2. Why do we add the dense layers only at the end?
3. Does the model converge with the specified settings?

Challenges:
1. Try to modify the network architecture: the number of layers, the number of filters in the layers, the sizes of the filters, etc.
2. What's the best test accuracy you can achieve?

### Classify structured data

[feature_columns.ipynb](feature_columns.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/feature_columns

Quiz questions:
1. This tutorial is just meant to teach you some mechanics and doesn't give an impressive result. What are some of the reasons why this model under-performs?
2. What are the situations in which you should consider using embedding or hashed-feature columns? Can you think of a good use-case for bucketized features?

### Overfitting and underfitting

[overfit_and_underfit.ipynb](overfit_and_underfit.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/overfit_and_underfit

Quiz questions:
1. Try to summarize how you diagnose under- and overfitting.
2. If your model is overfitting, what is the most ideal way to improve it?
3. How can you fix under-fitting?

Challenge:
1. All the models in this example are overfitting. Can you build a model that underfits?

### Saving and restoring models

[save_and_restore_models.ipynb](save_and_restore_models.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/save_and_restore_models

## Optional advanced notebooks

### Defining custom layers

[custom_layers.ipynb](custom_layers.ipynb)

https://www.tensorflow.org/beta/tutorials/eager/custom_layers

### Loading and preprocessing images

[images.ipynb](images.ipynb)

https://www.tensorflow.org/beta/tutorials/load_data/images

### Deep Convolutional Generative Adversarial Networks (DCGAN)

[dcgan.ipynb](dcgan.ipynb)

https://www.tensorflow.org/beta/tutorials/generative/dcgan

### Variational auto-encoders (VAE)

[cvae.ipynb](cvae.ipynb)

https://www.tensorflow.org/beta/tutorials/generative/cvae

### Image to image translation with CycleGAN

[cyclegan.ipynb](cyclegan.ipynb)

https://www.tensorflow.org/beta/tutorials/generative/cyclegan

**Note**: I didn't have time to install tensorflow-examples, so this is done in the notebook.
You will have to restart the kernel after running the `pip install` cell to pick up the new library.

### Transformers for language understanding

[transformer.ipynb](transformer.ipynb)

https://www.tensorflow.org/beta/tutorials/text/transformer

### Image captioning

[image_captioning.ipynb](image_captioning.ipynb)

https://www.tensorflow.org/beta/tutorials/text/image_captioning

This example takes quite a while to run. It uses a fairly slow feature caching method, and the model training has poor GPU utilization and takes a while.

## TensorBoard

If you'd like to try TensorBoard in Jupyter, you can take a look at the example
code in [test_tensorboard.ipynb](test_tensorboard.ipynb). See if you can get
TensorBoard working with one of the example notebooks!
