from flask import Flask, request, jsonify, g
from typing import List
from level_1.challenge import is_mutant
from .db import MutantDatabase

app = Flask(__name__)

def get_db():
    """Obtiene una instancia de la base de datos para la solicitud actual."""
    if 'db' not in g:
        g.db = MutantDatabase(host="18.188.133.85", user="challenge-meli", password="api-mutant", database="challenge-meli")
    return g.db

@app.route('/mutant/', methods=['POST'])
def check_mutant():
    data = request.get_json()
    dna = data.get("dna")

    if not dna or not isinstance(dna, list) or not all(isinstance(seq, str) for seq in dna):
        return jsonify({"error": "Invalid input"}), 400

    db = get_db()  # Obtiene la conexión a la base de datos para esta solicitud

    try:
        if db.dna_exists(dna):
            return jsonify({"message": "DNA already exists"}), 409
        # Verifica si el ADN pertenece a un mutante
        if is_mutant(dna):
            db.saveData(dna, True)
            return jsonify({"message": "Mutant detected"}), 200
        else:
            db.saveData(dna, False)
            return jsonify({"message": "Not a mutant"}), 403
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats', methods=['GET'])
def check_stats():
    db = get_db()  # Obtiene la conexión a la base de datos para esta solicitud

    try:
        stats=db.getStats()
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.teardown_appcontext
def close_connection(exception):
    """Cierra la conexión a la base de datos al finalizar la solicitud"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)
