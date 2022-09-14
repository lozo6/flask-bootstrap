from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/shows')
def shows():
    return render_template('shows.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)