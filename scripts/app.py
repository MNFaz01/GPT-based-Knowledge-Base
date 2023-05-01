#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

pdf_path = os.getenv('PDF_PATH')
openai_api_key = os.getenv('OPENAI_API_KEY')
model_name = os.getenv('MODEL_NAME')

# location of the pdf file/files. 
reader = PdfReader(pdf_path)

# read data from the file and put them into a variable called raw_text
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

# We need to split the text that we read into smaller chunks so that during information retreival we don't hit the token size limits. 

text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)
# expose this index in a retriever interface
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":5})

# create a chain to answer questions 
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(model_name=model_name), chain_type="stuff", retriever=retriever, return_source_documents=True)


def ask_question():
    query = question_entry.get()
    result = qa({"query": query})
    answer_text.delete("1.0", tk.END)
    answer_text.insert(tk.END, result['result'])

# create a tkinter window
window = tk.Tk()
window.title("Question Answering App")

# create a label for the question
question_label = tk.Label(window, text="Enter your question:")
question_label.pack()

# create an entry field for the question
question_entry = tk.Entry(window)
question_entry.pack()

# create a button to ask the question
ask_button = tk.Button(window, text="Ask", command=ask_question)
ask_button.pack()

# create a label for the answer
answer_label = tk.Label(window, text="Answer:")
answer_label.pack()

# create a text box to display the answer
answer_text = tk.Text(window)
answer_text.pack()

# run the tkinter event loop
window.mainloop()

