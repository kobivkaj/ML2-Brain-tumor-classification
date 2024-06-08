# ML-Projekt

# Brain Tumor Classification (MRI) Dataset

This repository contains the Brain Tumor Classification (MRI) dataset originally available on Kaggle.

### Download Images

You can download the data from the following sources:

#### Kaggle Datasets:
1. **First Dataset:**
   - [Brain Tumor Classification (MRI)](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)

2. **Additional Data:**
   - [Brain Tumor Detection](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection?select=no)
   - [Brain Tumor MRI Image Classification](https://www.kaggle.com/datasets/iashiqul/brain-tumor-mri-image-classification/data)

#### Google Drive:
1. **First Data:**
   - [Download Link](https://drive.google.com/drive/folders/1L1N_F4S0OcnyhXKY4PK5vSyI6SvmMdB9?usp=sharing)

2. **Combined Data:**
   - [Download Link](https://drive.google.com/drive/folders/1LZliDGpo7wjKdoFt90hny4DwsR5XXBo0?usp=share_link)

#### Instructions
You can open the file MRI_Brain_Tumor.ipynb in Google Colab or use this [link](https://colab.research.google.com/drive/1vkfnGmyXDY02GhqtHJPt5MOrHkm1y-3H?usp=sharing).

If you are using this project on your device, follow these steps:
- Create pyenv:
  - Install Python 3.12.3 with `pyenv install 3.12.3`
  - Create a virtual environment with `pyenv virtualenv 3.12.3 myenv`
  - Activate the virtual environment with `pyenv activate myenv`
- Open the file MRI_Brain_Tumor.ipynb and start with the exploration

#### Project structure
- The trained models can be found in the MRI_Brain_Tumor.ipynb 
- The combine_data.py is the script to combine the three datasets together
- The dataaugmentation.ipynb file contains the code used to generate more image data, which is also included in the MRI_Brain_Tumor.ipynb file