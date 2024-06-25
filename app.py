from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained PKL file
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the route to handle the prediction request
@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Get the input RSSI values
        rssi1 = float(request.form["rssi1"])
        rssi2 = float(request.form["rssi2"])
        rssi3 = float(request.form["rssi3"])

        # Predict the location
        location = model.predict([[rssi1, rssi2, rssi3]])

        # Return the prediction result
        return render_template("result.html", location=location[0])
    else:
        # Return the prediction form
        return render_template("index.html")

# Define the route to show the prediction result
@app.route("/result.html")
def show_result():
    location = request.args.get("location")
    return render_template("result.html", location=location)

if __name__ == "__main__":
    app.run(debug=True)
