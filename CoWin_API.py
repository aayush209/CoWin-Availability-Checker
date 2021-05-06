from flask import Flask, render_template
import requests
import json
from datetime import date

app = Flask(__name__)

baseURL = 'https://cdn-api.co-vin.in/api'
    
def getTodaysDate():
    temp_date = date.today().strftime("%d-%m-%Y")
    return str(temp_date)
    
def getColumnNames(temp_json):
    return(list(temp_json[0].keys()))


def responseGenericInfo(api_response, states_or_districts, state_id_param=None):
    
    states_or_districts = str(states_or_districts)
    json_data = json.loads(api_response.text)
    record_dict = json_data[states_or_districts]
    ColumnNames = getColumnNames(record_dict)
    
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)    
    
def responseSlotAvailability(api_response, date_param):
    
    json_data = json.loads(api_response.text)
    record_dict = json_data['sessions']
    
    if len(record_dict) == 0 :
        return "<h1>NO SESSIONS AVAILABLE for " + date_param + "</h1>"
    
    ColumnNames = getColumnNames(record_dict)

    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)
    
@app.route('/')
def homepage():
    return "States ---> /states"

@app.route('/stateInfo')
def genericStateInfo():
    
    api_response = requests.get( baseURL + '/v2/admin/location/states')

    return responseGenericInfo(api_response, 'states')

@app.route('/districtsByState/<state_id>')
@app.route('/districtsBystate/<state_id>')
@app.route('/districtsbyState/<state_id>')
@app.route('/districtsbystate/<state_id>')
def genericDistrictsByState(state_id=None):
    
    state_id_param = str(state_id)
    api_response = requests.get( baseURL + '/v2/admin/location/districts/' + state_id_param )

    return responseGenericInfo(api_response, 'districts', state_id_param)    
    
@app.route('/panchkula')
@app.route('/panchkula/<req_date>')
def availabilityPanchkula(req_date=None):
    
    date_param = getTodaysDate()
    if req_date != None :
        date_param = str(req_date) 
        
    api_response = requests.get( baseURL + '/v2/appointment/sessions/public/findByDistrict?district_id=187&date=' + date_param)

    return responseSlotAvailability(api_response, date_param)

@app.route('/chandigarh')
@app.route('/chandigarh/<req_date>')
def availabilityChandigarh(req_date=None):  
    
    date_param = getTodaysDate()
    if req_date != None :
        date_param = str(req_date) 
    
    api_response = requests.get( baseURL + '/v2/appointment/sessions/public/findByDistrict?district_id=108&date=' + date_param)
    
    return responseSlotAvailability(api_response, date_param)

@app.route('/district/<dist_id>')
@app.route('/district/<dist_id>/<req_date>')
def availabilityByDistrict(dist_id=None, req_date=None):

    dist_it_param = str(dist_id)
    date_param = getTodaysDate()
    
    if req_date != None :
        date_param = str(req_date) 

    api_response = requests.get( baseURL + '/v2/appointment/sessions/public/findByDistrict?district_id=' + dist_it_param + '&date=' + date_param )

    return responseSlotAvailability(api_response, date_param)

@app.route('/byPin/<pin_id>')
@app.route('/byPin/<pin_id>/<req_date>')
def availabilityByPin(pin_id=None, req_date=None):
    
    pin_id_param = str(pin_id)
    date_param = getTodaysDate()
    
    if req_date != None :
        date_param = str(req_date) 
        
    api_response = requests.get( baseURL + '/v2/appointment/sessions/public/findByPin?pincode=' + pin_id_param + '&date=' + date_param )

    return responseSlotAvailability(api_response, date_param)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)