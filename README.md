# Enterprise Resource Planning App API

## Objectives

## Technologies

s
## Project Structure
- app -> holds all application code
- app/core -> holds all shared code across multiple applications
- app/users -> holds all user related code

**Core App Structure**
- app/core/tests/
- app/core/models
- app/core/admin
- app/core/apps
- app/core/migrations

**User App Structure**
- app/users/tests/
- app/users/serializers
- app/users/view
- app/users/urls
- app/users/admin


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
