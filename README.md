# ACSE 4.4 - Machine Learning Miniproject
# The Identification Game
Team members: Rory Johnston , Jorge Garcia, Yaqi Li, Lingaona Zhu, Zijian Wang, Yuling Li

Week long investigation of different neural network architectures to classify 64x64 images (similar to Tiny Imagenet) over 200 categories. Our top 2 performing architectures were:

- WRESNET50: Scored an **F1 score of 79.2%** on the test set. 
- Ensemble of WRESNET50, RESNET18, RESNET152 and DENSENET121: Scored an **F1 score of 74.6%** on the tests set. 


# Repository structure

- models: Contains the 3 of the 4 notebooks used to generate our most accurate classifications: RESNET18, RESNET152 and DENSENET121 (WRESNET50 is contained in the root directory, as "Entropy_Training_W_RESNET50_min_AUG_SGD.ipynb).

- submit: Contains the two .csv files from our top-2 submissions. 

- Entropy_Training_W_RESNET50_min_AUG_SGD.ipynb: Notebook containing our most accurate submission (79.2%).

- Ensemble.ipynb: Notebook containing our 2nd most accurate submission (74.6%). **Note that this notebook takes .pt files which are not stored on Github due to file size limitations. You can find them here (and must put them inside the "models" folder): https://drive.google.com/drive/folders/1YrGILfJNM9X2ZDbdWwWXbCMeqdxn6HKn?usp=sharing**  

- mapping.json:	Provides mappings.	

- mapping.py: Wrapper to load and provide mappings. 

# Additional information 

All information about this Kaggle challenge is available here: https://www.kaggle.com/c/acse-miniproject/overview
