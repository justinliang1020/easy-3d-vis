from flask import Flask
from flask import send_file
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "assets/mic.npz"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000,debug=True)