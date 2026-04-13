from flask import Flask, render_template, request
import os
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            
            raw_data = {
                "fixed_acidity": float(request.form['fixed_acidity']),
                "volatile_acidity": float(request.form['volatile_acidity']),
                "citric_acid": float(request.form['citric_acid']),
                "residual_sugar": float(request.form['residual_sugar']),
                "chlorides": float(request.form['chlorides']),
                "free_sulfur_dioxide": float(request.form['free_sulfur_dioxide']),
                "total_sulfur_dioxide": float(request.form['total_sulfur_dioxide']),
                "density": float(request.form['density']),
                "pH": float(request.form['pH']),
                "sulphates": float(request.form['sulphates']),
                "alcohol": float(request.form['alcohol'])
            }

            
            data = {
                "fixed acidity": raw_data["fixed_acidity"],
                "volatile acidity": raw_data["volatile_acidity"],
                "citric acid": raw_data["citric_acid"],
                "residual sugar": raw_data["residual_sugar"],
                "chlorides": raw_data["chlorides"],
                "free sulfur dioxide": raw_data["free_sulfur_dioxide"],
                "total sulfur dioxide": raw_data["total_sulfur_dioxide"],
                "density": raw_data["density"],
                "pH": raw_data["pH"],
                "sulphates": raw_data["sulphates"],
                "alcohol": raw_data["alcohol"]
            }

            # Convert to DataFrame
            input_df = pd.DataFrame([data])

            # Prediction
            obj = PredictionPipeline()
            predict = obj.predict(input_df)

            return render_template('results.html', prediction=str(predict))

        except Exception as e:
            print("Exception:", e)
            return f"Something went wrong: {e}"

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)