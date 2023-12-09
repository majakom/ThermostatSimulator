from flask import Flask, render_template
#import thermostat_formulas

app = Flask(__name__, template_folder='html_files')
@app.route("/")
@app.route("/flaskApp")
def flaskApp():
    return render_template('flaskApp.html')

if __name__ == '__main__':  
   app.run(debug=True)