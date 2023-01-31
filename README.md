# Mortgage Calculator

## Description

A simple mortgage calculator, with a small frontend to interact with.\
User will provide parameters to the API, and get the calculated payment figure, with a200 status code.\
Both frontend and backend will check for valid inputs. \
For invalid inputs, API will return error message with 400 status code, and users will be alerted for the invalid ones.

## Project Structure
1. Frontend - React
2. Backend - Flask
3. For simplicity, both frontend and backend are in a same project

## (optional) Enter virtual environment
1. If not in virtual environment already, cd into /Produce8_assessment/
2. run `venv\Scripts\activate`

## How to run locally (backend)
1. Open a separate terminal
2. cd into /Produce8_assessment/backend
3. run `pip install -r requirements.txt` , , it will take a few minutes to install packages
4. run `flask run`
5. visit `http://127.0.0.1:5000`
6. If you see "Hello World", it is running properly

## How to run locally (frontend)
1. Open a separate terminal
2. cd into /Produce8_assessment/frontend/mortgage-calculator
3. run `yarn` , it will take a few minutes to install packages
4. run `yarn start`
5. visit http://127.0.0.1:3000/
6. If you see a mortgage calculator form, it is running properly
7. Try give it a few numbers and submit

## How to test
1. cd into /Produce8_assessment/backend
2. run `python -m pytest`
