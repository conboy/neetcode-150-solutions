import os
def make_py(folder):
    # os.chdir(f'/home/conrad/neetcode-150-solutions/{folder}')

    question_name = input("Input the name of the question: ")
    question_name = question_name.lower().replace('.', '').replace(' ', '_') + '.py'
    print(question_name)
    # f = open(question_name, 'w')
    # f.close()

make_py('two_pointers')