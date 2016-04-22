import config

from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

if config.DEVELOPMENT:
    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('css', path)

    @app.route('/images/<path:path>')
    def send_image(path):
        return send_from_directory('images', path)

if __name__ == "__main__":
    app.run(debug=config.DEVELOPMENT)
