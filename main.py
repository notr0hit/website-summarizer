# Importing modules
import tkinter as tk

'''Tkinter is the standard GUI library for Python.it provides fast and easy way to create GUI applications. '''
import nltk

'''The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical 
natural language processing (NLP) for English written in the Python programming language'''
# nltk.download('punkt')
from newspaper import Article

'''Newspaper is a Python module used for extracting and parsing newspaper articles. Newspaper use advance algorithms 
with web scrapping to extract all the useful text from a website'''
import pyttsx3

''' pyttsx3 is a text-to-speech conversion library in Python'''


def get_summary():
    url = url_text.get('1.0', 'end').strip()

    article = Article(url)
    article.download()
    article.parse()
    '''parse is a command for dividing the given program code into a small piece of code for analyzing the correct syntax.
    Python parser is mainly used for converting data in the required format, this conversion process is known as parsing. '''
    article.nlp()
    '''Natural language processing (NLP) is a field that focuses on making natural human language usable by computer programs.
     NLTK, or Natural Language Toolkit, is a Python package that you can use for NLP.'''

    title.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.config(state='disable')
    summary.config(state='disable')

    global summary_global_var
    summary_global_var = 'Title: ' + article.title + '. Summary: ' + article.summary


def listen_summary():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 25)
    engine.say(summary_global_var, rate)
    engine.runAndWait()

import tkinter as tk

'''Tkinter is the standard GUI library for Python.it provides fast and easy way to create GUI applications. '''
'''gui is a desktop  app which helps to interact with the computer using graphical icons'''
# building gui


root = tk.Tk() #empty window
'''root is a empty window where we are going to place all the widget now'''
root.title('Article Summarizer')
root.geometry('1200x600')

#Label is a widget that is used to implement display boxes where we can place text
#inside fxns parameters
# root is the parent window
title_label = tk.Label(root, text='Title', font=('Helvetica', 12, 'bold'))
title_label.pack() # pack is used to show the label in root

#Text Widget is used where a user wants to insert multiline text fields
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

summary_label = tk.Label(root, text='Summary', font=('Helvetica', 12, 'bold'))
summary_label.pack()

summary = tk.Text(root, height=26, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()
##### Now Khushi will explain

url_label = tk.Label(root, text='URL')
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.pack()

summarize_button = tk.Button(root, text='Summarize',bg='gray', fg='white', command=get_summary)
summarize_button.pack()

listen_button = tk.Button(root, text='Listen to Summary', bg='gray', fg='white',command=listen_summary)
listen_button.pack()

root.mainloop() # keep displaying the window until we close it.
