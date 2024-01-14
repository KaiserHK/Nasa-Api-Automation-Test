# Nasa-Api-Automation-Test
This repository contains some demo code for API testing NASA's Asteroid - Near Earth Object Web Service (NeoWs) RESTful API. This API allows it's users to query the NASA JPL Asteroid Team dataset to get information on tracked asteroids and their approach to Earth. Here is a link to the NASA Open API page, where one can find the Asteroids - NeoWs endpoint: https://api.nasa.gov/

# Technologies
For this project, I chose to utilize Python (3.12.1) with the following modules:
- PyTest
- Requests

# How to Install and Run
1. Install Python (I used Python 3.12.1 for this project).
2. Setup virtual environment by running "python -m venv {project root path}" in the command line.
3. Activate the virtual environment by running "{path to venv folder}\Scripts\Activate".
4. Install the required module by running "pip install {pytest/requests}" while the virtual environment is activated.
5. Clone/Download the code in this repo (I recommend storing the tests.py and test_requests.py files right next to the virtual environment folder).
6. Navigate to the project folder that contains the test files.
7. Run the test.py file from the command line by running "pytest tests.py {options}".
