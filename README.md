# AI Food Calorie Estimator

An offline-capable AI system that detects food from images, estimates calories, and features a chatbot interface to interact with the nutritional data.

## Setup & Running

This project uses Python. A virtual environment has been created and dependencies should be installed.

To run the application:

1. Open your terminal in this project directory (`c:/Users/prach/OneDrive/Desktop/project`).
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Features
- **Image Input**: Upload an image or take a photo using your camera.
- **AI Detection**: Uses HuggingFace `transformers` (nateraw/food) to detect and classify the food.
- **Calorie Estimation**: Cross-references detected food with a local CSV database to estimate calories and macros.
- **Chatbot**: An integrated nutrition chatbot that uses the image context to answer your questions about the food.
