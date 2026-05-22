"""
Backend: Integral Art Generator
Calcula integrales definidas con SymPy y las devuelve al frontend.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sympy as sp
import math
import os

app = Flask(__name__, static_folder='.')
CORS(app)


def parse_and_integrate(func_str: str, a: float, b: float) -> dict:
    x = sp.Symbol('x')
    func_str = func_str.replace('^', '**')
    local_dict = {
        'x': x,
        'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
        'exp': sp.exp, 'log': sp.log, 'ln': sp.log,
        'sqrt': sp.sqrt, 'pi': sp.pi, 'e': sp.E,
        'abs': sp.Abs, 'asin': sp.asin, 'acos': sp.acos,
        'atan': sp.atan, 'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh,
    }
    expr = sp.sympify(func_str, locals=local_dict)
    try:
        integral_result = sp.integrate(expr, (x, a, b))
        area = float(integral_result.evalf())
    except Exception:
        from scipy import integrate as sci_integrate
        f_lambdified = sp.lambdify(x, expr, modules=['numpy'])
        area, _ = sci_integrate.quad(f_lambdified, a, b)
    if math.isnan(area) or math.isinf(area):
        raise ValueError("La integral diverge o no existe en ese intervalo.")
    return {
        "area": area,
        "func_interpreted": str(expr),
        "a": a,
        "b": b
    }


@app.route('/api/integrate', methods=['POST'])
def integrate_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400
    func_str = data.get('func', '').strip()
    a = data.get('a')
    b = data.get('b')
    if not func_str:
        return jsonify({"error": "La función no puede estar vacía"}), 400
    if a is None or b is None:
        return jsonify({"error": "Se requieren los límites a y b"}), 400
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify({"error": "Los límites a y b deben ser números"}), 400
    if a >= b:
        return jsonify({"error": "El límite inferior a debe ser menor que b"}), 400
    try:
        result = parse_and_integrate(func_str, a, b)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Error al calcular la integral: {str(e)}"}), 422


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
