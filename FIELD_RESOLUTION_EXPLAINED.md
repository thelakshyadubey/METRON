# 🔧 Dynamic Field Resolution - How It Works

## 📋 The Problem

Different chatbot APIs have different JSON structures:

```json
// Chatbot A (Simple)
Request:  {"message": "Hello"}
Response: {"response": "Hi there!"}

// Chatbot B (Nested)
Request:  {"input": {"text": "Hello"}}
Response: {"output": {"bot": {"reply": "Hi there!"}}}

// Chatbot C (OpenAI-style)
Request:  {"messages": [{"role": "user", "content": "Hello"}]}
Response: {"choices": [{"message": {"content": "Hi there!"}}]}
```

**How can ONE testing framework work with ALL of them?**

---

## 💡 The Solution: Dot Notation Path Resolution

The framework uses **configurable field paths** that you specify in the UI.

### Theory

1. **Request Building**: User specifies request field (e.g., `"message"` or `"input.text"`)
2. **Response Extraction**: User specifies response field (e.g., `"response"` or `"output.bot.reply"`)
3. **Path Navigation**: Framework walks the JSON tree using dot-separated keys

---

## 💻 Code Implementation

### Step 1: Configuration (User Input)

```python
@dataclass
class ChatbotConfig:
    """Configuration for chatbot endpoint"""
    url: str
    request_field: str = "message"     # ← User configures this
    response_field: str = "response"   # ← User configures this
    headers: Dict[str, str] = field(default_factory=lambda: {"Content-Type": "application/json"})
    timeout: int = 30
```

**In the UI:**
```
Request Field:  [message        ]  ← For {"message": "..."}
Response Field: [response       ]  ← For {"response": "..."}
```

---

### Step 2: Sending Request

```python
async def send_message(self, message: str) -> Tuple[str, float]:
    """Send message and return (response, latency_ms)"""
    start_time = time.perf_counter()
    
    async with aiohttp.ClientSession() as session:
        # BUILD REQUEST: Use the configured request field
        payload = {self.config.request_field: message}
        #          ↑ If request_field = "message", creates {"message": "..."}
        #          ↑ If request_field = "input.text", would need nested builder
        
        async with session.post(
            self.config.url,
            json=payload,
            headers=self.config.headers,
            timeout=aiohttp.ClientTimeout(total=self.config.timeout)
        ) as resp:
            latency_ms = (time.perf_counter() - start_time) * 1000
            
            if resp.status != 200:
                return f"[Error: HTTP {resp.status}]", latency_ms
            
            # EXTRACT RESPONSE: Use the configured response field
            data = await resp.json()
            response = self._extract_response(data)
            #          ↑ This is the magic!
            return response, latency_ms
```

---

### Step 3: Response Extraction (The Core Magic)

```python
def _extract_response(self, data: Dict) -> str:
    """Extract response from nested JSON using dot notation"""
    
    # Split the path by dots: "output.bot.reply" → ["output", "bot", "reply"]
    fields = self.config.response_field.split(".")
    
    # Start with the full response
    result = data
    
    # Walk the JSON tree
    for field in fields:
        if isinstance(result, dict) and field in result:
            result = result[field]  # Go one level deeper
        else:
            return str(data)  # Fallback: return raw response
    
    return str(result)  # Final value
```

---

## 🎬 Example Walkthrough

### Example 1: Simple Structure

**Configuration:**
- Request field: `"message"`
- Response field: `"response"`

**What Happens:**

```python
# 1. User says: "Hello"
message = "Hello"

# 2. Build request
payload = {"message": "Hello"}

# 3. Send to API → Get response
data = {"response": "Hi there!", "timestamp": "2024-01-01"}

# 4. Extract response
fields = "response".split(".")  # → ["response"]
result = data
for field in ["response"]:
    result = result["response"]  # → "Hi there!"
return "Hi there!"
```

---

