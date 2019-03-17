def get_answer(prompt):
    answer = input(prompt)
    answer = answer.lower() #Set response to lower case
    while not (answer=='yes' or answer=='no'):
        answer = input(prompt)
    return answer

if __name__ == '__main__':
    get_answer('Is your name Dillbob?: ')