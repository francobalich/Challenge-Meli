import sys
import os
from flask import Flask, request, jsonify
from typing import List
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../level-1')))
from challenge import is_mutant

app = Flask(__name__)

@app.route('/mutant/', methods=['POST'])
def check_mutant():
    data = request.get_json()
    dna = data.get("dna")

    if not dna:
        return jsonify({"error": "Invalid input"}), 400

    if is_mutant(dna):
        return jsonify({"message": "Mutant detected"}), 200
    else:
        return jsonify({"message": "Not a mutant"}), 403

if __name__ == '__main__':
    app.run(debug=True)
