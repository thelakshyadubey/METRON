# 🔮 AI Agent Tester - Professional Edition

*100% Custom Automated Testing Tool for AI Chatbots & RAG Agents*

---

## ✨ Features

- **Standard Testing** - Test chatbots with 10 pre-built personas
- **RAG Testing** - Test RAG agents with ground truth validation
- **Auto-Generate** - AI creates personas & scenarios from your documents
- **Hallucination Detection** - Catch factual errors automatically
- **LLM Judge** - AI evaluates response quality
- **Multi-Provider** - Groq, Gemini, NVIDIA NIM support
- **Analytics Dashboard** - Track quality trends over time
- **Export** - JSONL, CSV, JSON formats

---

## 🚀 Quick Start

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Set API Keys (.env)
```
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key
```

### 3. Run
```bash
streamlit run app.py
```

---

## 📚 RAG Testing (New!)

Test RAG (Retrieval-Augmented Generation) agents with ground truth validation.

### How It Works:

1. **Upload Ground Truth** - Paste or upload your knowledge base (TXT, PDF)
2. **Describe Agent** - Tell us what your RAG agent does
3. **Auto-Generate** - AI creates relevant personas & test scenarios
4. **Run Tests** - Test against ground truth for accuracy
5. **Detect Hallucinations** - Judge catches fabricated information

### RAG Judge Evaluates:
- ✅ Factual accuracy against ground truth
- ✅ Hallucination detection
- ✅ Appropriate uncertainty ("I don't know" when needed)
- ✅ Response completeness

### Example Scenarios Generated:
- **Factual** - Questions directly answerable from docs
- **Inference** - Questions requiring synthesis
- **Edge Cases** - Boundary questions
- **Out-of-Scope** - Questions agent should refuse
- **Adversarial** - Testing hallucination resistance

---

## 🎭 Standard Testing

### 10 Built-in Personas:

**Standard Users (5):**
- 👤 Normal User - Basic questions
- 😠 Frustrated Customer - Angry, demanding
- 🤔 Confused Beginner - Needs simple explanations
- 🧑‍💻 Technical Expert - Detailed questions
- ⚡ Impatient User - Wants quick answers

**Adversarial Attackers (5):**
- 🔓 Jailbreak Attacker - Bypass safety
- 💉 Prompt Injector - Inject malicious prompts
- 🕵️ PII Extractor - Extract private info
- ☠️ Toxic User - Offensive behavior
- 🎭 Social Engineer - Manipulation tactics

---

## 🔌 Connect Your Chatbot

Your chatbot needs a simple REST API:

```json
POST http://your-api.com/chat
Body: {"message": "user question"}
Response: {"response": "bot answer"}
```

Configure in sidebar:
- API URL
- Request/Response field names
- Authentication (optional)

---

## 📊 What You Get

### Test Results:
- ✅ Pass/Fail status
- 📊 Judge score (0-100%)
- 💬 Conversation transcript
- ⏱️ Response time
- 🔍 Hallucinations detected (RAG)
- 📝 Detailed judge reasoning

### Analytics:
- Pass rate trends
- Failure patterns by persona
- Performance over time

### Export Formats:
- JSONL (for fine-tuning)
- CSV (spreadsheet)
- JSON (API integration)

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `app.py` | Main application (~1800 lines) |
| `groq_chatbot_server.py` | Sample test chatbot |
| `requirements.txt` | Dependencies |
| `.env` | API keys |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│           Streamlit UI                       │
│   [Standard Tests] [RAG Tests] [Analytics]   │
└──────────────────┬──────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ↓              ↓              ↓
┌────────┐   ┌──────────┐   ┌─────────────┐
│ User   │   │ Chatbot  │   │ RAG Judge   │
│ Sim    │ ↔ │ API      │ → │ (Ground     │
│ (LLM)  │   │ Adapter  │   │  Truth)     │
└────────┘   └──────────┘   └─────────────┘
                                  │
                                  ↓
                   ┌─────────────────────────┐
                   │ SQLite Analytics DB     │
                   └─────────────────────────┘
```

---

## 💡 Example: RAG Testing

**Setup:**
- Ground Truth: Product documentation PDF
- Agent: Customer support for TechCorp

**Auto-Generated Test:**
```
Persona: 📊 Data Analyst (Expert)
Scenario: [FACTUAL] Ask about API rate limits

Question: "What are the rate limits for the enterprise API tier?"

Expected: Agent should answer from documentation
```

**Result:**
```
✅ PASSED - Score: 95%

✅ Factually accurate - Matched documentation
✅ No hallucinations detected
✅ Complete response with relevant details
⚠️ Minor: Could mention documentation section
```

---

## 🛠️ Configuration

### Environment Variables (.env):
```
GROQ_API_KEY=gsk_xxx          # Groq (free, fast)
GEMINI_API_KEY=xxx            # Google Gemini
NVIDIA_NIM_API_KEY=xxx        # NVIDIA NIM (optional)
```

### Supported LLM Providers:
- **Groq** - Free, very fast (recommended)
- **Gemini** - Google's models
- **NVIDIA NIM** - Enterprise models

---

## 📞 Checklist

- [ ] `pip install -r requirements.txt`
- [ ] Set API keys in `.env`
- [ ] `streamlit run app.py`
- [ ] Enter chatbot API URL
- [ ] **Standard:** Select personas & scenarios
- [ ] **RAG:** Upload ground truth, generate test cases
- [ ] Enable Judge
- [ ] Run Tests!

---

**Built with ❤️ - 100% Custom, No External Testing Libraries**
