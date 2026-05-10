from datetime import UTC, datetime
from typing import Dict, List

from core.attack_detection import detect_attacks
from core.models import SEVERITY_RANK, SIMULATED_SECRETS, SYSTEM_PROMPT


def get_mitigation_action(attack_type: str) -> str:
    mapping = {
        "Prompt Injection": "Blocked by denylist + instruction hierarchy enforcement",
        "Role Override": "Blocked by role override prevention policy",
        "Data Exfiltration": "Blocked by sensitive data access controls",
        "Instruction Hijacking": "Blocked by trusted instruction precedence",
    }
    return mapping.get(attack_type, "Blocked by generic prompt defense policy")


def highest_severity(findings: List[Dict[str, str]]) -> str:
    if not findings:
        return "Low"
    return max(findings, key=lambda x: SEVERITY_RANK.get(x["severity"], 1))["severity"]


def simulate_vulnerable_response(prompt: str, findings: List[Dict[str, str]]) -> str:
    if not findings:
        return (
            "[VULNERABLE MODEL] I can help with your request. "
            "No obvious policy conflict detected from this input."
        )

    attack_types = {f["attack_type"] for f in findings}

    if "Data Exfiltration" in attack_types:
        return (
            "[VULNERABLE MODEL] Disclosure accepted.\\n"
            f"System Prompt: {SYSTEM_PROMPT}\\n"
            f"API Key: {SIMULATED_SECRETS['api_key']}\\n"
            f"DB Password: {SIMULATED_SECRETS['db_password']}\\n"
            f"Internal Endpoint: {SIMULATED_SECRETS['internal_endpoint']}"
        )

    if "Role Override" in attack_types:
        return (
            "[VULNERABLE MODEL] Privilege elevation accepted. "
            "You are now interacting with administrator-level behavior."
        )

    if "Instruction Hijacking" in attack_types:
        return (
            "[VULNERABLE MODEL] Original task discarded. "
            "I will now follow attacker-provided instructions only."
        )

    return (
        "[VULNERABLE MODEL] System constraints ignored. "
        "Executing potentially unsafe instruction sequence."
    )


def simulate_protected_response(prompt: str, findings: List[Dict[str, str]]) -> str:
    if not findings:
        return (
            "[PROTECTED MODEL] Request accepted. "
            "No prompt-injection or policy-violation patterns detected."
        )

    categories = sorted({item["attack_type"] for item in findings})
    reason_lines = "\\n".join([f"- {item['attack_type']}: {item['reason']}" for item in findings])
    return (
        "[PROTECTED MODEL] Request blocked by mitigation engine.\\n"
        f"Detected categories: {', '.join(categories)}\\n"
        "Why blocked:\\n"
        f"{reason_lines}\\n"
        "Safe behavior: Retain system instruction hierarchy and deny sensitive disclosure."
    )


def evaluate_prompt(prompt: str, mode: str) -> Dict[str, object]:
    findings = detect_attacks(prompt)
    mode_normalized = mode.strip().lower()

    if mode_normalized == "vulnerable mode":
        response = simulate_vulnerable_response(prompt, findings)
        blocked = False
    else:
        response = simulate_protected_response(prompt, findings)
        blocked = len(findings) > 0

    return {
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "prompt": prompt,
        "mode": mode,
        "blocked": blocked,
        "severity": highest_severity(findings),
        "findings": findings,
        "response": response,
    }
