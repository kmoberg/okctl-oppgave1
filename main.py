# Oslo Origo Sample Project
# Author: Karl Mathias Moberg
# License: MIT

import os, requests, json
from flask import Flask

api = Flask(__name__)


@api.route('/origo', methods=['GET'])
def get_stations():

    # Get API URL from Environment Variable
    api_url = os.getenv('API_URL')

    try:
        stations_raw = requests.get(api_url)

        stations_json_payload = stations_raw.json()

        # The rest here depends on how the tasks should be completed.
        # It's kinda ambigious in the task so either just return the previous variable for the pure, raw code
        # Or if you just want the names of the stations, use the following

        stations_list = stations_json_payload['data']['stations']

        all_stations = []

        for i in range(len(stations_list)):
            all_stations.append(stations_list[i]['name'])

    except:
        print('ERROR: {}'.format())

    return json.dumps(all_stations, ensure_ascii=False).encode('utf8')  # If you want the entire JSON dump and, comment line.

    # Uncomment this if you want to return absolutely everything, raw, then commend the previous line.
    # return stations_json_payload


if __name__ == '__main__':
    api.run(host="0.0.0.0", debug=True)
