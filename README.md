# pdf-summarization
A REST API that summarizes a single-page PDF file that is built using Python Flask and OpenAI ChatGPT 3.5 for summarization.

## Installation

1. Clone the repository.
2. Install the dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment an environment variable for OpenAI API key:
   
   - Create a `.env` file in the root directory of the project.
   - Add the following line to the `.env` file:
   
   ```bash
    OPENAI_API_KEY=<your_openai_api_key>
    ```

## Usage

This API provides a single endpoint for summarizing a single-page PDF file.

### API Endpoint: `POST /summarize`
#### Request:
- Method: `POST`
- Content-Type: `form-data`
- Body: 
    - `file`: a `.pdf` file

This endpoint accepts a POST request with a PDF file and returns a summarized text extracted from the PDF using OpenAI's GPT-3.5 Turbo model.





### Running the Program


1. From a local environment

    ```bash
   flask --app app run --debug -p 5001
   ```

2. From docker

   ```bash
   docker build -t flask-app .
   docker run -p 5001:5001 flask-app
   ```