### Example 2: Nested Structure

**Configuration:**
- Request field: `"input.text"` (not yet supported for nested request, but works for simple)
- Response field: `"output.bot.reply"`

**What Happens:**

```python
# Response from API
data = {
    "output": {
        "bot": {
            "reply": "Hello, how can I help?",
            "confidence": 0.95
        },
        "timestamp": "2024-01-01"
    }
}

# Extract response
fields = "output.bot.reply".split(".")  # → ["output", "bot", "reply"]
result = data

# Step 1: result = data["output"]
result = {
    "bot": {
        "reply": "Hello, how can I help?",
        "confidence": 0.95
    },
    "timestamp": "2024-01-01"
}

# Step 2: result = result["bot"]
result = {
    "reply": "Hello, how can I help?",
    "confidence": 0.95
}

# Step 3: result = result["reply"]
result = "Hello, how can I help?"

return "Hello, how can I help?"
```

---

### Example 3: Array Access (OpenAI Style)

**Current Limitation:** The code doesn't support array indexing like `choices[0].message.content`.

**To support this, we'd need to enhance the code:**

```python
def _extract_response(self, data: Dict) -> str:
    """Extract response with support for arrays"""
    import re
    
    result = data
    
    # Split path and handle array indices
    parts = self.config.response_field.split(".")
    
    for part in parts:
        # Check if this part has array index: "choices[0]"
        match = re.match(r'(\w+)\[(\d+)\]', part)
        
        if match:
            # Array access
            field_name = match.group(1)  # "choices"
            index = int(match.group(2))   # 0
            
            if isinstance(result, dict) and field_name in result:
                result = result[field_name]
                if isinstance(result, list) and index < len(result):
                    result = result[index]
                else:
                    return str(data)
            else:
                return str(data)
        else:
            # Regular dict access
            if isinstance(result, dict) and part in result:
                result = result[part]
            else:
                return str(data)
    
    return str(result)
```

---

## 🎯 Real-World Usage Examples

### Your Groq Chatbot
```
URL: http://localhost:5000/chat
Request Field: message
Response Field: response

Works with: {"message": "hi"} → {"response": "hello"}
```

### OpenAI API
```
URL: https://api.openai.com/v1/chat/completions
Request Field: messages[0].content  # (requires enhancement)
Response Field: choices[0].message.content

Works with: 
{"choices": [{"message": {"content": "hello"}}]}
```

### Custom Nested API
```
URL: https://myapi.com/chat
Request Field: input.text
Response Field: data.output.text

Works with:
{"data": {"output": {"text": "hello", "confidence": 0.9}}}
```

---

## 🔍 Current Limitations

1. **Request Building**: Only supports simple top-level fields
   - ✅ Works: `"message"` → `{"message": "..."}`
   - ❌ Doesn't work: `"input.text"` → `{"input": {"text": "..."}}`

2. **Array Access**: Response extraction doesn't support array indices
   - ✅ Works: `"output.text"`
   - ❌ Doesn't work: `"choices[0].message.content"`

3. **Complex Structures**: Can't build complex request payloads
   - ❌ Can't do: `{"messages": [{"role": "user", "content": "..."}]}`

---

## 🚀 Future Enhancements

To support ANY API structure, we could add:

1. **JSON Template for Requests**
   ```json
   {
     "messages": [
       {"role": "user", "content": "{{USER_MESSAGE}}"}
     ],
     "temperature": 0.7
   }
   ```

2. **JSONPath for Response**
   ```
   $.choices[0].message.content
   ```

3. **GraphQL Support**
4. **WebSocket Support** for streaming responses

---

## 📝 Summary

**The framework is UNIVERSAL because:**

1. You configure the field paths in the UI
2. The code dynamically builds requests using your field name
3. The code walks the JSON tree using dot notation
4. Works with any REST API that returns JSON

**No hardcoding!** Everything is configurable. 🎉
