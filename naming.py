import os

os.chdir('/home/conrad/neetcode-150-solutions/arrays_&_hashing')

question_name = input("Input the name of the question: ")
question_name = question_name.lower().replace('.', '').replace(' ', '_') + '.py'

f = open(question_name, 'w')
f.close()