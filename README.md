# Introduction  
Ths is a foundational web application that demonstrates core functionalities  
pertinant to a fitness and gym management system.  
  
# Version control  
The main branch is where the release codeides. When an release happens the  
Github Actions tag that main brach point with version number (v1, v2, v3 etc).  
Contributors creates branches from main and when ready create an MR to main.  
  
# Unit testing framework  
Unit testing is implemented using python module unittest. It mainly uses  
mock and patch from this module. While writing unit tests care needs to be  
taken not to invoke tkinter GUI display sice the tests will be run in  
Github Actions and no display is available in this CICD.  
  
# Automated testing configuration  
Testing will automatically triggered whenever a merge happens to main branch.  
If the test fails the Github actions pipeline will be failed and no container  
image will be created. Successfull test execution will result in a docker image  
creation and push to docker hub.  
  
# Containerization with Docker  
If the automated tests are all passed then Github actions create a docker image  
and push to docker hub. Image uses python:3.9-slim base image and installs  
all pre requisites python and tinker libraries. However the image does not have  
an entry point. This is beacuse this is a GUI application and we cannot run it  
during Github Actions since there is no display available. In production after  
deploying image the application needs to be started as an additional step. Use  
operational tools to automate this.  
  
# CICD Pipeline  
Test and build is automated through a CICD pipeline. Github Actions is used to  
implement the CICD pipelines and is configured to run automatically whenever a  
merge to main branch happens. This pipeline first build a docker image and run  
defined tests. If the tests fail the pipeline also fails and exits. If the tests  
are successfull, then the pipeline tag the main branch of the repository then  
creates a docker image and push it to docker hub with the same tag as that created  
for the branch. These tags serve as release versions.  
  
| Item | Location |
|:---|:---|
| Application code | ACEest_Fitness.py |
| Unit test code | test_ACEest_Fitness.py |
| Image build code | Dockerfile |
| CICD code | .github/workflows/buildimage.yml |
