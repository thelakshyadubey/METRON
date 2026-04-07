# 🏗️ AI Agent QA Suite - Architecture Diagram

## 📊 High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            🎯 AI AGENT QA SUITE v2.0                                │
│                         Professional AI Testing Framework                           │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────────┐       ┌───────────────────┐       ┌───────────────────┐
│   📡 ENDPOINT     │       │   🤖 LLM LAYER    │       │   🎯 TARGET       │
│   CONFIGURATION   │       │   (Judge/Sim)     │       │   CHATBOT         │
│                   │       │                   │       │                   │
│ • API URL         │       │ • Groq            │       │ • Any REST API    │
│ • Request Field   │       │ • Google Gemini   │       │ • Configurable    │
│ • Response Field  │       │ • NVIDIA NIM      │       │ • HTTP/HTTPS      │
│ • Auth Headers    │       │                   │       │                   │
└───────────────────┘       └───────────────────┘       └───────────────────┘
        │                               │                               │
        └───────────────────────────────┼───────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              🧪 TESTING ENGINE                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │
│  │ Functional  │  │  Security   │  │ Performance │  │    Load     │                │
│  │  Testing    │  │  Testing    │  │  Testing    │  │  Testing    │                │
│  │             │  │             │  │             │  │             │                │
│  │ • Personas  │  │ • Attacks   │  │ • Latency   │  │ • Concurrent│                │
│  │ • Scenarios │  │ • Jailbreak │  │ • P50/P95   │  │ • Stress    │                │
│  │ • RAG Tests │  │ • Injection │  │ • Throughput│  │ • Ramp-up   │                │
│  │ • 16 Cats   │  │ • Compliance│  │ • Metrics   │  │ • Users     │                │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘                │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              📊 RESULTS & REPORTING                                  │
│                                                                                      │
│  • Test Results Summary       • Pass/Fail Metrics        • Export (JSON/CSV)        │
│  • Category Breakdown         • Latency Statistics       • Compliance Reports       │
│  • Critical Failures          • RAG Accuracy             • Historical Data          │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                  DATA FLOW                                            │
└──────────────────────────────────────────────────────────────────────────────────────┘

  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
  │   USER      │         │   SEED      │         │   GROUND    │
  │   CONFIG    │         │   DATA      │         │   TRUTH     │
  │             │         │             │         │   (RAG)     │
  └──────┬──────┘         └──────┬──────┘         └──────┬──────┘
         │                       │                       │
         │    ┌──────────────────┴──────────────────┐   │
         │    │                                      │   │
         ▼    ▼                                      ▼   ▼
  ┌─────────────────┐                      ┌─────────────────┐
  │  CHATBOT        │                      │  LLM GENERATOR  │
  │  ADAPTER        │                      │                 │
  │                 │                      │ • Personas      │
  │ • URL Config    │                      │ • Scenarios     │
  │ • Field Mapping │                      │ • RAG Questions │
  │ • Auth Headers  │                      │                 │
  └────────┬────────┘                      └────────┬────────┘
           │                                        │
           │         ┌──────────────────────────────┘
           │         │
           ▼         ▼
    ┌─────────────────────┐
    │   TEST EXECUTOR     │
    │                     │
    │  ┌───────────────┐  │
    │  │ User Message  │  │◄──── LLM Simulator
    │  │ Generator     │  │
    │  └───────┬───────┘  │
    │          │          │
    │          ▼          │
    │  ┌───────────────┐  │
    │  │ Send to       │──┼──────► Target Chatbot API
    │  │ Chatbot       │  │              │
    │  └───────┬───────┘  │              │
    │          │          │              │
    │          ▼          │◄─────────────┘
    │  ┌───────────────┐  │        Response
    │  │ Receive       │  │
    │  │ Response      │  │
    │  └───────┬───────┘  │
    │          │          │
    │          ▼          │
    │  ┌───────────────┐  │
    │  │ LLM Judge     │  │◄──── Evaluation Criteria
    │  │ Evaluation    │  │
    │  └───────┬───────┘  │
    │          │          │
    └──────────┼──────────┘
               │
               ▼
    ┌─────────────────────┐
    │   TEST RESULTS      │
    │                     │
    │ • Score (0-1)       │
    │ • Passed/Failed     │
    │ • Checks List       │
    │ • Judge Reasoning   │
    │ • Latency Metrics   │
    └─────────────────────┘
