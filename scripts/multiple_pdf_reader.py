#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing all the packages

import os
import tkinter as tk
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from dotenv import load_dotenv


# Load environment variables
env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

pdf_path = os.getenv('PDF_PATH_MULTIPLE')
openai_api_key = os.getenv('OPENAI_API_KEY')
model_name = os.getenv('MODEL_NAME')

# Create index from PDFs
loaders = [UnstructuredPDFLoader(os.path.join(pdf_path, fn)) for fn in os.listdir(pdf_path)]
index = VectorstoreIndexCreator().from_loaders(loaders)

# Define function to handle question input and display answer and source
def handle_question():
    question = question_entry.get()
    result = index.query_with_sources(question)
    answer_label.config(text=f"Answer: {result['answer']}")
    source_label.config(text=f"Source: {result['sources']}")

# Create Tkinter app window
window = tk.Tk()
window.title('Question and Answer')
window.geometry('500x300')

# Create question input box
question_label = tk.Label(window, text='Enter your question:')
question_label.pack()
question_entry = tk.Entry(window, width=80)
question_entry.pack()

# Create button to submit question
submit_button = tk.Button(window, text='Submit', command=handle_question)
submit_button.pack()

# Create label to display answer
answer_label = tk.Label(window, text='', wraplength=400)
answer_label.pack()

# Create label to display source
source_label = tk.Label(window, text='')
source_label.pack()

# Run Tkinter app
window.mainloop()


# In[ ]:




