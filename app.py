from flask import Flask, render_template, request
import random

app = Flask(__name__)

def transform_word(word):
    
    #Get the index of spaces, if the given word contains any
    spaces_index = []
    letter_index = 0    
    for letter in word:

        if letter == " ":
            spaces_index.append(letter_index)
            letter_index += 1

        else:
            letter_index += 1

    #Generate indexes to be censored, making sure we don't censor spaces
    censored_letters = round(len(word)*0.3)  #how many letters will be censored
    picked_indexes = [] #index of already censored letters
    
    for _ in range(censored_letters):
        censored_letter_index = random.choice([i for i in range(0,len(word)) if (i not in spaces_index) and (i not in picked_indexes)])

        picked_indexes.append(censored_letter_index)

    #Turn letters into underscores
    word = list(word)
    for i in picked_indexes:
        word[i] = "_"
    
    transformed = "".join(str(element) for element in word)
    return transformed




@app.route('/', methods=['GET', 'POST'])
def index():
  
    if request.method == 'POST':
        input_text = request.form['input_text']
        lines = input_text.splitlines()

        transformed_lines = [transform_word(line) for line in lines]
        output_text = '\n'.join(transformed_lines)

    return render_template('index.html', input_text=input_text, output_text=output_text)


if __name__ == '__main__':
    app.run(debug=True)
