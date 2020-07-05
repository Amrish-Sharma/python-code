#importing needed modules flask(to create the endpoints),request to fetch the json from timeapi
#json to load the result and get needed information
from flask import Flask
import requests
import json
#creating an app instance of the flask
app = Flask(__name__)
#creating a welcome page for the flask on localhost
@app.route('/')
def welcome():
    return "Hello, Welcome to Time Endpoint API Implementation"
#to access this on your machine try below links on your webbrowser:# 127.0.0.1/timezone/pst
# # 127.0.0.1/timezone/utc
# 127.0.0.1/timezone/cst
@app.route('/timezone/<timezone>')
def get_time(timezone):
    #url from which the information of timedetails are fetched in json format
    url = "http://worldclockapi.com/api/json/{}/now".format(timezone)
    response = requests.get(url)
    data = response.text
    #loading the details in json format in variable timedetails
    timedetails = json.loads(data)
    #to get only the currentDateTime and then fetching only the time
    currenttime = str(timedetails['currentDateTime'])[11:16]
    #retunning the details of the time for the current timezone
    return "Current time in timezone {} is: ".format(timezone)+currenttime

#running the flask in debug mode
if __name__ == "__main__":
    app.run(debug=True)



