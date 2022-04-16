from flask import Flask,render_template,request, redirect, url_for

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route("/")
def index():
    return redirect(url_for("form"))

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return redirect(url_for("data"))
    return render_template('form.html')
 
@app.route('/data/', methods = ["GET", "POST"])
def data():
    form_data = request.form
    return render_template('data.html',form_data = form_data)

if __name__ == '__main__':
    app.run(debug=True)