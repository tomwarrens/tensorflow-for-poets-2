# Overview

This repo is forked from ["TensorFlow for poets 2" repo](https://github.com/googlecodelabs/tensorflow-for-poets-2).

Almost all the references made here are taken from ["TensorFlow for poets 2" codelab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2).

First: install TensorFlow for python3 [windows](https://www.tensorflow.org/install/install_windows) or
[macOS](https://www.tensorflow.org/install/install_mac).

There are both CPU and GPU versions.

After having cloned the repository and placed yourself 
inside it, save your training files (**jpg**) in tf_files this way:

* Dataset
    * Car
        * image1.jpg
        * image2.jpg
    * noCar
        * imageA.jpg
        * imageB.jpg

This way when you compute `dir tf_files/Dataset` from
windows prompt (`ls tf_files/Dataset` when working with Unix) you
should get: 

`Car/` 

`noCar/`

***File format to jpg:***

I created a script *file_conversion.py* that converts any
input format to desired output format (in this case .jpg). 

It runs like this: 

`python file_conversion.py (--directory) (--input_format=png) (--output_format=jpg)`

All command line arguments have default values, for now
the script converts the file if classes are Car and noCar, please feel free to change the code for any class you need. 


***Setting parameters for transfer learning:***

It's rather easy from now on. 

**Training:**

In the terminal 

`python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/ \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --image_dir=tf_files/dataset \
  --print_misclassified_test_images=True`

*Parameters (the ones needed)*:

* --bottleneck_dir = directory where we save the feature map representation for each image
* --how_many_training_steps = how many times I train batch_size instances in training set
* --output_graph = **where to save in .pb format the retrained network**
* --flip_left_right = Whether to randomly flip half of the training images horizontally
* --model_dir=tf_files/models/ = the directory where we find the network 

In retrain.py you find all the parameters you can set. 

**Testing:**

In the terminal 

`python -m scripts.label_image 
--graph=tf_files/retrained_graph.pb 
--image=tf_files/dataset/Car/trial.jpg
--multiple_images=True
--testing_directory=tf_files/testing_dataset`