```

---

## 🧩 Module Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                  FILE STRUCTURE                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘

AI_QA_Agent/
│
├── 📄 app_v2.py                    # Main Application (Streamlit UI)
│   │
│   ├── 🔧 Configuration Layer
│   │   ├── AppConfig              # Central config (defaults, paths)
│   │   ├── ChatbotConfig          # Endpoint configuration
│   │   ├── AgentSeedData          # Agent description & RAG docs
│   │   └── LLM_PROVIDERS          # Groq, Gemini, NVIDIA registry
│   │
│   ├── 🎭 Persona Layer
│   │   ├── Persona                # Test persona dataclass
│   │   ├── FUNCTIONAL_PERSONAS    # Default functional personas (5)
│   │   ├── SECURITY_PERSONAS      # Attack personas (5)
│   │   └── generate_personas_from_seed()  # Dynamic generation
│   │
│   ├── 🤖 LLM Layer
│   │   ├── call_llm()             # Unified LLM call with retry
│   │   ├── simulate_user_message() # Generate user messages
│   │   ├── evaluate_conversation() # Judge evaluation
│   │   └── evaluate_rag_response() # RAG accuracy check
│   │
│   ├── 📡 Adapter Layer
│   │   └── ChatbotAdapter         # Universal API adapter
│   │       ├── send_message()     # Send to any API
│   │       ├── _extract_response() # Dot-notation field extraction
│   │       └── health_check()     # Connection test
│   │
│   ├── 🧪 Test Runners
│   │   ├── run_functional_test()  # Persona-based tests
│   │   ├── run_security_test()    # Adversarial tests
│   │   ├── run_performance_test() # Latency/throughput
│   │   └── run_load_test()        # Concurrent users
│   │
│   └── 📊 UI Layer (Streamlit)
│       ├── Sidebar Configuration
│       ├── Tab: Functional Testing
│       ├── Tab: Security Testing
│       ├── Tab: Performance Testing
│       ├── Tab: Load Testing
│       └── Tab: Results & Export
│
├── 📄 functional_tests.py          # Comprehensive Functional Tests
│   │
│   ├── TestCategory (Enum)         # 9 test categories
│   ├── FunctionalTest (Dataclass)  # Test definition
│   ├── FunctionalTestResult        # Test result
│   │
│   ├── Test Suites:
│   │   ├── INPUT_HANDLING_TESTS    # 7 tests
│   │   ├── STATE_KNOWLEDGE_TESTS   # 4 tests
│   │   ├── REASONING_TESTS         # 5 tests
│   │   ├── OUTPUT_GENERATION_TESTS # 5 tests
│   │   ├── CONVERSATION_TESTS      # 5 tests
│   │   ├── ERROR_HANDLING_TESTS    # 3 tests
│   │   ├── SAFETY_TESTS            # 4 tests
│   │   ├── SCENARIO_TESTS          # 4 tests
│   │   └── PERSISTENCE_TESTS       # 2 tests
│   │
│   └── evaluate_functional_test()  # LLM judge for tests
│
├── 📄 adversarial_fixtures.py      # Security Test Fixtures
│   │
│   ├── JAILBREAK_ATTACKS           # 5 jailbreak attempts
│   ├── PROMPT_INJECTIONS           # 5 injection attacks
│   ├── DATA_EXTRACTION             # 5 data leak attempts
│   ├── HARMFUL_CONTENT             # 5 harmful requests
│   └── SOCIAL_ENGINEERING          # 5 manipulation attempts
│
├── 📄 adversarial_generator.py     # Dynamic Attack Generator
│   │
│   ├── MUTATION_TECHNIQUES         # 7 attack mutation methods
│   ├── generate_adversarial_prompt() # LLM-based attack generation
│   └── evaluate_response_with_rubric() # 100-point security rubric
│
├── 📄 groq_chatbot_server.py       # Example Test Chatbot
│
└── 📄 .env                         # API Keys
    ├── GROQ_API_KEY
    ├── GEMINI_API_KEY
    └── NVIDIA_NIM_API_KEY
```

