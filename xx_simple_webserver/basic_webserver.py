from bottle import route, run, template

@route('/')
@route('/status')
def index():
    return template('<b>Hello World</b>!')



run(host='localhost', port=8080)