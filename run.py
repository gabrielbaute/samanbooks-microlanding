from waitress import serve
from landing import create_app
from landing.config import Config

app = create_app()

if __name__ == '__main__':
    #serve(app, host='0.0.0.0', port=5001, threads=10)
    app.run(debug=Config.DEBUG, port=Config.PORT)