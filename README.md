# orchestration
ctm aapi event orchestration

This handler builds and submits a COONTROL-M workflow in JSON from a JSON template.

The template has variables that need replacing prior to writing it out to be submitted to Control-M for processing.

For more information, see the code reference on the [Automation API Code Reference documentation page](https://docs.bmc.com/docs/display/public/workloadautomation/Control-M+Automation+API+-+Code+Reference).

## Prerequisites  
For CONTROL-M API support you require V9.0.18.200.  

## Requirements

The master json file needs to be copied to an accessible location and the path to the location needs to be updated in the code
A path is required to write out the JSON created

## Variables

The following variables need to be updated and tailored to your own environment in order to implement this example: 

endpoint
username
password

Look for these tags in the example and update the value to match your control-m environment.

__NOTE: The master JSON file is working sample. You will need to tailor the fields in the JSON to your requirements

This example changes the jobname of the first job in the workflow and also inserts the parameter at the end of the command being executed

### See the jobs in the UI

Once the workflow has been submitted you can track the jobs on the EM UI or using the API to GET the status and results
