# Data-Mining-Term
## Description:
This code loads a pre-trained model for generating a classification of a review for board games.  
Given a review, it spits out a estimated rating using a Naive Bayes Classifier.
## Usage:
Make a post request to the flask url and have the data passed in for the following parameters:
* review (string)  
What is returned:
* Inner HTML value for just a number classifiation of what the review rating should be.
## Deployment Instructions
### Pre-requisites:
* Have a pythonanywhere account:
    * https://www.pythonanywhere.com/
* Basic knowledge of Web requests, and commandline usage.  
### Instructions
* start a new or use a fresh web app using python 3.7
* replace the code inside the flask_app.py with the one from this repository in the Site Folder.
* Go to the consoles tab and open a new BASH shell
* run the following command ``` pip3.7 install --user flask_cors ```
* goto the root directory of the web app. (the root dir, is one directory up from the flask_app.py)
* Inside the Model folder upload the finalized_model.zip file. The pythonanywhere site, has a restriction on upload sizes being less than 100 Mib. So we can't upload the raw, finalized_model.sav due to the size.
* Once the file is uploaded, you should be able to uncomment the commented out code for the zip file and place in the paths to the zipfile you stored.
* Reload the web app. It should now be able to accept POST requests for the model.
* If any issues arise, there should be a link to the error logs from the web app's configuration page.
