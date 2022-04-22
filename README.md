# Chaitanya RASA BOT

# Rasa Deployment
Deploying Rasa Bot over Google Cloud Platform using Docker.

## Prerequisites:
- RASA

## Instructions:

### For installing Depencies on Windows:

### RASA Installation

If python is installed in your system, then pip comes in handy.
So simple steps are:
1) Install virtualenv using

- > pip install virtualenv 

2) Now in which ever directory you are, this line below will create a virtualenv there

 - > virtualenv myenv

And here also you can name it anything instead of myenv.

3) Now if you are same directory then type,

- > myenv\Scripts\activate

4) Upgrade pip (Please use this command in administrator mode)

- > pip install --upgrade pip

5) Install RASA

- > pip install rasa==2.5.0

NOTE : Please check Python version should be 3.7 or greater and pip should be installed previously

If the rasa installation gives error, try this [solution](https://stackoverflow.com/questions/64291087/matplotlib-module-sip-has-no-attribute-setapi)


## Installation Complete

## Get files

To download the RASA files from github run the following command 

- > git clone https://github.com/athenasaurav/Chaitanya.git

Move inside directory

- > cd Chaitanya

Open a new Anaconda Prompt

- > rasa train


## RUN Chatbot

Open one Ananconda prompt and move into ```rikjai``` folder

- > rasa run -m models --enable-api --cors “*” --debug


## Chat with Bot

Click on ```index.html``` in the folder to open in browser and start chatting


