from flask import Flask, render_template
import requests
import json
from datetime import date

app = Flask(__name__)

def getTodaysDate():
    temp_date = date.today().strftime("%d-%m-%Y")
    return str(temp_date)
    
def getColumnNames(temp_json):
    return(list(temp_json[0].keys()))
    
@app.route('/')
def homepage():
    return "States ---> /states"

@app.route('/stateInfo')
def genericStateInfo():
    
    api_response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states')
    json_data = json.loads(api_response.text)
    record_dict = json_data['states']
    ColumnNames = getColumnNames(record_dict)
    
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)

@app.route('/districtsByState/<dist_id>')
@app.route('/districtsBystate/<dist_id>')
@app.route('/districtsbyState/<dist_id>')
@app.route('/districtsbystate/<dist_id>')
def genericDistrictsByState(dist_id=None):
    
    api_response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/' + str(dist_id) )
    json_data = json.loads(api_response.text)
    record_dict = json_data['districts']
    ColumnNames = getColumnNames(record_dict)
    
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)
    
@app.route('/panchkula')
@app.route('/panchkula/<req_date>')
def availabilityPanchkula(req_date=None):

    if req_date == None :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=187&date=' + getTodaysDate() )
    else :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=187&date=' + str(req_date) )
    json_data = json.loads(api_response.text)
    record_dict = json_data['sessions']
    
    if len(record_dict) == 0 :
        return "<h1>NO SESSIONS AVAILABLE</h1>"
    
    ColumnNames = getColumnNames(record_dict)
        
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)

@app.route('/chandigarh')
@app.route('/chandigarh/<req_date>')
def availabilityChandigarh(req_date=None):  

    if req_date == None :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=108&date=' + getTodaysDate() )
    else :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=108&date=' + str(req_date) )
    
    json_data = json.loads(api_response.text)
    record_dict = json_data['sessions']
    
    if len(record_dict) == 0 :
        return "<h1>NO SESSIONS AVAILABLE</h1>"
    
    ColumnNames = getColumnNames(record_dict)
        
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)

@app.route('/district/<dist_id>')
@app.route('/district/<dist_id>/<req_date>')
def availabilityByDistrict(dist_id=None, req_date=None):
    
    if req_date == None :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=' + str(dist_id) + '&date=' + getTodaysDate() )
    else :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=' + str(dist_id) + '&date=' + str(req_date) )
    json_data = json.loads(api_response.text)
    record_dict = json_data['sessions']
    
    if len(record_dict) == 0 :
        return "<h1>NO SESSIONS AVAILABLE</h1>"
    
    ColumnNames = getColumnNames(record_dict)
        
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)

@app.route('/byPin/<pin_id>')
@app.route('/byPin/<pin_id>/<req_date>')
def availabilityByPin(pin_id=None, req_date=None):
    
    if req_date == None :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + str(pin_id) + '&date=' + getTodaysDate() )
    else :
        api_response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + str(pin_id) + '&date=' + str(req_date) )
    json_data = json.loads(api_response.text)
    record_dict = json_data['sessions']
    
    if len(record_dict) == 0 :
        return "<h1>NO SESSIONS AVAILABLE</h1>"
    
    ColumnNames = getColumnNames(record_dict)
        
    return render_template('session_template.html', records=record_dict, colnames=ColumnNames)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)