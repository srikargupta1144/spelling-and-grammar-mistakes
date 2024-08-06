# Spelling & Grammar Mistakes Correction App

This project demonstrates how to deploy a Streamlit-based spelling and grammar mistakes correction app using `language_tool_python` in a Docker container.

## Prerequisites

- Docker Desktop installed
- Virtualization enabled in BIOS settings
- Hyper-V installed and enabled on Windows

## Setup Instructions

### Local Development

1. **Clone the Repository**: 
   ```bash
   git clone spelling-and-grammar-mistakes
   cd spelling-and-grammar-mistakes

2. **Create Virtual Environment**:
   ```bash
   python -m venv new_env
   new_env\Scripts\activate  # For Windows
   source new_env/bin/activate  # For Unix-based systems

3. **Install Dependencies**:
   ```bash
   pip install streamlit language_tool_python

4. **Run the App Locally**:
   ```bash
   streamlit run app.py

### Docker Deployment

1. **Create a Dockerfile**:
   ```dockerfile
   FROM python:3.11-slim

   COPY . /app
   WORKDIR /app

   # Install Python dependencies
   RUN pip3 install -r requirements.txt

   #entrypoint
   ENTRYPOINT ["streamlit", "run"]

   CMD ["app.py"]


2. **Build Docker Image**:
   ```bash
   docker build -t textcorrectionimg .

3. **Run Docker Image**:
   ```bash
   docker run -p 8501:8501 textcorrectionimg

4. **Login to Docker Hub**:
   ```bash
   docker login

5. **Push Docker Image to Docker Hub**:
   ```bash
   docker tag textcorrectionimg srikargupta1144/textcorrection:1.0
   docker push srikargupta1144/textcorrection:1.0

6. **Pull Docker Image from Docker Hub**:
   ```bash
   docker pull srikargupta1144/textcorrection:1.0
   docker run -p 8501:8501 srikargupta1144/textcorrection:1.0

## Using the App

1. **Navigate to the App**: Open your browser and go to `http://localhost:8501`.
2. **Enter Text**: Enter the text (up to 500 words) in the text area.
3. **Correct Mistakes**: Click the "Correct Mistakes" button to see the corrected text.
