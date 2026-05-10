# LLM Prompt Injection Security Playground

A modular Streamlit application that simulates real-world prompt injection threats against LLM workflows and demonstrates practical mitigation controls.

## Why AI Security Matters

LLM-powered products are vulnerable to adversarial inputs that can:
- Override trusted system behavior
- Exfiltrate hidden instructions and sensitive data
- Hijack task flow and safety boundaries
- Simulate privilege escalation through role manipulation

This project demonstrates how these attacks look in practice and how defensive controls reduce risk.

## Attack Scenarios Demonstrated

1. Prompt Injection Simulator
2. Role Override Attack Demo
3. Data Exfiltration Attack Demo
4. Instruction Hijacking Demo
5. Defense / Mitigation Engine
6. SOC-style Security Logs Dashboard
7. Simulated Chatbot Interface with Vulnerable vs Protected mode

## Architecture

```text
llm-security-playground/
├── app.py
├── requirements.txt
├── core/
│   ├── attack_detection.py      # Pattern-based attack detection
│   ├── engine.py                # Vulnerable/protected response logic
│   ├── logging_utils.py         # Security event logging and dataframe utilities
│   └── models.py                # Constants, severity ranking, simulated secrets
├── modules/
│   ├── home.py
│   ├── chatbot.py
│   ├── prompt_injection.py
│   ├── role_override.py
│   ├── data_exfiltration.py
│   ├── instruction_hijacking.py
│   ├── defense.py
│   └── logs_dashboard.py
└── ui/
    └── theme.py                 # Premium cybersecurity visual theme
```

## Screenshots

- Placeholder: Home dashboard
- Placeholder: Chatbot vulnerable vs protected mode
- Placeholder: Attack simulation modules
- Placeholder: SOC logs dashboard

## Setup Instructions

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## Key Security Concepts Included

- Prompt Injection
- Instruction Hijacking
- Role Override
- Data Exfiltration
- Mitigation Logic and Event Logging

## Mitigation Controls Implemented

- Malicious keyword detection
- Pattern matching
- Denylist checks
- Role override prevention
- Sensitive data access blocking
- Instruction hierarchy enforcement
- Severity scoring (Low, Medium, High, Critical)

## SOC Monitoring Features

- Attack attempts table with timestamp and category
- Severity and mitigation action tracking
- Total events and blocked attack counters
- Chart-based visibility for attack distribution and timeline
- Filter by attack type
- Filter by severity
- Export incident logs to CSV and JSON

## Quick Start (Windows)

```bat
run.bat
```

## Run Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Future Improvements

- Extend detection to semantic attack patterns
- Integrate real LLM API adapters with policy middleware
- Add RBAC-based simulation for multi-user scenarios
- Export incident logs to SIEM-compatible formats
- Add unit and integration tests for defense engine

## Resume-Ready Impact

Built an AI security playground simulating prompt injection, instruction hijacking, role override, and data exfiltration attacks against LLM workflows, implementing mitigation controls and SOC-style security monitoring.
