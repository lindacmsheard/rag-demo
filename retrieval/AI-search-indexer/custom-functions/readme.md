## Pre-requisites
Install Azure functions core tools v4 on your development machine

verify with
```bash
func --version
```

## Set up a function project
```bash
## run these these to create a new function app in a different folder:
#func init
#func new

# work with the existing function app code
cd retrieval/AI-search-indexer/custom-functions

cp example_local.settings.json local.settings.json
# then update the connection strings in local.settings.json

# run the function app locally
func start
```

## Deployment
1. create a utility storage account if not available in the target resource group yet
```bash
az storage account create --name ragutilstorage --resource-group rag --location uksouth --sku Standard_LRS
```

2. create an azure function app with the cli (python function app, function runtime version 4)
```
az functionapp create --resource-group rag --consumption-plan-location uksouth --name ai-search-functions-py --storage-account ragutilstorage --runtime python --functions-version 4 --os-type Linux --runtime-version 3.10 
```


3. deploy the functionapp with functions core tools - take local settings 
> Note: ensure the local.settings.json file is updated with the correct connection strings
```bash
func azure functionapp publish ai-search-functions-py --publish-local-settings
```

sample GET request
```
https://ai-search-functions-py.azurewebsites.net/api/extract_xml_item?item=Barcode&file=ExampleXML.xml
```