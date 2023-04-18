# Selenium automation
This Readme will take you through how to set up the e2e test suite. 
You will need the following installed:
- PyCharm
- Python

# Setup with terminal and run tests
```shell
# Navigate to the repo in Terminal
# Setup the Python environment
$ python -m venv venv
$ .\venv\Scripts\activate
(venv) $ pip install -r requirements.txt


```
# Running tests
There are two arguments that you need to set if you want to run against Selenium Grid
and don't want to run against Chrome.
- `local` will run the end-to-end tests locally on your machine through Selenium
- `browser` sets the browser that you want to run the tests against. 
- For running locally, only three browsers will work `chrome`, `firefox`, and `edge`.
- If this argument isn't included when running the tests, the default is to run the tests in Chrome.


Example of Local testing with Firefox:
```python
pytest --runner=local --browser=firefox
```

# More helpful resources
- Page Object Model: https://www.pluralsight.com/guides/getting-started-with-page-object-pattern-for-your-selenium-tests
- Pytest-bdd docs: https://pytest-bdd.readthedocs.io/en/stable/
- Python Selenium docs: https://selenium-python.readthedocs.io/api.html
- Selenium docs: https://www.selenium.dev/documentation/
- Setup venv on Win 10: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/
- https://medium.com/@dev.jhesed/how-to-install-and-setup-pycharm-and-venv-in-windows-10-d4af56399b00


##  Selenium Grid on a Windows machine:
- Install Java Development Kit (JDK) on your Windows machine. You can download the latest version from the official website of Oracle.
- Download the Selenium standalone server jar file from the official Selenium website.
- Open the command prompt and navigate to the folder where you have downloaded the Selenium standalone server jar file.
- Start the Selenium hub by running the following command:
```shell
    java -jar selenium-server-standalone.jar -role hub
```
- By default, the hub will start on port 4444. You can verify this by opening a web browser and entering the following URL:
```shell
    http://localhost:4444/grid/console
```
- You should see a console with no registered nodes.
- Start the Selenium node by running the following command:
```shell
    java -jar selenium-server-standalone.jar -role node -hub http://localhost:4444/grid/register
```
- This command will register the node with the hub running on the same machine.
- Once the node is registered successfully, you can see it in the console by refreshing the following URL in the web browser:
```shell
    http://localhost:4444/grid/console
```
- You can use the Selenium Grid to execute your tests on multiple machines and browsers by specifying the remote URL in your Selenium code.
