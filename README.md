# CoWin-Availability-Checker
CoWin-Availability-Checker (Python Flask)

Pre-Requisities 

1. Install Python3
2. Install the following libraries using pip :

	a. pip install Flask
	b. pip install requests
	
How to Run

1. Open Powershell or cmd 
2. Use command python CoWin_API.py
3. Flask App will run on localhost:5000, use end point references below to use various functionalities
   e.g 	localhost:5000/stateInfo
   
End Point References - 

1. /stateInfo - To get state_ids for all states
   e.g. For Haryana, state_id = 12

2. /districtsByState/<state_id> - To get district_id using state_id
   e.g /districtsByState/12 - 	using this we get all districts in Haryana (state_id = 12)

3. /chandigarh - To get slot availability for Chandigarh (dist_id = 108) via findByDistrict CoWin API for current system date
   /chandigarh/<req_date> - To get slot availability for Chandigarh (dist_id = 108) via findByDistrict CoWin API for a specific date
   e.g. /chandigarh/06-05-2021 - it will fetch all available sessions in chandigarh for 6th May 2021

4. /panchkula - To get slot availability for Panchkula (dist_id = 187) via findByDistrict CoWin API for current system date
   /panchkula/<req_date> - To get slot availability for Panchkula (dist_id = 187) via findByDistrict CoWin API for a specific date
   e.g. /panchkula/06-05-2021 - it will fetch all available sessions in Panchkula for 6th May 2021

5. /district/<dist_id> - To get slot availability for a specific district via findByDistrict CoWin API for current system date
   /district/<dist_id>/<req_date> - To get slot availability for a specific district via findByDistrict CoWin API for a specific date
   e.g. /district/187/06-05-2021 - it will fetch all available sessions in Panchkula for 6th May 2021

6. /byPin/<pin_id> - To get slot availability for a specific pincode via findByPin CoWin API for current system date
   /byPin/<pin_id>/<req_date> - To get slot availability for a specific pincode via findByPin CoWin API for a specific date

Note - req_date must follow the format DD-MM-YYYY