# Enterprise Resource Planning App API

## Objectives

## Technologies


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


1. ### User App endpoints

2. ### User App authentication
**Authentication method -> Token Authentication**
- [Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
- Helps avoid using email and password authentication on each request

**Personnel App Structure**
- app/personnel/tests/
- app/personnel/serializers
- app/personnel/view
- app/personnel/urls


1. ### Personnel App endpoints

2. ### URLs
- The router will automatically generate the following URL patterns for the DepartmentViewSet:

   - List View: /department/ (HTTP GET)
   - Create View: /department/ (HTTP POST)
   - Detail View: /department/<pk>/ (HTTP GET, HTTP PUT, HTTP PATCH, HTTP DELETE)
   - Update View: /department/<pk>/ (HTTP PUT, HTTP PATCH)
   - Delete View: /department/<pk>/ (HTTP DELETE)
   - The router.register() method with the basename, one can easily set up the URL patterns for the view set without having to manually define them in the urls.py file.

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
