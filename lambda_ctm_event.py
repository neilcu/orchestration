import requests
import json
def lambda_handler(event, context):
    global r
    endpoint_url='https://hostname:8443/'
    login_url=endpoint_url+'automation-api/session/login'
    print(login_url)
    user='user'
    password='password'
    payload = {'username': user, 'password': password}
    headers = {'Content-type': 'application/json'}
        #  Request for token
    r = requests.post(login_url, data=json.dumps(payload),verify=False,headers=headers)
    r_json=json.loads(r.text)
    token=r_json['token']
    print(token)
    ctm='ctmaws'
    endpoint_event=endpoint_url+'automation-api/run/event/'+ctm
    eventname='bluem_event'
    eventdate='ODAT'
    payload = {'name': eventname, 'date': eventdate}
    header_auth_val= 'Bearer '+ token
    headers.update(Authorization=header_auth_val)
    #  Request for setting the event
    r = requests.post(endpoint_event, data=json.dumps(payload),verify=False,headers=headers)
    print(json.loads(r.text))
    #  Request for logout
    endpoint_logout=endpoint_url+'automation-api/session/logout'
    r = requests.post(endpoint_logout, verify=False,headers=headers)
    print(json.loads(r.text))
    print('Request for delete received')
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }
