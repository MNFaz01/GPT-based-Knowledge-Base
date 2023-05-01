# Question-Answer with your own data using OpenAI GenAI Models

This project provides two Python scripts that allow you to ask questions and receive answers from PDF documents. The app uses the langchain library to perform natural language processing tasks such as text splitting, embeddings, and question answering.

The first script, `single_pdf_reader.py`, reads data from a single PDF file defined in a .env file. It uses FAISS as the vector database and manually does document chunking, embedding, and adding the relevant data to the vector database. The script downloads embeddings from OpenAI and creates a chain to answer questions.

The second script, `multiple_pdf_reader.py`, reads data from multiple PDF files. It uses Chromadb as the vector database and VectorstoreIndexCreator(), which does everything itself, like document chunking, embedding, and adding embedding and text to the vector database.

Both scripts use the langchain library to perform various NLP tasks like text splitting, embeddings, and document loading. They also use tkinter to create a simple GUI for asking questions.

## Installation
1. Clone this repository using `git clone git@github.com:MNFaz01/GPT-based-Knowledge-Base.git` or download as a ZIP file and extract it to your preferred location.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment by running `python -m venv venv` in your terminal.
4. Activate the virtual environment by running `source venv/bin/activate` on macOS/Linux or `venv\Scripts\activate` on Windows.
5. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.  
6. Update the .env file with the necessary environment variables. Here is an example .env file:  
* PDF_PATH_SINGLE=/path/to/single/pdf 
* PDF_PATH_MULTIPLE=/path/to/multiple/pdf   
* OPENAI_API_KEY = your_api_key  
* MODEL_NAME = your_desired_model_name  

In order to use the OpenAI API, you will need an API key. Follow the instructions on the OpenAI website to obtain your API key.

## Usage
* Update the `PDF_PATH_SINGLE` and `PDF_PATH_MULTIPLE` environment variable in the `.env` file to point to your own PDF documents.
* Run `single_pdf_reader.py` or `multiple_pdf_reader.py` in your terminal or IDE.  
* Type in your question in the Question: field and hit the Ask button.
* The app will display the most relevant answer based on the pre-existing documents.
* Update the PDFs as needed.

## Screenshots  
Screenshots of the GUI for each script are provided below:  

`Output of single_pdf_reader.py`  

`Output of multiple_pdf_reader.py`  

## Customization
You can customize the window size by editing the python scripts. For example, you can change the default window size by modifying the `width` and `height` variables.

You can also modify the `qa` function to change the behavior of the question answering system. For example, you can adjust the `k` parameter to retrieve more or fewer documents from the pre-existing documents.

## Credits
This app uses the following open-source libraries:

* langchain and openai for natural language processing tasks  
* PyPDF2 for reading PDF documents  
* tkinter for building the GUI  
* dotenv for loading environment variables  

## License
This project is licensed under the MIT License.
