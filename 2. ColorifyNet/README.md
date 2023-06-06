# ColorifyNet
This project is inspired by the colorization.py script from the OpenCV library. It provides a simple way to colorize black and white images using a pre-trained neural network.

## Description
The Colorization program allows users to colorize black and white images by leveraging a pre-trained neural network. The program takes a grayscale image as input and automatically applies colorization based on the neural network's predictions.

The colorization process involves the conversion of the input image from the RGB color space to the LAB color space. In this color space, the L channel represents the lightness of the image, while the A and B channels contain the color information. The neural network takes the L channel as input and generates predictions for the A and B channels.

The Colorization program utilizes a deep neural network that has been trained on a large dataset of colored images. The neural network has learned to capture and predict the color values for different grayscale pixels. By applying the learned colorization patterns, the program can accurately colorize black and white images.

## Example Application
This repository provides an example application that demonstrates the capabilities of the colorization functionality implemented:

![Capture](https://github.com/ShakalyaGarg/Foundations-of-ML/assets/129611852/ecf58da1-6041-4fc6-93e6-dd1c916f8da8)

## Usage
* Clone or download the repository to your local machine.
* Include the "Models" folder from the repository in your project folder to ensure the pretrained neural network is available for the script to work correctly.
* Install the required libraries mentioned in the "Requirements" section.
* Provide the path to the black and white image you want to colorize by updating the image_path variable in the script.
* Execute the script and wait for the colorization process to complete.
* Once the process is finished, two windows will pop up: one displaying the original black and white image and another showing the colorized version.

Please note that for the script to function properly, it is important to include the "Models" folder in your project directory. This folder contains the pretrained neural network that is utilized by the application for colorization.

Respective files for Models floder can be found in the following link:
https://drive.google.com/drive/folders/1FaDajjtAsntF_Sw5gqF0WyakviA5l8-a

## Requirements
The following libraries are required to run the Colorization program:
* numpy
* cv2 (OpenCV)

## Repository Structure
The repository is structured as follows:

* ***colorization.py***: The main Python script that performs the colorization.
* Models: Directory containing the pre-trained model files.
    * ***colorization_deploy_v2.prototxt***: Model architecture file.
    * ***colorization_release_v2.caffemodel***: Model weights file.
    * ***pts_in_hull.npy***: File containing the kernel points used for colorization.
* Images: Directory containing sample black and white images for testing.
    * Lion_King.jpg: Sample black and white image.
