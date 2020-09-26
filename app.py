from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('main.html')

@app.route("/predict", methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            experience = int(request.form['experience'])
            test_score = int(request.form['test_score'])
            interview_score = int(request.form['interview_score'])

            prediction = model.predict([[experience, test_score, interview_score]])
            # print(prediction[0][0])
            output = round(prediction[0][0], 2)
            if output < 0:
                return render_template('main.html',prediction_texts="Sorry you cannot predict")
            else:
                return render_template('main.html',prediction_text="Predicted Employee salary is $ {}".format(output))
        else:
            return render_template('main.html')
    except Exception as e:
        print(str(e))
        pass

if __name__=="__main__":
    app.run(debug=True)

