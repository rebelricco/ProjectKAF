from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort
import ActualCoffeMachine.DoStuff as Do
import json
import time
import smbus


app = Flask(__name__)




@app.route('/', methods=['GET'])
def default():
    return 'Dav, du skal nok lige skrive URl´en rigtigt..';


@app.route('/Kaffe', methods=['POST'])
def make_Kaf():
    getTimeSettingsFile = open("settings.KAF", "r+");
    rawJsonStringFromSettingsFile = getTimeSettingsFile.read();
    getTimeSettingsFile.close();
    parsedJsonFile = json.loads(rawJsonStringFromSettingsFile);

    Status = Do.lav_kaffe(parsedJsonFile['kopper']);
    return jsonify({'KAF': Status}), 201


@app.route('/KaffeSenere', methods=['POST'])
def make_Kaf_Delayed():
    if not request.json or not 'Kop' in request.json or not 'Time' in request.json:
        abort(400)
    setting_file = open("delayed.KAF", "w+");
    json.dump(request.json, setting_file);
    setting_file.close();
    return "Makeing KAF soon TM";


@app.route('/Settings', methods=['POST'])
def update_Settings():
    setting_file = open("settings.KAF", "w+");
    json.dump(request.json, setting_file);
    setting_file.close();
    return "Settings Updated";


@app.route('/Settings', methods=['GET'])
def get_Settings():
    setting_file = open("settings.KAF", "r+");
    returnjsonstring = setting_file.read();
    setting_file.close();
    return returnjsonstring;



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Method not Found'}), 404)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port= int('1337'), debug=True)
