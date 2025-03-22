import os
import requests
import json
import re
import time
import sqlite3
import warnings

## Load Enphase API Authentication Parameters
f = open("auth.txt")
api_key = f.readline()[:-1]
user_id = f.readline()[:-1]
system_id = f.readline()[:-1]
auth_string = "key="+api_key+"&user_id="+user_id
f.close()

## Connect to Database
db_path = os.path.join("solar.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

## Query System Information if Unknown
if system_id == '':
    q = "https://api.enphaseenergy.com/api/v2/systems?"+auth_string
    r = requests.get(q)
    #print(r.status_code)
    #print(r.text)
    # TODO use if test to ensure r.status_code == 200 aka "OK"
    # Example r.text return:
    rr = '{"systems":[{"system_id":777364,"system_name":"Egan, Jeff","system_public_name":"Residential System","status":"normal","timezone":"America/New_York","country":"US","state":"NH","city":"Pelham","postal_code":"03076","connection_type":"ethernet","meta":{"status":"normal","last_report_at":1574021515,"last_energy_at":1574021293,"operational_at":1444486200}}]}'
    # TODO implement regular expressions re.search to parse the system id

q_yr = str(2019)
q_mo = str(11)
q_dy = str(18)

for q_yr in ["2019"]:
    for q_mo in ["12"]:
        for q_dyv in list(range(1,32)):
            q_dy = str(q_dyv)
            q = "https://api.enphaseenergy.com/api/v2/systems/"+system_id+"/summary?summary_date="+q_yr+"-"+q_mo+"-"+q_dy+"&"+auth_string  # Docs: https://developer.enphase.com/docs#summary
            print(q)
            r = requests.get(q)
            print(r.status_code)
            if r.status_code == 200:
                print(r.text)
                m = re.search(r'"energy_today":(\d+)',r.text)  # energy_today = Watt-hours
                mq = "INSERT OR REPLACE INTO production (date, energy_Wh) VALUES ('"+q_mo+"/"+q_dy+"/"+q_yr+"', "+m[1]+")"
                cur.execute(mq)
                conn.commit()
            time.sleep(7.0)  ## API Call Limitations = Max 10 hits per minute, Max 10,000 hits per month 
conn.close()