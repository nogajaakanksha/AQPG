# AQPG
Automatic Question Paper Generator in python

####Descrption

This system generates the question paper automatically using python. The system is divided into two steps:
The system uses NLP for question generation.

1. Question generation
    a) Using context based aproach
    b) Using NER based approach
    c) Using noun phrase approach
2. Question paper generation
    Algorithm is applied to find best questions from generated questions.
    Question paper is generated in pdf format.

####Important Notes

1. You will need to install nltk,tkinter library.

####Usage

1. Just run the file home.py
The system will prompt for login and register. After registering, login into the system.
2. Select the input file. System will prompt five options: 
  ---convert file
  ---Generate context wise questions
  ---Generate NER based questions
  ---Generate noun phrase wise questions
  ---Generate question paper
3. According to the selection, system will generate question paper.