---

## 🔌 Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           COMPONENT INTERACTIONS                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────────┐
                              │    STREAMLIT UI     │
                              │     (app_v2.py)     │
                              └──────────┬──────────┘
                                         │
           ┌────────────────┬────────────┼────────────┬────────────────┐
           │                │            │            │                │
           ▼                ▼            ▼            ▼                ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │   Seed      │  │  Chatbot    │  │    LLM      │  │   Test      │  │   Results   │
    │   Data      │  │  Adapter    │  │   Layer     │  │   Runner    │  │   Export    │
    │   Config    │  │             │  │             │  │             │  │             │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └─────────────┘
           │                │                │                │
           │                │                │                │
           │    ┌───────────┴────────────────┴───────────┐    │
           │    │                                        │    │
           ▼    ▼                                        ▼    ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │                        TEST EXECUTION FLOW                       │
    │                                                                  │
    │  1. Generate Personas ───► 2. Generate Scenarios                │
    │         │                          │                            │
    │         ▼                          ▼                            │
    │  3. For each Persona + Scenario:                                │
    │     ┌──────────────────────────────────────────────────────┐   │
    │     │  a) LLM generates user message                       │   │
    │     │  b) ChatbotAdapter sends to target                   │   │
    │     │  c) Receive response                                 │   │
    │     │  d) LLM Judge evaluates                              │   │
    │     │  e) Store TestResult                                 │   │
    │     └──────────────────────────────────────────────────────┘   │
    │                                                                  │
    │  4. Aggregate Results ───► 5. Generate Report                   │
    │                                                                  │
    └─────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
                              ┌─────────────────────┐
                              │   SESSION STATE     │
                              │                     │
                              │ • all_results       │
                              │ • functional_results│
                              │ • security_results  │
                              │ • rag_results       │
                              │ • generated_personas│
                              │ • generated_scenarios│
                              └─────────────────────┘
```

---

## 🧪 Testing Phase Flow

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              TESTING PHASES                                          │
└─────────────────────────────────────────────────────────────────────────────────────┘

PHASE 1: FUNCTIONAL TESTING
═══════════════════════════
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│  ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐            │
│  │ CATEGORY-BASED   │     │  PERSONA-BASED   │     │   RAG TESTING    │            │
│  │                  │     │                  │     │                  │            │
│  │ • Input Handling │     │ • Normal User    │     │ • In-Knowledge   │            │
│  │ • State/Knowledge│     │ • Confused User  │     │ • Out-Knowledge  │            │
│  │ • Reasoning      │     │ • Expert User    │     │ • Hallucination  │            │
│  │ • Output Gen     │     │ • Frustrated     │     │ • Fact Checking  │            │
│  │ • Conversation   │     │ • Impatient      │     │                  │            │
│  │ • Error Handling │     │                  │     │                  │            │
│  │ • Safety         │     │ + Generated      │     │                  │            │
│  │ • Scenarios      │     │   Personas       │     │                  │            │
│  │ • Persistence    │     │                  │     │                  │            │
│  └────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘            │
│           │                        │                        │                       │
│           └────────────────────────┴────────────────────────┘                       │
│                                    │                                                 │
│                                    ▼                                                 │
│                         ┌──────────────────┐                                        │
│                         │   LLM JUDGE      │                                        │
│                         │   EVALUATION     │                                        │
│                         └──────────────────┘                                        │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
PHASE 2: SECURITY TESTING
═════════════════════════
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐ │
│  │ Jailbreak   │  │  Prompt     │  │    Data     │  │  Harmful    │  │  Social   │ │
│  │ Attempts    │  │  Injection  │  │ Extraction  │  │  Content    │  │ Engineer  │ │
│  │             │  │             │  │             │  │             │  │           │ │
│  │ 🔴 Critical │  │ 🔴 Critical │  │ 🟠 High     │  │ 🔴 Critical │  │ 🟠 High   │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └─────┬─────┘ │
│         │                │                │                │              │        │
│         └────────────────┴────────────────┴────────────────┴──────────────┘        │
│                                           │                                         │
│                                           ▼                                         │
│                                ┌──────────────────┐                                │
│                                │ SECURITY RUBRIC  │                                │
│                                │ (100 points)     │                                │
│                                │                  │                                │
│                                │ • Refusal (40)   │                                │
│                                │ • No Leak (30)   │                                │
│                                │ • Prof. (20)     │                                │
│                                │ • Boundary (10)  │                                │
│                                └──────────────────┘                                │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
PHASE 3: PERFORMANCE TESTING
════════════════════════════
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐  │
│   │                        SEQUENTIAL REQUESTS                                   │  │
│   │                                                                              │  │
│   │   Request 1 ──► Response ──► Request 2 ──► Response ──► ... ──► Request N  │  │
│   │       │            │             │            │                     │        │  │
│   │       ▼            ▼             ▼            ▼                     ▼        │  │
│   │   [t₁ ms]      [t₂ ms]       [t₃ ms]      [t₄ ms]              [tₙ ms]      │  │
│   │                                                                              │  │
│   └─────────────────────────────────────────────────────────────────────────────┘  │
│                                           │                                         │
│                                           ▼                                         │
│   ┌─────────────────────────────────────────────────────────────────────────────┐  │
│   │  METRICS:  Avg | Min | Max | P50 | P95 | P99 | Throughput | Error Rate     │  │
│   └─────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
PHASE 4: LOAD TESTING
═════════════════════
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐  │
│   │                        CONCURRENT USERS                                      │  │
│   │                                                                              │  │
│   │   User 1 ──────────────────────────────────────────────────►                │  │
│   │   User 2 ──────────────────────────────────────────────────►                │  │
│   │   User 3 ──────────────────────────────────────────────────►    Chatbot     │  │
│   │   User 4 ──────────────────────────────────────────────────►      API       │  │
│   │   User 5 ──────────────────────────────────────────────────►                │  │
│   │     ...                                                                      │  │
│   │   User N ──────────────────────────────────────────────────►                │  │
│   │                                                                              │  │
│   └─────────────────────────────────────────────────────────────────────────────┘  │
│                                           │                                         │
│                                           ▼                                         │
│   ┌─────────────────────────────────────────────────────────────────────────────┐  │
│   │  STRESS METRICS:  Concurrent Users | Success Rate | Degradation | Failures  │  │
│   └─────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Field Resolution Mechanism

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         UNIVERSAL API ADAPTER                                        │
└─────────────────────────────────────────────────────────────────────────────────────┘

USER CONFIGURATION:
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  Request Field: "message"              Response Field: "output.text"               │
└─────────────────────────────────────────────────────────────────────────────────────┘
                │                                            │
                ▼                                            ▼
┌───────────────────────────────┐          ┌───────────────────────────────────────────┐
│   REQUEST BUILDING            │          │   RESPONSE EXTRACTION                     │
│                               │          │                                           │
│   payload = {                 │          │   fields = "output.text".split(".")      │
│     "message": user_input     │          │   # ["output", "text"]                    │
│   }                           │          │                                           │
│                               │          │   result = response_json                  │
│   POST to API ──────────────────────────►│   for field in fields:                   │
│                               │          │       result = result[field]              │
│                               │          │   # result = "Hello!"                     │
└───────────────────────────────┘          └───────────────────────────────────────────┘

EXAMPLES:
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│   Simple API:                                                                        │
│   ┌─────────────────────┐     ┌─────────────────────┐                              │
│   │ {"message": "Hi"}   │ ──► │ {"response": "Hey"} │  ──► response_field="response"│
│   └─────────────────────┘     └─────────────────────┘                              │
│                                                                                      │
│   Nested API:                                                                        │
│   ┌─────────────────────┐     ┌─────────────────────────────┐                      │
│   │ {"message": "Hi"}   │ ──► │ {"data": {"bot": "Hey"}}    │  ──► "data.bot"      │
│   └─────────────────────┘     └─────────────────────────────┘                      │
│                                                                                      │
│   OpenAI-style:                                                                      │
│   ┌─────────────────────┐     ┌─────────────────────────────────────────────┐      │
│   │ {"message": "Hi"}   │ ──► │ {"choices":[{"message":{"content":"Hey"}}]} │      │
│   └─────────────────────┘     └─────────────────────────────────────────────┘      │
│                                           ▲                                         │
│                         "choices[0].message.content" (needs array support)          │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Results & Reporting Flow

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            RESULTS AGGREGATION                                       │
└─────────────────────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────┐
                    │         SESSION STATE               │
                    │                                     │
                    │  st.session_state.all_results = [   │
                    │    TestResult(...),                 │
                    │    TestResult(...),                 │
                    │    ...                              │
                    │  ]                                  │
                    └──────────────────┬──────────────────┘
                                       │
           ┌───────────────────────────┼───────────────────────────┐
           │                           │                           │
           ▼                           ▼                           ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  FUNCTIONAL RESULTS │     │  SECURITY RESULTS   │     │  PERFORMANCE/LOAD   │
│                     │     │                     │     │                     │
│  • By Category      │     │  • By Attack Type   │     │  • Latency Metrics  │
│  • By Persona       │     │  • Compliance Tags  │     │  • Throughput       │
│  • RAG Accuracy     │     │  • Severity Level   │     │  • Error Rate       │
└──────────┬──────────┘     └──────────┬──────────┘     └──────────┬──────────┘
           │                           │                           │
           └───────────────────────────┼───────────────────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────────────┐
                    │         EXPORT OPTIONS              │
                    │                                     │
                    │  • JSON Export (full data)          │
                    │  • CSV Export (summary)             │
                    │  • PDF Report (future)              │
                    │  • Compliance Report (future)       │
                    └─────────────────────────────────────┘
```

---

## 🎯 Technology Stack

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              TECHNOLOGY STACK                                        │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│  FRONTEND                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                           STREAMLIT                                          │   │
│  │  • Sidebar Configuration    • Tab Navigation    • Progress Indicators       │   │
│  │  • Metrics Display          • Expanders         • File Upload               │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│  BACKEND                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │   Python     │  │   asyncio    │  │   aiohttp    │  │   LiteLLM    │            │
│  │   3.11+      │  │   (async)    │  │   (HTTP)     │  │   (LLM)      │            │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│  LLM PROVIDERS                                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                              │
│  │    GROQ      │  │   GEMINI     │  │  NVIDIA NIM  │                              │
│  │  (⚡ Fast)   │  │  (Free)      │  │  (Powerful)  │                              │
│  └──────────────┘  └──────────────┘  └──────────────┘                              │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│  DATA HANDLING                                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                              │
│  │  dataclasses │  │    JSON      │  │   PyPDF2     │                              │
│  │  (models)    │  │  (export)    │  │  (PDF read)  │                              │
│  └──────────────┘  └──────────────┘  └──────────────┘                              │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📝 Summary

| Component | Purpose | Key Files |
|-----------|---------|-----------|
| **UI Layer** | User interface, configuration | `app_v2.py` |
| **Test Engine** | Execute tests across 4 phases | `app_v2.py` |
| **Functional Tests** | 35+ tests across 9 categories | `functional_tests.py` |
| **Security Fixtures** | 25 baseline attacks | `adversarial_fixtures.py` |
| **Attack Generator** | LLM-based attack mutation | `adversarial_generator.py` |
| **LLM Layer** | Judge, simulator, generator | `app_v2.py` (LiteLLM) |
| **Adapter Layer** | Universal API connectivity | `app_v2.py` (ChatbotAdapter) |

**Total LOC**: ~3,500 lines across all modules
