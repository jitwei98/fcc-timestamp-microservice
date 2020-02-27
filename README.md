# fcc-timestamp-microservice

A microservice that converts date strings to 
* microseconds from epoch
* utc string

Requirements from https://www.freecodecamp.org/learn/apis-and-microservices/apis-and-microservices-projects/timestamp-microservice

## Running in development mode
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python api.py
```
Access the microservice at http://127.0.0.1:5000/


## Usage

/api/timestamp/
```
// Current time and date
{
    "unix": 1582824290265,
    "utc": "2020-02-27 17:24:50.265376"
}
```

/api/timestamp/1450137600

```
{
    "unix": 1450166400000,
    "utc": "2015-12-15 08:00:00"
}
```

/api/timestamp/2015-12-25
```
{
    "unix": 1451001600000,
    "utc": "2015-12-25 00:00:00"
}
```
