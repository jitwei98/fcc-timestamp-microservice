import datetime
import dateparser
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



'''
Code adapted from
https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
'''
EPOCH = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - EPOCH).total_seconds() * 1000.0



class DateParser(Resource):
    def get(self, date_string=None):
        if not date_string:
            date = datetime.datetime.now()
        else:
            date = dateparser.parse(date_string)
            if date is None: return {"error": "Invalid Date"}

        return {
            'unix': int(unix_time_millis(date)),
            'utc': date.isoformat(' ')
        }

api.add_resource(DateParser,
                 '/api/timestamp/',
                 '/api/timestamp/<date_string>')

if __name__ == '__main__':
    app.run(debug=True)
