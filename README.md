# Lab.Azure.API-Management

A basic API Management example with Azure Functions, Cosmos DB and Azure Resource Manager


## Development

### Dependencies

Install:

* Python3.8 - https://wiki.python.org/moin/BeginnersGuide/Download

        # For Ubuntu (Python 3.8 is default version):
        sudo apt install python3

* Visual Studio Code - https://code.visualstudio.com/
  * Python extension - https://marketplace.visualstudio.com/items?itemName=ms-python.python
  * Azure tools - https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack
  * Azure functions extension - https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions
* Azure Functions Core Tools - https://github.com/Azure/azure-functions-core-tools/blob/v4.x/README.md#to-install-with-npm

        # Using node on Ubuntu:
        sudo npm i -g azure-functions-core-tools@4 --unsafe-perm true

* Install the Azure CLI on Linux - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux

        # For Ubuntu:
        curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

### Install dependencies and start the function host

```sh
cd src
```

Use the run configuration of the project by clicking "▷ Run and Debug" or execute the following commands:

```sh
# https://docs.python.org/3/tutorial/venv.html
.venv/bin/python -m pip install -r requirements.txt
```

```sh
.venv/bin/activate && func host start
```

### Execute the function locally

Execute the ConcertsApiHandler function from the Azure workspace tab or open [localhost:7071/api/ConcertsApiHandler?artist=Madonna](http://localhost:7071/api/ConcertsApiHandler?artist=Madonna) in the browser.


### Deployment

[Login to Azure](https://rakesh-suryawanshi.medium.com/login-to-azure-subscription-from-vscode-988f82c9eee3) from Visual Studio Code

```sh
# Create a resource group for the deployment
az group create --name "ConcertsDev" --location "germanywestcentral"

# Deploy the application
az deployment group create --resource-group "ConcertsDev" --template-file "azuredeploy.jsonc"

# Zip and deploy the application code
zip -r "ConcertsApiHandler.zip" "./ConcertsApiHandler"
az functionapp deployment source config-zip \
	-g "ConcertsDev" -n "Concerts/ConcertsApiHandler" --src "./ConcertsApiHandler.zip"
```

### Cleanup

```sh
az group delete --name "ConcertsDev"
```


## Resources

* [Login to Azure Subscription from VSCode](https://rakesh-suryawanshi.medium.com/login-to-azure-subscription-from-vscode-988f82c9eee3)
* [Quickstart: Create a function in Azure with Python using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)
* [Tutorial: Create and deploy your first ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template?tabs=azure-powershell)
* [Quickstart: Create and deploy Azure Functions resources from an ARM template](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-resource-manager?tabs=azure-cli)
* [Azure Function app and an HTTP-triggered function](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.web/function-http-trigger)
* [Deploying Azure Functions with the Azure CLI](https://markheath.net/post/deploying-azure-functions-with-azure-cli)
