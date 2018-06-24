from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/availablerides')
def avilable_rides():
    return render_template('availableRides.html')
    
@app.route('/riderequests')
def riderequest():
    return render_template('rideRequests.html')

@app.route('/addride')
def addride():
    return render_template('addride.html')
    
if __name__ == '__main__':
     app.run(debug = True)