# botG (Powered by Google) v1.1

Project mainly aims to develop a QABot web application which uses google search results to answer the user queries.
- Using Google API for GooglePalm model.
- LangChain.
- StreamLit for UI.

The application is built and tested in python 3.10 environment.
Project requirements are specified in the requiremetns file.

# Steps to run the project

## 1. Install requirements

Run the below command to install all the required packages for this project(Recommended also to create a new python environment)
```
pip install -r requirements.txt
```

<br>

## 2. Set your API keys

Set your Google API key and Serpai API key in the [apis.py](https://github.com/aabhi02/botG/blob/main/apis.py) file.

<br>

## 3. Run the app.py file using Streamlit command

Run the following command to start the web app
```
streamlit run app.py
```

<br>

And your done!!! Ask the BotG any general questions you want and talk to [GOOGLE](https://www.google.com).