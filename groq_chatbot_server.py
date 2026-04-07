"""
NVIDIA Chatbot API Wrapper (Rate Limited)
- 39 requests per minute limit
- Uses NVIDIA_API_KEY_V2 environment variable
- Model: meta/llama-3.1-70b-instruct
"""

from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()
app = Flask(__name__)

# Rate limiter: 39 requests per minute
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["39 per minute"],
    storage_uri="memory://"
)

# Initialize NVIDIA client (OpenAI-compatible)
NVIDIA_BASE_URL = "https://api.build.nvidia.com/v1"
nvidia_client = OpenAI(
    base_url=NVIDIA_BASE_URL,
    api_key=os.getenv("NVIDIA_API_KEY_V2")  # Changed to V2
)

# System prompt (same as before)
SYSTEM_PROMPT = """You are a helpful and motivating virtual gym trainer.
You assist users with:
- Workout routines and exercise demonstrations
- Fitness goals (weight loss, muscle gain, endurance, etc.)
- Nutrition and diet tips
- Injury prevention and proper form
- Gym equipment usage and safety

Be encouraging, professional, and concise. Adapt advice to the user's fitness level. Never promote harmful or extreme practices."""

# Fixed model
DEFAULT_MODEL = "meta/llama-3.1-70b-instruct"


@app.route('/chat', methods=['POST'])
@limiter.limit("39 per minute")  # Apply rate limit to this endpoint
def chat():
    """
    Chat endpoint with 39 RPM limit.
    POST /chat
    Body: {"message": "user message here"}
    Response: {"response": "bot response"}
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Call NVIDIA API
        chat_completion = nvidia_client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            model=DEFAULT_MODEL,
            temperature=0.7,
            max_tokens=500,
        )

        bot_response = chat_completion.choices[0].message.content
        return jsonify({"response": bot_response})

    except Exception as e:
        # Catch rate limit errors from the API itself (if any)
        if "rate_limit" in str(e).lower():
            return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "NVIDIA chatbot is running (39 RPM limit)"})


if __name__ == '__main__':
    # Check if API key is set
    if not os.getenv("NVIDIA_API_KEY_V2"):
        print("=" * 50)
        print("⚠️  ERROR: NVIDIA_API_KEY_V2 not set!")
        print("=" * 50)
        print()
        print("Set it with:")
        print("  set NVIDIA_API_KEY_V2=your_key_here   (Windows)")
        print("  export NVIDIA_API_KEY_V2=your_key_here (Linux/Mac)")
        print()
        print("Get your free key from: https://build.nvidia.com")
        print("=" * 50)
        exit(1)

    print("=" * 50)
    print("🤖 NVIDIA Chatbot API Server (Rate Limited: 39 RPM)")
    print("=" * 50)
    print()
    print("Endpoints:")
    print("  POST http://localhost:5000/chat (max 39 calls per minute per IP)")
    print("  GET  http://localhost:5000/health")
    print()
    print("Example request:")
    print('  curl -X POST http://localhost:5000/chat \\')
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"message": "Hello!"}\'')
    print()
    print(f"Using model: {DEFAULT_MODEL}")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    print()

    app.run(host='0.0.0.0', port=5000, debug=False)