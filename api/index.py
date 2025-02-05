from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from flask_talisman import Talisman

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n):
    """Fetch a fun fact about the given number from Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=5)
        if response.status_code == 200:
            return response.json().get("text", "No fact available.")
    except requests.RequestException:
        return "No fact available."
    return "No fact available."

app = Flask(__name__)

# Enable CORS for all API routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Only use HTTPS in production
if __name__ != '__main__':
    Talisman(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """Classify a number based on its mathematical properties."""
    number = request.args.get('number')

    # Validate input
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    num = int(number)
    properties = []

    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 else "even")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
