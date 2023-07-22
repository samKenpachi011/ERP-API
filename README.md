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

### Database Configuration
- the docker compose configuration add a db service that uses the postgresql database and dev volume
- environment variables are also set for the db on the main service and the db service
**Fixing race condition**
- in core/app/management/commands/ there is a wait_for_postgres_db file to check on the database status
-running the command-> `docker-compose run --rm app sh -c "python manage.py wait_for_postgres_db"`




## Project Management

1. ### Test Driven Development
- A development practice to write tests for functionalities before implementation
- Example -> /app/sample_cal_test.py has base calculator functions that are documented and the test class in /app/tests.py inherits from the SimpleTestCase classs

2. ### Pre-Installs/Configuration
    - Vs-Code / any IDE
    - GIT
    - Set up Docker and Docker-Compose
    - Setup linting
    - Configure Github actions
<br/>

3. ### Documentation
**Developers or any user of our APIs needs to know how to use them.**
- **Documentation is both Manual and Automatic(endpoints) -> tools**
    - [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
    - [DRF Spectacular benefits](https://levelup.gitconnected.com/drf-spectacular-the-ultimate-tool-for-automated-drf-api-documentation-61bd4cca36b7)
    - [Schemas](https://www.django-rest-framework.org/api-guide/schemas/)

- **What we have documented**
    - Available endpoints
    - Application docker configurations
    - Authentication process
    - Endpoint payloads and responses


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
