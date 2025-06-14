---
title: Visionary Verse
emoji: ✒️
colorFrom: green
colorTo: blue
sdk: docker
app_port: 8000
readiness_check:
  path: /health
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

---

# Visionary Verse ✒️

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://ekocak-visionary-verse.hf.space)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

An AI-powered service that generates creative fantasy stories inspired by an uploaded image. This project demonstrates an end-to-end MLOps workflow, from development and containerization to automated deployment.

---

### **Live Demo**

You can try the live application hosted on Hugging Face Spaces:

**➡️ [https://ekocak-visionary-verse.hf.space/docs](https://ekocak-visionary-verse.hf.space/docs)**

*(Note: The application is hosted on a free tier and may go to sleep. The first request might take a moment to wake it up and load the models.)*

### **Features**

-   **Multi-Modal Input:** Takes an image as input.
-   **Image Understanding:** Leverages a pre-trained Vision-Transformer model (`microsoft/git-large-coco`) to generate a descriptive caption for the image.
-   **Creative Text Generation:** Uses the caption as a prompt for a generative language model (`gpt2`) to create a unique short story.
-   **API-First Design:** A robust backend built with FastAPI, serving the AI model through a clean REST API.
-   **Containerized & Reproducible:** The entire application and its dependencies are containerized with Docker, ensuring it runs consistently in any environment.
-   **Automated CI/CD:** A GitHub Actions workflow automates the process of building the Docker image and pushing it to a registry upon changes to the `main` branch.

### **Tech Stack & Architecture**

-   **AI & Machine Learning:** PyTorch, Transformers (Hugging Face)
-   **Backend:** Python 3.9, FastAPI, Uvicorn
-   **DevOps & Deployment:** Docker, GitHub Actions (CI), Hugging Face Spaces (CD)

### **How to Run Locally**

To run this project on your local machine, ensure you have **Docker** installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ekocak02/visionary-verse.git](https://github.com/ekocak02/visionary-verse.git)
    cd visionary-verse
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t visionary-verse .
    ```

3.  **Run the Docker container:**
    ```bash
    # To run on CPU
    docker run --rm -p 8000:8000 visionary-verse

    # To run with NVIDIA GPU access (if available)
    # docker run --rm -p 8000:8000 --gpus all visionary-verse
    ```

4.  **Access the API:**
    -   Open your web browser and go to **`http://127.0.0.1:8000/docs`**.
    -   Use the interactive Swagger UI to upload an image and test the `/generate` endpoint.

### **API Endpoint**

#### `POST /generate`

-   **Description:** Uploads an image and returns a generated story.
-   **Request Body:** `multipart/form-data` containing the image file.
-   **Successful Response (`200 OK`):**
    ```json
    {
      "input_image_filename": "example.jpg",
      "generated_caption": "a cat sitting on a mountain top",
      "generated_story": "A fantasy adventure set in a land that once was a cat sitting on a mountain top: The feline, known as..."
    }
    ```
