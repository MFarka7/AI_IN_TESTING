from flask import Flask, request, jsonify

app = Flask(__name__)

def sum_to_string(a, b):
    """
    Return the sum of two numbers as a string.

    Example:
        sum_to_string(2, 3) -> "5"
        sum_to_string(2.5, 1.5) -> "4.0"
    """
    try:
        return str(a + b)
    except TypeError:
        raise TypeError("Both arguments must be numbers or support the + operator")

@app.route('/sum', methods=['GET', 'POST'])
def sum_api():
    if request.method == 'POST':
        data = request.get_json()
        a = data.get('a')
        b = data.get('b')
    else:
        a = request.args.get('a')
        b = request.args.get('b')
    try:
        a = float(a)
        b = float(b)
        result = sum_to_string(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide two numbers.'}), 400

def main():
    print(sum_to_string(2, 3))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'api':
        app.run(debug=True)
    else:
        main()
