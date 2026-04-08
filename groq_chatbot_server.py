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
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"  # Fixed: was api.build.nvidia.com
# Use NVIDIA_API_KEY_V2 for chatbot server (separate from NVIDIA_NIM_API_KEY used by judge)
api_key = os.getenv("NVIDIA_API_KEY_V2") or os.getenv("NVIDIA_NIM_API_KEY")
nvidia_client = OpenAI(
    base_url=NVIDIA_BASE_URL,
    api_key=api_key
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

# Working models (all tested and confirmed):
DEFAULT_MODEL = "meta/llama-3.1-8b-instruct"  # Fast, smaller model (recommended)
# DEFAULT_MODEL = "meta/llama-3.1-70b-instruct"  # Larger, more capable
# DEFAULT_MODEL = "meta/llama3-8b-instruct"  # Llama 3 (previous version)
# DEFAULT_MODEL = "mistralai/mistral-7b-instruct-v0.3"  # Mistral alternative


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
    api_key = os.getenv("NVIDIA_NIM_API_KEY") or os.getenv("NVIDIA_API_KEY_V2")
    if not api_key:
        print("=" * 50)
        print("⚠️  ERROR: No NVIDIA API key found!")
        print("=" * 50)
        print()
        print("Set one of these in .env file:")
        print("  NVIDIA_NIM_API_KEY=your_key_here")
        print("  NVIDIA_API_KEY_V2=your_key_here")
        print()
        print("Get your free key from: https://build.nvidia.com")
        print("=" * 50)
        exit(1)

    key_type = "NVIDIA_NIM_API_KEY" if os.getenv("NVIDIA_NIM_API_KEY") else "NVIDIA_API_KEY_V2"
    
    print("=" * 60)
    print("🤖 NVIDIA Chatbot API Server (Rate Limited: 39 RPM)")
    print("=" * 60)
    print()
    print(f"✓ Using: {key_type}")
    print(f"✓ API Key: {api_key[:10]}...{api_key[-4:]}")
    print(f"✓ Endpoint: {NVIDIA_BASE_URL}")
    print(f"✓ Model: {DEFAULT_MODEL}")
    print()
    print("Endpoints:")
    print("  POST http://localhost:5000/chat (max 39 calls/min per IP)")
    print("  GET  http://localhost:5000/health")
    print()
    print("Example request:")
    print('  curl -X POST http://localhost:5000/chat \\')
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"message": "Hello!"}\'')
    print()
    print("Press Ctrl+C to stop")
    print("=" * 60)
    print()

    app.run(host='0.0.0.0', port=5000, debug=False)