# 🐔 Henalyze(Poultry disease classifier)

A Deep Learning-based image classification system to identify poultry diseases using chicken images. This project uses a Convolutional Neural Network (CNN) architecture based on **VGG16**, trained to distinguish between healthy and diseased chickens. It also includes an end-to-end CI/CD pipeline with Docker, GitHub Actions, AWS ECR, and EC2 for deployment.

---

## 📌 Project Highlights

- 🔍 **Problem**: Identify diseases in chickens based on image input.
- 🧠 **Model Used**: Transfer Learning with **VGG16**.
- 📦 **Frameworks**: TensorFlow, Keras, Flask.
- 🐍 **Language**: Python
- 🐳 **Deployment Stack**: Docker, AWS ECR, EC2, GitHub Actions.

---

## 📈 Model Performance

| Metric    | Value     |
|-----------|-----------|
| Accuracy  | 90.51%    |
| Loss      | 0.6722    |

---

## 🛠️ How to Run Locally

### STEP 1: Clone the repository

```bash
git clone https://github.com/yashdive/poultry-disease-classifier
cd Poultry-Disease-Classfier
```

### STEP 2: Create a conda environment

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### STEP 3: Install the requirements

```bash
pip install -r requirements.txt
```

### STEP 4: Run the application

```bash
python app.py
```

Then open your browser and go to:

```bash
http://localhost:5000
```

---

## 📦 DVC Commands (If using Data Version Control)

```bash
dvc init
dvc repro
dvc dag
```

---

## 🚀 CI/CD Deployment on AWS with GitHub Actions

This project uses a production-grade CI/CD pipeline to automate deployment to AWS EC2 using Docker and ECR.

### Step-by-Step Pipeline

1. ✅ **Login to AWS Console**
2. 🔑 **Create IAM User** with:
   - `AmazonEC2ContainerRegistryFullAccess`
   - `AmazonEC2FullAccess`

3. 📦 **Create an ECR Repository**  
   Save the URI for Docker image (e.g.):
   ```
   566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
   ```

4. 🖥️ **Launch EC2 Instance** (Ubuntu)

5. 🐳 **Install Docker in EC2**
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

6. 🏃‍♂️ **Configure EC2 as GitHub Self-hosted Runner**
- Go to `GitHub > Settings > Actions > Runners > New self-hosted runner`
- Follow the steps and run commands on EC2

7. 🔐 **Add GitHub Secrets** (in repo settings):
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME=chicken
```

---

## 📌 Summary of What I Did

- Built a poultry disease classification model using transfer learning with VGG16.
- Achieved high accuracy of 90%+ on the validation dataset.
- Built a web app using Flask to serve model predictions.
- Containerized the application with Docker.
- Automated the full deployment pipeline using GitHub Actions, ECR, and EC2.
- Set up a self-hosted GitHub Runner on EC2 to handle builds securely without costs during idle.

---

## 🔒 Deployment Note

The EC2 and ECR resources were deleted after deployment to avoid ongoing AWS charges. The app is not publicly hosted due to GPU/deep learning constraints. Local setup instructions are provided for offline testing.

---

## 📄 License

This project is licensed under [MIT License](LICENSE).
