from flask import Flask,render_template,url_for,request
import sqlite3

import joblib
model = joblib.load('logistic_regression.lb')
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
        flight_distance = int(request.form["flight_distance"])
        inflight_entertainment = int(request.form["inflight_entertainment"])
        baggage_handling = int(request.form["baggage_handling"])
        cleanliness = int(request.form["cleanliness"])
        departure_delay = int(request.form["departure_delay"])
        arrival_delay = int(request.form["arrival_delay"])
        gender = int(request.form["gender"])
        customer_type = int(request.form["customer_type"])
        travel_type = int(request.form["travel_type"])
        class_type = request.form["class_type"]
        Class_Eco = 0
        Class_Eco_Plus = 0
        if class_type == 'ECO':
            Class_Eco = 1
        elif class_type == 'ECO_PLUS':
            Class_Eco_Plus = 1

        conn = sqlite3.connect("userdata.db")
        conn.execute("""
                    insert into userrecord(
                        age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,departure_delay, 
                        arrival_delay, gender, customer_type, class_type,type_of_travel, Class_Eco,Class_Eco_Plus)
                        values(?,?,?,?,?,?,?,?,?,?,?,?,?) """,
                        (age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,departure_delay, 
                        arrival_delay, gender, customer_type, class_type, travel_type, Class_Eco,Class_Eco_Plus))

        conn.commit()
        conn.close()

        UNSEEN_DATA = [[age,
                        flight_distance,
                        inflight_entertainment,
                        baggage_handling,
                        cleanliness,
                        departure_delay,
                        arrival_delay,
                        gender,
                        customer_type,
                        travel_type,
                        Class_Eco,
                        Class_Eco_Plus
                        ]]
        
        prediction = model.predict(UNSEEN_DATA)[0]
        print(prediction)
        labels = {'1':"SATISFIED",'0':"UNSATISFIED"}

        # return label[str(prediction)]
        return render_template('output.html',output=labels[str(prediction)],
                               age=age,
                               flight_distance=flight_distance,
                               inflight_entertainment=inflight_entertainment,
                               baggage_handling=baggage_handling,
                               cleanliness=cleanliness,
                               departure_delay=departure_delay,
                               arrival_delay=arrival_delay,
                               gender='Male' if gender == 1 else 'female',
                               customer_type='Loyal Customer' if customer_type == 0 else 'Disloyal Customer',
                               class_type=class_type,
                               travel_type='Personal Travel' if travel_type == 1 else 'Business Travel'
                            )

if __name__ == "__main__":
    app.run(debug=True)