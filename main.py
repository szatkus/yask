import config
import registration
__all__ = [registration]

from flask import send_from_directory, render_template

from app import app

@app.route('/')
def root():
    return render_template('index.html', place='hot')

if config.DEVELOPMENT:
    @app.route('/css/<path:path>')
    def send_css(path: str):
        return send_from_directory('css', path)

    @app.route('/images/<path:path>')
    def send_image(path: str):
        return send_from_directory('images', path)

if __name__ == '__main__':
    app.run(debug=config.DEVELOPMENT)
