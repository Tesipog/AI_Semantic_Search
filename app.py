from flask import Flask, request,render_template
from Query import QuestionSearch
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Home.html')
@app.route('/process', methods=["POST"])
def process():
    input_data = request.form.get('input_field')
    question_search = QuestionSearch()
    result = question_search.search(input_data)
    result = result.replace('\n', '<br>')
    return result

if __name__ == '__main__':
    app.run(debug=True)