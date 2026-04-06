# 🔍 SecureLens: AI-Powered Image Moderation System

SecureLens is a deep learning-based image moderation system designed to automatically classify images as **Safe (SFW)** or **Not Safe (NSFW)**.
It leverages computer vision and neural networks to assist in **content filtering and platform safety**.

---

## 🚀 Key Features

* 📤 Upload images through an interactive interface
* 🤖 AI-based classification (SFW vs NSFW)
* ⚡ Real-time prediction using a trained deep learning model
* 🖥 Built with Streamlit for a simple and clean UI
* 🔒 Simulates content moderation before posting

---

## 🧠 Model Architecture

* Model Type: Convolutional Neural Network (CNN)
* Base Model: MobileNetV2 (Transfer Learning)
* Input Size: 224 × 224 × 3
* Output Layer: Sigmoid activation
* Classification: Binary (SFW / NSFW)

---

## ⚙️ Tech Stack

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* PIL (Python Imaging Library)

---

## 📂 Project Structure

```
SecureLens/
│
├── app.py                           # Streamlit application
├── securelens_model_training.ipynb  # Model training notebook
├── requirements.txt                 # Dependencies
├── README.md                        # Project documentation
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/bhuvanaasankar24/SecureLens.git
cd SecureLens
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```

---

## 📊 Dataset

The dataset used for training is not included in this repository due to size limitations.

The model was trained on a binary image classification dataset containing:

* SFW (Safe images)
* NSFW (Unsafe / sensitive images)

You can use publicly available datasets from platforms like Kaggle or create your own curated dataset.

---

## ⚠️ Model File

The trained model file (`.h5`) is not included due to GitHub file size restrictions.
You can generate the model by running the training notebook.

---

## 💡 Future Enhancements

* 🌐 Deploy as a live web application
* 📊 Add confidence score visualization
* 🎥 Extend to video moderation
* 🧠 Improve accuracy with larger datasets
* 🔍 Add explainability (Grad-CAM / heatmaps)

---

## 🎯 Use Cases

* Social media content moderation
* AI-based filtering systems
* Safety checks before content upload
* Research in computer vision & ethics

---

## 👩‍💻 Author

**Bhuvaneshwari S**

LinkedIn - www.linkedin.com/in/bhuvana-sankar,

Mail - bhuvanaasankar241@gmail.com

---

This project is for educational purposes. You can use and modify it freely.

## ⭐ If you found this useful
Give this repo a ⭐ and support the project!
