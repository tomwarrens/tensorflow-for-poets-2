# Documentation

This repo is forked from ["TensorFlow for poets 2" repo](https://github.com/googlecodelabs/tensorflow-for-poets-2).

Almost all the references made here are taken from ["TensorFlow for poets 2" codelab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2).


First: install TensorFlow for python3 [windows](https://www.tensorflow.org/install/install_windows) or
[macOS](https://www.tensorflow.org/install/install_mac).


# Inception Retrain

**Requirements:**

* python 3.5 ( or later)
* PIL
* tensorflow (1.0 or later)

## STEPs:

0) We consider as root of the project   `tensorflow-with-happiness2/`. To run a script you have to be inside the root with the prompt. Using `dir` (o  `ls` for Mac Users)  you should see the following direcories :
        a) `tf_files/`
        b) `scripts/`
        c) **file_convertion.py**
        d)Documentatu
        
1) Put the images divided into subfolders in the directory `tf_files/dataset/`
*Be Careful* the label's name will be the same as the subufolders that contained into the direcory `dataset/`

2) The model works with **jpg** images, if yours are not into desired format you should convert by running **file_convertion.py**. Be careful to change the name of the directories where are situated the pics inside the scripts  file_convertion.py.

    `python file_conversion.py (--dir) (--input_format=png) (--output_format=jpg)`
    
    Automatically the script convert all images inside the subfolder specified into *dir* option.
    If you need to convert a single folder easily is necessary to add the argoument *one_folder* = True
    
     `python file_conversion.py --dir=my/path/ --input_format=png --output_format=jpg --one_folder=True`
    

3) Check inside the folder `tf_files/` you should have the following direcotries:
        a)  `dataset/` where are situated the training and validation data (not splitted)
        b)  `models/` which cointains *Inception network*
        c)  `training_summaries/` where will be located the data for the tensorboard, at the moment is empty
        d)   `testing/` that's optional folder, where you have to put a subsample of pics where you wanna test your retrined model!
            The script that will be used to testing will come soon!
            
4) **Training:**
    From terminal run:
    
    `python -m scripts.retrain
    --bottleneck_dir=tf_files/bottlenecks
    --how_many_training_steps=500
    --model_dir=tf_files/models/
    --summaries_dir=tf_files/training_summaries/
    --output_graph=tf_files/retrained_graph.pb
    --output_labels=tf_files/retrained_labels.txt
    --image_dir=tf_files/dataset
    --print_misclassified_test_images`
    
    or
    
    
    `python retrain.py
    --bottleneck_dir=tf_files/bottlenecks
    --how_many_training_steps=500
    --model_dir=tf_files/models/
    --summaries_dir=tf_files/training_summaries/
    --output_graph=tf_files/retrained_graph.pb
    --output_labels=tf_files/retrained_labels.txt
    --image_dir=tf_files/dataset
    --print_misclassified_test_images`
    
5) **It's done! You have your own model!**


    
6) **Testing**
    You could test just a pic, by running (from root terminal)
    
    `python -m scripts.label_image
    --graph=tf_files/retrained_graph.pb
    --image=tf_files/testing/my-image-path/image_test.jpg`
    
    Or directly a folder and saving the prevision into a .txt file
    
        `python -m scripts.label_image
        --graph=tf_files/retrained_graph.pb
        --multiple_images=True
        --testing_directory=tf_files/testing/test_set/` > final_results.txt
        
At the end you will have all the prevision saved inside final_results.txt
        







