from flask import Flask,render_template,url_for,request
import sqlite3

import joblib
model = joblib.load('randomforest.lb')
app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/project')    # http://127.0.0.1:5000/project
def project():
    return render_template('project.html') 

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    if  request.method == "POST":
        age = int(request.form["age"])
        bmi = int(request.form["bmi"])
        child = int(request.form["child"])
        gender = int(request.form["gender"])
        smoker = int(request.form["smoker"])
        region = request.form["region"]
        northwest = 0
        southeast = 0
        northeast = 0
        if region == 'northwest':
            northwest = 1
        elif region == 'southeast':
            southeast = 1
        elif region == 'northeast':
            northeast = 1

        conn = sqlite3.connect("userdata.db")
        conn.execute("""
                    insert into userrecord(
                        age, bmi, child, gender, smoker, region, northwest,southeast,northeast)
                        values(?,?,?,?,?,?,?,?,?) """,
                        (age, bmi, child, gender, smoker, region, northwest,southeast,northeast))
        conn.commit()
        conn.close()

        UNSEEN_DATA = [[age, bmi, child, gender, smoker, northwest,southeast,northeast]]
        
        prediction = model.predict(UNSEEN_DATA)
        print(prediction)

        # return label[str(prediction)]
        return render_template('output.html',output=prediction,
                               age=age,
                               bmi=bmi,
                               child=child,
                               gender='Male' if gender == 1 else 'female',
                               smoker='Yes' if smoker == 1 else 'No',
                               region=region,
                            )

if __name__ == "__main__":
    app.run(debug=True)