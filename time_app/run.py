from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    return {"current_time": datetime.datetime.now().isoformat()}

app.run(host='0.0.0.0',
        port=8080,
        debug=True)



