from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/taxa', methods=['GET'])
def get_taxa():
    return jsonify({"taxa": 12.5})


if __name__ == '__main__':
    app.run(port=5000)
