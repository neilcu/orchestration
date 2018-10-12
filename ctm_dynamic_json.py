import requests
import json
import os
import boto3
import collections
import sys

def lambda_handler():

  with open("<masterpath>/master.json", "r") as jsonFile:
    data = json.load(jsonFile, object_pairs_hook=collections.OrderedDict)

  infilename = sys.argv[1]
  file_command = '<pathtoscript>/myscript.sh'
  proc_step = file_command + " " + infilename

  tmp = data
  data["quicktest"]["DYNFILE"]["Command"] = proc_step
  data["quicktest"][infilename] = data["quicktest"]["DYNFILE"]
  del data["quicktest"]["DYNFILE"]

  with open("<path_to_write_new_input_json>"/input.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)

    jsonFile.close()

    global r

    endpoint_url='https://<myhostname>:8443/'
    login_url=endpoint_url+'automation-api/session/login'
    user='<myuser>'
    password='<mypassword>'
    payload = {'username': user, 'password': password}
    headers = {'Content-type': 'application/json'}
	#  Request for token
    r = requests.post(login_url, data=json.dumps(payload),verify=False,headers=headers)
    r_json=json.loads(r.text)
    token=r_json['token']
    print(token)

    endpoint_run=endpoint_url+'automation-api'
    header_auth_val= 'Bearer '+ token
    headers.update(Authorization=header_auth_val)
    #  Request for submitting and running a JSON payload
    payload = '/home/wbad/lambda/input.json'
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
