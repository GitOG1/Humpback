# app.py (Flask example)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your actual bot logic
def process_message(user_message):
    # Example (very basic)
    return "You said: " + user_message

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid JSON'}), 400  # Bad request

        user_message = data.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400  # Bad request

        bot_reply = process_message(user_message)
        return jsonify({'reply': bot_reply})
    except Exception as e:
        print(f"Error processing message: {e}")  # Print error to console for debugging
        return jsonify({'error': 'An error occurred'}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production