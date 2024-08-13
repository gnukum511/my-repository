# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# Create a function named "lcm" which calculates the least common multiple of two numbers
def lcm(num1,num2):
    common_multiplications = [] 
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i) 
    return min(common_multiplications)

# Create a function named `index` which uses a template file named `index.html`
# send two numbers as template variables to the index.html and assign route of no path ('/')
@app.route('/')
def index():
    num1 = 10
    num2 = 20
    return render_template('index.html', num1=num1, num2=num2)

# Calculate LCM using the "lcm" function, then send the result to the "result.html" file
# Assign route of path ('/calc'). 
@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "GET":
        return render_template("index.html")
    else:           # request.method == "POST"
        # lcm, result1, result2, developer_name
        num1 = int(request.form.get("number1"))
        num2 = int(request.form.get("number2"))
        lcm_caluclated = num1 * num2
        return render_template("result.html", lcm=lcm_caluclated, result1=num1, result2=num2, developer_name="Garry")
# Add a statement to run the Flask application which can be debugged
if __name__ == '__main__':
    app.run(debug=True)