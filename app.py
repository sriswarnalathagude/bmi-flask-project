from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('smily.html')


@app.route('/result', methods=['POST'])
def result():

    weight = float(request.form['weight'])

    height_type = request.form['height_type']


    # Height in meters
    if height_type == "meters":

        height = float(request.form['height_meters'])


    # Height in feet
    elif height_type == "feet":

        feet = float(request.form['height_feet'])

        height = feet * 0.3048


    # Height in inches
    else:

        inches = float(request.form['height_inches'])

        height = inches * 0.0254


    bmi = weight / (height * height)


    if bmi < 18.5:

        status = "Underweight"
        color = "#3498db"


    elif bmi < 25:

        status = "Normal"
        color = "#2ecc71"


    elif bmi < 30:

        status = "Overweight"
        color = "#f39c12"


    else:

        status = "Obese"
        color = "#e74c3c"


    return render_template(
        'result.html',
        bmi=round(bmi, 2),
        status=status,
        color=color
    )


if __name__ == '__main__':
    app.run(debug=True)