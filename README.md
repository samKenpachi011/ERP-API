# Enterprise Resource Planning App API

## Objectives

## Technologies

s
## Project Structure


## Project Management

1. ### Test Driven Development
- A development practice to write tests for functionalities before implementation
- Example -> /app/sample_cal_test.py has base calculator functions that are documented and the test class in /app/tests.py inherits from the SimpleTestCase classs

## GitHub Actions
### Used to run automated tasks for pushes to the repository
**Use Cases**
 - Running unit tests
 - Code linting
 - Deployment

**On Push Trigger**
 - Run unit tests
 - linting

**checks.yml**
- This file has a job that runs all the steps on a ubuntu machine (ubuntu runner)
- Uses actions that are pre made
- Checks out the code so that its available for linting and running tests
- Should cater for logging into docker hub to push/pull images


## Steps


## Contributions
