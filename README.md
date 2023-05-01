# Question-Answering App with your own data using OpenAI GenAI Models
This is a simple app built using Python's tkinter library that allows you to ask questions and get answers based on a pre-existing document. The app uses the langchain library to perform natural language processing tasks such as text splitting, embeddings, and question answering.

## Installation
1. Clone this repository using `git clone git@github.com:MNFaz01/GPT-based-Knowledge-Base.git` or download as a ZIP file and extract it to your preferred location.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment by running `python -m venv venv` in your terminal.
4. Activate the virtual environment by running `source venv/bin/activate` on macOS/Linux or `venv\Scripts\activate` on Windows.
5. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.

In order to use the OpenAI API, you will need an API key. Follow the instructions on the OpenAI website to obtain your API key.

## Usage
1. Update the `PDF_PATH` environment variable in the `.env` file to point to your own PDF document.
2. Run the app.py file using your terminal: `python app.py`
3. Type in your question in the Question: field and hit the Ask button.
4. The app will display the most relevant answer based on the pre-existing document.

## Customization
You can customize the app by editing the app.py file. For example, you can change the default window size by modifying the `width` and `height` variables.

You can also modify the `qa` function to change the behavior of the question answering system. For example, you can adjust the `k` parameter to retrieve more or fewer documents from the pre-existing document.

## Credits
This app uses the following open-source libraries:

langchain and openai for natural language processing tasks
PyPDF2 for reading PDF documents
tkinter for building the GUI
dotenv for loading environment variables

## License
This project is licensed under the MIT License.
