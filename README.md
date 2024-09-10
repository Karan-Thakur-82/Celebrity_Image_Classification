# Here’s an in-depth description for your **Celebrity Image Classification** project to use on GitHub:

---

# Celebrity Image Classification

## Overview

**Celebrity Image Classification** is a machine learning project designed to classify images of famous athletes using face and eye detection algorithms combined with a web-based interface. This system is built to identify one of five pre-selected celebrity athletes: **Lionel Messi**, **Maria Sharapova**, **Roger Federer**, **Serena Williams**, and **Virat Kohli**. The project utilizes **OpenCV** for image detection and **scikit-learn** for model training and classification, making it a powerful tool for real-time image recognition.

The web interface allows users to upload an image, which the system processes to classify the celebrity based on the trained model. The system also provides a similarity probability table, showcasing the percentage match for each of the five athletes. If the image does not meet the detection criteria, it returns a message indicating the failure to detect the face or eyes.

## Features

### 1. **Face & Eye Detection with OpenCV**
   The system uses **OpenCV's Haarcascade** algorithm to accurately detect faces and eyes in the uploaded image. The detection ensures that only images with visible faces and eyes are processed, improving the reliability of classification.

### 2. **Image Processing with Wavelet Transforms**
   **2D Wavelet Transforms** are applied to each image to enhance key features that help the classification models distinguish between the different celebrities.

### 3. **Machine Learning Models**
   Multiple machine learning models, including **Support Vector Machine (SVM)**, **Random Forest**, and **Logistic Regression**, have been trained on a carefully curated dataset of celebrity images. These models provide high accuracy and speed in classifying the correct athlete.

### 4. **Probability Table of Celebrity Matches**
   After classifying the image, the system outputs a probability table that ranks each of the five athletes by the percentage likelihood that they match the input image.

### 5. **Web Interface with Flask**
   A user-friendly web interface built using **Flask** allows users to easily drag and drop images for classification. The interface is simple yet effective, providing quick feedback and classification results in real time.

### 6. **Error Handling for Image Quality**
   If the system detects an unclear image (e.g., if the face or eyes are not visible), it returns a message: **"Can't classify image. Classifier was not able to detect face and two eyes properly"**, guiding the user to upload a clearer image.

## Technical Stack

### 1. **Backend**
   - **Python**: The core programming language used for all backend operations, including image processing, model training, and classification logic.
   - **OpenCV**: Used for face and eye detection, ensuring that the image being classified meets the necessary criteria.
   - **Scikit-learn**: Provides the framework for training and applying machine learning models such as SVM, Random Forest, and Logistic Regression.

### 2. **Frontend**
   - **HTML/CSS/JavaScript**: Frontend technologies used to create the web interface, enabling drag-and-drop image uploading and displaying the classification results.

### 3. **Web Framework**
   - **Flask**: A lightweight web framework that serves the frontend, handles user image uploads, and passes data to the machine learning models for classification.

## Workflow

1. **Data Collection**: 
   - A dataset of celebrity images was compiled, focusing on five athletes (Messi, Sharapova, Federer, Williams, Kohli) with images that had clear, detectable faces and eyes.
  
2. **Preprocessing**: 
   - The images were cleaned and cropped, and **2D Wavelet Transforms** were applied to enhance features for better classification.
   
3. **Model Training**: 
   - The dataset was split into training and test sets, and three machine learning models (SVM, Random Forest, Logistic Regression) were trained to classify the images.
   
4. **Web Interface Development**: 
   - A **Flask** application was built to provide a simple and intuitive drag-and-drop feature, allowing users to upload an image for classification.

5. **Classification**: 
   - The backend processes the uploaded image, detects the face and eyes, applies wavelet transforms, and uses the trained models to classify the image as one of the five athletes.
   
6. **Result Output**: 
   - The celebrity’s name is displayed, along with a probability table showing similarity percentages for all five celebrities.

7. **Error Handling**: 
   - If no face or eyes are detected, the system responds with an error message prompting the user to upload a clearer image.

## Future Work
- Expanding the celebrity dataset to include more athletes or even celebrities from other fields like actors, musicians, etc.
- Improving model accuracy through deeper learning methods (e.g., Convolutional Neural Networks).
- Adding support for multi-image classification and batch processing.

## Conclusion
This project demonstrates how **machine learning**, **image processing**, and **web development** can be combined to create a powerful and engaging web-based image recognition system. The use of face and eye detection, along with multiple machine learning models, ensures reliable classification, while the user-friendly Flask-based interface makes it easy for anyone to upload and classify images.
