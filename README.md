# DL4Sci School TensorFlow tutorials

This repository contains the hands-on introductory deep learning tutorial examples for the
Deep Learning for Science school at Berkeley Lab: https://dl4sci-school.lbl.gov/

These jupyter notebooks come from the official TensorFlow 2.0 tutorials at
https://www.tensorflow.org/beta.

We made minor updates so attendees could run them on Cori GPU without modification.

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

Finally, depending on time, you can also try out the advanced examples.

For each example, see if you can successfully modify the code and take note of how results change.

### Basic classification

[basic_classification.ipynb](basic_classification.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/basic_classification

### Classify structured data

[feature_columns.ipynb](feature_columns.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/feature_columns

### Convolutional neural networks

[intro_to_cnns.ipynb](intro_to_cnns.ipynb)

https://www.tensorflow.org/beta/tutorials/images/intro_to_cnns

### Overfitting and underfitting

[overfit_and_underfit.ipynb](overfit_and_underfit.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/overfit_and_underfit

### Saving and restoring models

[save_and_restore_models.ipynb](save_and_restore_models.ipynb)

https://www.tensorflow.org/beta/tutorials/keras/save_and_restore_models

## Optional advanced notebooks

### Defining custom layers

[custom_layers.ipynb](custom_layers.ipynb)

https://www.tensorflow.org/beta/tutorials/eager/custom_layers

### DCGAN

[dcgan.ipynb](dcgan.ipynb)

https://www.tensorflow.org/beta/tutorials/generative/dcgan

### VAE

[cvae.ipynb](cvae.ipynb)

https://www.tensorflow.org/beta/tutorials/generative/cvae

### Loading and preprocessing images

[images.ipynb](images.ipynb)

https://www.tensorflow.org/beta/tutorials/load_data/images

### Transformer

[transformer.ipynb](transformer.ipynb)

https://www.tensorflow.org/beta/tutorials/text/transformer

### Image captioning

[image_captioning.ipynb](image_captioning.ipynb)

https://www.tensorflow.org/beta/tutorials/text/image_captioning

## TensorBoard

If you'd like to try TensorBoard in Jupyter, you can take a look at the example
code in [test_tensorboard.ipynb](test_tensorboard.ipynb). See if you can get
TensorBoard working with one of the example notebooks!