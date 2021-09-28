# Oslo Origo Sample Project
# Author: Karl Mathias Moberg
# License: MIT

import os, requests
from flask import Flask

api = Flask(__name__)


@api.route('/origo', methods=['GET'])
def get_stations():

    # Get API URL from Environment Variable
    api_url = os.getenv('API_URL')

    try:
        stations = requests.get(api_url)
        stations_json_payload = stations.json()

    except:
        print('ERROR: {}'.format())

    return stations_json_payload


if __name__ == '__main__':
    api.run(host="0.0.0.0", debug=True)
