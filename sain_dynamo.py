import requests
import json
import os
import boto3
import collections
import sys

def lambda_handler():

  with open("/home/wbad/lambda/prod/dynamo.json", "r") as jsonFile:
    data = json.load(jsonFile, object_pairs_hook=collections.OrderedDict)

#  sys.argv[2]

  infilename = sys.argv[1]
  file_command = '/home/neilc/myscript.sh'
  proc_step = file_command + " " + infilename

  tmp = data
  data["quicktest"]["DYNFILE"]["Command"] = proc_step
  data["quicktest"][infilename] = data["quicktest"]["DYNFILE"]
  del data["quicktest"]["DYNFILE"]

  with open("/home/wbad/lambda/input.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)

    jsonFile.close()

#  with open("/home/wbad/lambda/input.json", "r") as jsonFile:
#    data = json.load(jsonFile)

#  tmp = data["quicktest"]["testjb1"]
#  data["testjb1"] = "myfilename"

#  with open("/home/wbad/lambda/newinput.json", "w") as jsonFile:
#    json.dump(data, jsonFile)

#  with open('/home/wbad/lambda/input.json') as json_data:
#    d = json.load(json_data)
#    print(d) 


    global r
    #endpoint_url='https://ncudrs.i2t.com:8443/'  
    endpoint_url='https://ec2-35-177-38-80.eu-west-2.compute.amazonaws.com:8443/'  
    login_url=endpoint_url+'automation-api/session/login'
    user='emuser'                                                       
    password='ncpass'                                                   
    payload = {'username': user, 'password': password}
    headers = {'Content-type': 'application/json'}
	#  Request for token   
    r = requests.post(login_url, data=json.dumps(payload),verify=False,headers=headers)
    r_json=json.loads(r.text)
    token=r_json['token']
    #print(token)
    #ctm='ctmaws'
    endpoint_run=endpoint_url+'automation-api'
    header_auth_val= 'Bearer '+ token
    headers.update(Authorization=header_auth_val)
    #  Request for submitting and running a JSON payload  
    payload = '/home/wbad/lambda/input.json'
    #r = requests.post(endpoint_run, data=payload,verify=False,headers=headers)
    #print(r.text)
    uploaded_files = [
        ('jobDefinitionsFile', ('Jobs.json', open(payload, 'rb'), 'application/json'))
    ]
    r = requests.post(endpoint_run + '/run', files=uploaded_files, headers={'Authorization': 'Bearer ' + token}, verify=False)
    print(r.content)
    #  Request for logout
    endpoint_logout=endpoint_url+'automation-api/session/logout'
    r = requests.post(endpoint_logout, verify=False,headers=headers)
    print(json.loads(r.text))
    return 'Request for delete received'

lambda_handler()
