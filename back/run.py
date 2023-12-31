"""Run Server
"""
from src import create_app

app = create_app()

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(host='0.0.0.0', port=8000, debug=True)
