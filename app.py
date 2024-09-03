from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def analyse():
    if request.method == 'POST':
        text = TextBlob(request.form['text'])
        sentiment = text.sentiment
        if sentiment.polarity >= 0.80 and sentiment.subjectivity >= 0.80:
            result = 'Анализ настроения: позитивное, полное понимание ситуации'
            color = 'green'
        elif 0.20 >= sentiment.polarity >= 0.0 and sentiment.subjectivity >= 0.80:
            result = 'Анализ настроения: холодный рассудок, полное понимание ситуации'
            color = 'darkseagreen'
        elif 0.7 >= sentiment.polarity >= 0.51 and sentiment.subjectivity >= 0.80:
            result = 'Анализ настроения: позитивное рассуждение, полное понимание ситуации'
            color = 'green'
        elif sentiment.polarity >= 0.70 and sentiment.subjectivity >= 0.70:
            result = 'Анализ настроения: позитивное, уверенное, объективное'
            color = 'green'
        elif sentiment.polarity >= 0.70 and sentiment.subjectivity >= 0.50:
            result = 'Анализ настроения: позитивное, возможно не объективное'
            color = 'darkseagreen'
        elif 0.70 >= sentiment.polarity >= 0.51 and 0.70 >= sentiment.subjectivity >= 0.51:
            result = 'Анализ настроения: позитивное, объективное'
            color = 'darkseagreen'
        elif 0.70 >= sentiment.polarity >= 0.51 and 0.50 >= sentiment.subjectivity:
            result = 'Анализ настроения: позитивное, неуверенное'
            color = 'yellow'
        elif 0.50 >= sentiment.polarity >= 0.41 and 0.49 >= sentiment.subjectivity:
            result = 'Анализ настроения: нейтральное, неуверенное'
            color = 'yellow'
        elif 0.50 >= sentiment.polarity >= 0.41 and 0.50 >= sentiment.subjectivity >= 0.41:
            result = 'Анализ настроения: нейтральное, неуверенное'
            color = 'yellow'
        elif 0.50 >= sentiment.polarity >= 0.41 and 0.60 >= sentiment.subjectivity >= 0.41:
            result = 'Анализ настроения: нейтральное'
            color = 'yellow'
        elif 0.50 >= sentiment.polarity >= 0.41 and 0.70 >= sentiment.subjectivity >= 0.51:
            result = 'Анализ настроения: нейтральное, уверенное'
            color = 'yellow'
        elif 0.30 >= sentiment.polarity >= 0.21 and 0.70 >= sentiment.subjectivity >= 0.51:
            result = 'Анализ настроения: объективная злость'
            color = 'red'
        elif 0.40 >= sentiment.polarity >= 0.31 and 0.60 >= sentiment.subjectivity >= 0.41:
            result = 'Анализ настроения: нейтральное, неуверенное'
            color = 'rosybrown'
        elif 0.21 >= sentiment.polarity and sentiment.subjectivity >= 0.51:
            result = 'Анализ настроения: негативное рассуждение'
            color = 'rosybrown'
        elif 0.30 >= sentiment.polarity >= 0.20 and 0.40 >= sentiment.subjectivity:
            result = 'Анализ настроения: негативное, неуверенное'
            color = 'red'
        elif 0.40 >= sentiment.polarity >= 0.21 and 0.50 >= sentiment.subjectivity:
            result = 'Анализ настроения: нейтральное, неуверенное'
            color = 'rosybrown'
        elif 0.5 >= sentiment.polarity > 0.3 and 0.9 >= sentiment.subjectivity > 0.7:
            result = 'Анализ настроения: нейтральное, холодный рассудок, понимание ситуации'
            color = 'yellow'
        elif 0.30 >= sentiment.polarity > 0.0 and 0.30 >= sentiment.subjectivity > 0.0:
            result = 'Анализ настроения: отрицательное'
            color = 'red'
        elif 0.20 >= sentiment.polarity >= 0.1 and 0.50 >= sentiment.subjectivity >= 0.31:
            result = 'Анализ настроения: негативное, возможен стресс'
            color = 'rosybrown'
        elif 0.20 >= sentiment.polarity >= 0.1 and 0.30 >= sentiment.subjectivity:
            result = 'Анализ настроения: негативное, возможна паника'
            color = 'red'
        elif 0.1 >= sentiment.polarity > 0.0 and 0.40 >= sentiment.subjectivity > 0.0:
            result = 'Анализ настроения: негативное, неуверенность'
            color = 'red'
        elif sentiment.polarity == 0.0 and sentiment.subjectivity == 0.0:
            result = 'Анализ настроения: доказательство, утверждение, возможно неустойчивое, возможно не распознано'
            color = 'black'
        elif 0.0 >= sentiment.polarity and 0.0 >= sentiment.subjectivity:
            result = 'Анализ настроения: стресс, неуверенность в действиях'
            color = 'black'
        elif 0.0 >= sentiment.polarity and 0.3 >= sentiment.subjectivity > 0.0:
            result = 'Анализ настроения: поникшее, стресс'
            color = 'red'
        elif 0.0 >= sentiment.polarity and 0.7 >= sentiment.subjectivity > 0.3:
            result = 'Анализ настроения: тоскливое, рассуждение'
            color = 'rosybrown'
        elif 0.55 >= sentiment.polarity and 1.0 >= sentiment.subjectivity > 0.8:
            result = 'Анализ настроения: спокойное, поиск выхода из ситуации'
            color = 'green'
        elif 0.1 >= sentiment.polarity > 0.0 and 0.55 >= sentiment.subjectivity > 0.35:
            result = 'Анализ настроения: тревожное, возможно неуверенное'
            color = 'rosybrown'
        elif 0.7 >= sentiment.polarity > 0.6 and 0.8 >= sentiment.subjectivity > 0.7:
            result = 'Анализ настроения: позитивное рассуждение, уверенное'
            color = 'darkseagreen'
        elif 0.3 >= sentiment.polarity > 0.1 and 0.8 >= sentiment.subjectivity > 0.7:
            result = 'Анализ настроения: негативное рассуждение, понимание ситуации'
            color = 'rosybrown'
        else:

            result = 'Анализ настроения: не распознано, расставьте знаки препинания и завершения'
            color = 'black'
        return render_template('base.html', result=result, sentiment=sentiment, color=color)

