from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Ensure JSON data is provided
        data = request.json.get('data', [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid data format. Expected list."}), 400

        # Sample user info
        user_id = "your_fullname_ddmmyyyy"
        email = "your_email@domain.com"
        roll_number = "your_roll_number"
        
        # Processing
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = max(alphabets, key=str.lower) if alphabets else ''
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
