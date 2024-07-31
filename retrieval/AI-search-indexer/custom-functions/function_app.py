import azure.functions as func
import datetime
import json
import logging

import azurefunctions.extensions.bindings.blob as blob
import xml.etree.ElementTree as ET


app = func.FunctionApp()

@app.route(route="demo_http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="mock_skill_webapi", auth_level=func.AuthLevel.FUNCTION)
def mock_skill_webapi(req: func.HttpRequest) -> func.HttpResponse:
    """
    This function simulates an call made to a custom function from Azure AI Search Custom WebAPI skill.
    """
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )



@app.route(route="extract_xml_item", auth_level=func.AuthLevel.ANONYMOUS)
@app.blob_input(
    arg_name="inputblob", path="sampledata/xml/{file}", connection="DocumentStorage"
)
def extract_xml_item(req: func.HttpRequest, inputblob: blob.BlobClient) -> func.HttpResponse:
    logging.info(
        f"Python blob input function processed blob \n"
        f"Properties: {inputblob.get_blob_properties()}\n"
        f"Blob content head: {inputblob.download_blob().read(size=1)}"
    )
    item = req.params.get('item') or 'Barcode'
    
    xml_file = '/tmp/tmp.xml'
    with open(xml_file, 'wb') as f:
        f.write(inputblob.download_blob().readall())

    tree = ET.parse(xml_file)    
    root = tree.getroot()        
    # Assuming the barcode is in an element named 'Barcode'    
    barcode = root.find(f'.//{item}').text

    if barcode:
        return func.HttpResponse(f"Found {item}: {barcode}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )