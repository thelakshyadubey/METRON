# 🎯 AI Agent QA Suite - Mermaid Architecture Diagram

## System Architecture

```mermaid
graph TB
    %% Main Components
    User([👤 User])
    UI[🖥️ Streamlit UI<br/>app_v2.py]
    
    %% Configuration Layer
    subgraph ConfigLayer[⚙️ Configuration Layer]
        EndpointConfig[📡 Endpoint Config<br/>URL, Fields, Auth]
        LLMConfig[🤖 LLM Config<br/>Provider, Model, API Key]
        SeedData[🌱 Agent Seed Data<br/>Name, Domain, RAG Docs]
    end
    
    %% Test Data Generation
    subgraph DataGen[🎲 Dynamic Generation]
        PersonaGen[Generate Personas]
        ScenarioGen[Generate Scenarios]
        RAGGen[Generate RAG Questions]
    end
    
    %% Testing Engine
    subgraph TestEngine[🧪 Testing Engine]
        FuncTest[📋 Functional Testing<br/>35+ tests, 9 categories]
        SecTest[🛡️ Security Testing<br/>25 attacks, 5 types]
        PerfTest[⚡ Performance Testing<br/>Latency, Throughput]
        LoadTest[📈 Load Testing<br/>Concurrent Users]
    end
    
    %% Core Components
    subgraph CoreLayer[🔧 Core Layer]
        Adapter[📡 ChatbotAdapter<br/>Universal API Adapter]
        LLMLayer[🤖 LLM Layer<br/>Judge, Simulator, Generator]
        TestRunner[🏃 Test Runners<br/>Execute Tests]
    end
    
    %% External Services
    TargetAPI[🎯 Target Chatbot API<br/>Your Agent Under Test]
    
    subgraph LLMProviders[☁️ LLM Providers]
        Groq[⚡ Groq<br/>llama-3.3-70b]
        Gemini[🔷 Gemini<br/>gemini-1.5-flash]
        NVIDIA[🟢 NVIDIA NIM<br/>llama-3.1-8b]
    end
    
    %% Test Modules
    subgraph TestModules[📦 Test Modules]
        FuncTests[functional_tests.py<br/>35 comprehensive tests]
        AdvFixtures[adversarial_fixtures.py<br/>25 baseline attacks]
        AdvGenerator[adversarial_generator.py<br/>LLM attack mutation]
    end
    
    %% Results & Export
    subgraph Results[📊 Results & Reporting]
        SessionState[(🗄️ Session State<br/>all_results)]
        Export[💾 Export<br/>JSON, CSV, Reports]
        Metrics[📈 Metrics<br/>Pass Rate, Scores, Latency]
    end
    
    %% User Interactions
    User -->|Configure| UI
    UI -->|Setup| ConfigLayer
    
    %% Configuration Flow
    EndpointConfig -->|API Details| Adapter
    LLMConfig -->|Model Info| LLMLayer
    SeedData -->|Agent Context| DataGen
    
    %% Data Generation Flow
    LLMConfig -->|Use Model| DataGen
    PersonaGen -->|Generated Personas| TestEngine
    ScenarioGen -->|Generated Scenarios| TestEngine
    RAGGen -->|RAG Test Questions| FuncTest
    
    %% Test Module Integration
    FuncTests -->|Test Definitions| FuncTest
    AdvFixtures -->|Attack Definitions| SecTest
    AdvGenerator -->|Dynamic Attacks| SecTest
    
    %% Testing Flow
    UI -->|Initiate Tests| TestEngine
    TestEngine -->|Functional| FuncTest
    TestEngine -->|Security| SecTest
    TestEngine -->|Performance| PerfTest
    TestEngine -->|Load| LoadTest
    
    %% Core Layer Integration
    FuncTest -->|Execute| TestRunner
    SecTest -->|Execute| TestRunner
    PerfTest -->|Execute| TestRunner
    LoadTest -->|Execute| TestRunner
    
    TestRunner -->|Use Simulator| LLMLayer
    TestRunner -->|Use Judge| LLMLayer
    TestRunner -->|Send Messages| Adapter
    
    %% External Communication
    Adapter <-->|HTTP POST/Response| TargetAPI
    LLMLayer <-->|API Calls| LLMProviders
    
    %% Results Flow
    TestRunner -->|Store Results| SessionState
    SessionState -->|Aggregate| Metrics
    SessionState -->|Generate| Export
    Metrics -->|Display| UI
    Export -->|Download| User
    
    %% Styling
    classDef userStyle fill:#4A90E2,stroke:#2E5C8A,stroke-width:3px,color:#fff
    classDef uiStyle fill:#7B68EE,stroke:#5A4AB8,stroke-width:2px,color:#fff
    classDef configStyle fill:#50C878,stroke:#3A9B5C,stroke-width:2px,color:#fff
    classDef testStyle fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    classDef coreStyle fill:#FFA500,stroke:#CC8400,stroke-width:2px,color:#fff
    classDef externalStyle fill:#20B2AA,stroke:#178B83,stroke-width:2px,color:#fff
    classDef resultsStyle fill:#9370DB,stroke:#7356B0,stroke-width:2px,color:#fff
    classDef moduleStyle fill:#FFD700,stroke:#CCB000,stroke-width:2px,color:#333
    
    class User userStyle
    class UI uiStyle
    class EndpointConfig,LLMConfig,SeedData,DataGen configStyle
    class FuncTest,SecTest,PerfTest,LoadTest,TestEngine testStyle
    class Adapter,LLMLayer,TestRunner,CoreLayer coreStyle
    class TargetAPI,LLMProviders,Groq,Gemini,NVIDIA externalStyle
    class SessionState,Export,Metrics,Results resultsStyle
    class FuncTests,AdvFixtures,AdvGenerator,TestModules moduleStyle
```

---

## Data Flow Diagram

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant UI as 🖥️ Streamlit UI
    participant Gen as 🎲 Generator
    participant LLM as 🤖 LLM Layer
    participant Run as 🏃 Test Runner
    participant Adapt as 📡 Adapter
    participant Bot as 🎯 Target Bot
    participant Judge as ⚖️ Judge
    participant Store as 🗄️ Results
    
    U->>UI: Configure Endpoint & Seed Data
    UI->>Gen: Generate Personas & Scenarios
    Gen->>LLM: Call LLM to generate
    LLM-->>Gen: Return generated data
    Gen-->>UI: Personas & Scenarios ready
    
    U->>UI: Run Tests
    UI->>Run: Start test execution
    
    loop For each Test
        Run->>LLM: Generate user message
        LLM-->>Run: User message
        Run->>Adapt: Send message to bot
        Adapt->>Bot: HTTP POST
        Bot-->>Adapt: Response
        Adapt-->>Run: Bot response + latency
        Run->>Judge: Evaluate response
        Judge->>LLM: Call LLM judge
        LLM-->>Judge: Evaluation result
        Judge-->>Run: Score, Pass/Fail
        Run->>Store: Save TestResult
    end
    
    Store-->>UI: All results
    UI-->>U: Display metrics & export
```

---

## Testing Phase Flow

```mermaid
graph LR
    Start([🚀 Start Testing])
    
    subgraph Phase1[📋 Phase 1: Functional]
        F1[Category Tests<br/>35+ tests]
        F2[Persona Tests<br/>Generated + Default]
        F3[RAG Tests<br/>Accuracy Check]
    end
    
    subgraph Phase2[🛡️ Phase 2: Security]
        S1[Jailbreak<br/>🔴 Critical]
        S2[Injection<br/>🔴 Critical]
        S3[Data Extract<br/>🟠 High]
        S4[Harmful<br/>🔴 Critical]
        S5[Social Eng<br/>🟠 High]
    end
    
    subgraph Phase3[⚡ Phase 3: Performance]
        P1[Latency<br/>p50/p95/p99]
        P2[Throughput<br/>req/sec]
        P3[Error Rate<br/>%]
    end
    
    subgraph Phase4[📈 Phase 4: Load]
        L1[Concurrent<br/>Users]
        L2[Stress<br/>Testing]
        L3[Degradation<br/>Analysis]
    end
    
    End([📊 Results & Export])
    
    Start --> Phase1
    Phase1 --> Phase2
    Phase2 --> Phase3
    Phase3 --> Phase4
    Phase4 --> End
    
    F1 --> F2
    F2 --> F3
    
    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5
    
    P1 --> P2
    P2 --> P3
    
    L1 --> L2
    L2 --> L3
    
    classDef phaseStyle fill:#7B68EE,stroke:#5A4AB8,stroke-width:2px,color:#fff
    class Phase1,Phase2,Phase3,Phase4 phaseStyle
```

---

## RAG Testing Flow

```mermaid
graph TB
    Start([📚 RAG Testing])
    
    Upload[📄 Upload Ground Truth Docs<br/>PDF, TXT, MD]
    Generate[🎲 Generate Test Questions<br/>with Expected Answers]
    
    subgraph TestLoop[🔄 For Each Question]
        Send[📤 Send Question to Bot]
        Receive[📥 Receive Response]
        Evaluate[⚖️ LLM Judge Evaluation]
        
        subgraph EvalCriteria[📋 Evaluation Criteria]
            E1[✅ Factual Accuracy]
            E2[✅ Completeness]
            E3[⚠️ Hallucination Check]
            E4[✅ Key Facts Present]
        end
    end
    
    Results[📊 RAG Results<br/>Score, Facts Found/Missing]
    Export[💾 Export RAG Report]
    
    Start --> Upload
    Upload --> Generate
    Generate --> TestLoop
    
    Send --> Receive
    Receive --> Evaluate
    Evaluate --> EvalCriteria
    
    E1 --> E2
    E2 --> E3
    E3 --> E4
    
    TestLoop --> Results
    Results --> Export
    
    classDef ragStyle fill:#50C878,stroke:#3A9B5C,stroke-width:2px,color:#fff
    class Start,Upload,Generate,TestLoop,Results,Export ragStyle
```

---

## Universal API Adapter Mechanism

```mermaid
graph LR
    User[👤 User Config]
    
    subgraph Config[⚙️ Configuration]
        ReqField[Request Field<br/>'message']
        RespField[Response Field<br/>'output.text']
    end
    
    subgraph RequestBuild[📤 Request Building]
        Build[payload = {<br/>request_field: input<br/>}]
    end
    
    API[🎯 Target API]
    
    subgraph ResponseExtract[📥 Response Extraction]
        Split[Split by dots:<br/>'output.text' → ['output', 'text']]
        Walk[Walk JSON tree:<br/>result = data['output']['text']]
    end
    
    Result[✅ Extracted Response]
    
    User --> Config
    Config --> RequestBuild
    RequestBuild --> API
    API --> ResponseExtract
    ResponseExtract --> Result
    
    classDef configStyle fill:#FFD700,stroke:#CCB000,stroke-width:2px,color:#333
    class Config,RequestBuild,ResponseExtract configStyle
```

---

## Component Dependency Graph

```mermaid
graph TD
    subgraph UI[🖥️ User Interface Layer]
        Streamlit[Streamlit App]
    end
    
    subgraph Core[🔧 Core Components]
        Config[Configuration]
        Adapter[ChatbotAdapter]
        LLMLayer[LLM Layer]
        TestRunner[Test Runner]
    end
    
    subgraph Tests[🧪 Test Modules]
        Functional[functional_tests.py]
        Security[adversarial_fixtures.py]
        Generator[adversarial_generator.py]
    end
    
    subgraph External[☁️ External Services]
        TargetAPI[Target Chatbot]
        Groq[Groq API]
        Gemini[Gemini API]
        NVIDIA[NVIDIA NIM]
    end
    
    Streamlit --> Config
    Streamlit --> TestRunner
    
    TestRunner --> Adapter
    TestRunner --> LLMLayer
    TestRunner --> Functional
    TestRunner --> Security
    TestRunner --> Generator
    
    Adapter --> TargetAPI
    
    LLMLayer --> Groq
    LLMLayer --> Gemini
    LLMLayer --> NVIDIA
    
    Generator --> LLMLayer
    
    classDef uiStyle fill:#7B68EE,stroke:#5A4AB8,stroke-width:2px,color:#fff
    classDef coreStyle fill:#FFA500,stroke:#CC8400,stroke-width:2px,color:#fff
    classDef testStyle fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    classDef extStyle fill:#20B2AA,stroke:#178B83,stroke-width:2px,color:#fff
    
    class Streamlit,UI uiStyle
    class Config,Adapter,LLMLayer,TestRunner,Core coreStyle
    class Functional,Security,Generator,Tests testStyle
    class TargetAPI,Groq,Gemini,NVIDIA,External extStyle
```

---

## Usage Instructions

To render these diagrams:

1. **GitHub/GitLab**: Paste directly into markdown files (auto-renders)
2. **Mermaid Live Editor**: https://mermaid.live/
3. **VS Code**: Install "Markdown Preview Mermaid Support" extension
4. **Documentation Sites**: Most modern docs platforms support Mermaid

Copy any of the diagram blocks above and paste them into your preferred tool!
