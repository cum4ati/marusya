from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/skill', methods=['POST'])
def skill():
    data = request.json
    if 'вездекод' in list(map(lambda x: x.lower(), data['request']['original_utterance'])) and 'камчаты' in list(
            map(lambda x: x.lower(),
                data[
                    'request'][
                    'original_utterance'])):
        response = {}
        response['version'] = data['version']
        response['session'] = data['session']
        response['response'] = {'end_session': False, 'text': 'Привет вездекодерам!'}
        return jsonify(response)
    else:
        response = {}
        response['version'] = data['version']
        response['session'] = data['session']
        response['response'] = {'end_session': False,
                                'text': 'Чтобы я вам сказала привет, назовите вашу команду и передайте привет мне(камчаты привет)'}
        return jsonify(response)


if __name__ == '__main__':
    app.run()
