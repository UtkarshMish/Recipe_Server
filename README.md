# Recipe_Server

A Flask Server for Recipe Advisor project which utilizes Recommender Engine from lightfm module , and a custom recipe predictor.

## Example Web App

A example of the web app is hosted on url --> http://recipe-advisor.team

## System Requirements

1. Powerful PC running windows or linux or mac (64bit) preferably having more than 2 cores.
2. Python 3.7.7 (64bit)
3. Modern Browser (Google Chrome, Firefox, Vivaldi, Opera GX, etc)

## Steps for running

1. Create a .env with a MongoDB Atlas credentials namely having KEY, HOST and PASSWORD.

### Without using Docker

2. open cmd or terminal in current directory, run `pip install -r requirements.txt`.

3. run `python app.py`.

### Using Docker

2. run in cmd or terminal `docker build -t radvizor:latest .` /_ Notice it has dot in end _/ .

3. run in cmd or terminal `docker run --publish 5000:5000 --name recipe radvizor:latest`

### Common Step

4. Check the app in a browser on `localhost:5000`

5. End by `Ctrl` + `C`.

6. Stop docker image by `docker stop recipe` if using docker.

## References for the App

1. https://heartbeat.fritz.ai/recommender-systems-with-python-part-i-content-based-filtering-5df4940bd831?gi=20f8aad16956
2. https://anvil.works/learn/tutorials/jupyter-notebook-to-web-app
3. https://github.com/Cojacfar/FlaskWeb
4. https://github.com/nytimes/ingredient-phrase-tagger
5. https://github.com/conwayyao/Recipe-Analysis
6. https://github.com/lyst/lightfm
7. Best friend https://www.google.co.in
