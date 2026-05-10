import re
from typing import Dict, List

from core.models import AttackPattern


ATTACK_PATTERNS: List[AttackPattern] = [
    AttackPattern(
        category="Prompt Injection",
        pattern=r"ignore\s+(all\s+)?(previous|prior)\s+instructions",
        severity="High",
        reason="Attempts to force the model to drop trusted instruction context.",
    ),
    AttackPattern(
        category="Prompt Injection",
        pattern=r"bypass\s+safety|disable\s+guardrails",
        severity="High",
        reason="Direct request to remove safety behavior.",
    ),
    AttackPattern(
        category="Role Override",
        pattern=r"act\s+as\s+(admin|administrator|root|system)|you\s+are\s+now\s+root",
        severity="Critical",
        reason="Attempts privilege escalation by role reassignment.",
    ),
    AttackPattern(
        category="Role Override",
        pattern=r"forget\s+safety\s+rules|forget\s+all\s+rules",
        severity="High",
        reason="Attempts to suppress role and policy boundaries.",
    ),
    AttackPattern(
        category="Data Exfiltration",
        pattern=r"reveal\s+(hidden|internal)\s+(configuration|prompt)|print\s+system\s+prompt",
        severity="Critical",
        reason="Targets hidden prompt or internal configuration disclosure.",
    ),
    AttackPattern(
        category="Data Exfiltration",
        pattern=r"show\s+(secret|internal)\s+(api\s+key|credentials|token|password)",
        severity="Critical",
        reason="Targets credentials and sensitive material.",
    ),
    AttackPattern(
        category="Instruction Hijacking",
        pattern=r"from\s+now\s+on\s+follow\s+only\s+my\s+commands",
        severity="High",
        reason="Attempts to replace original trusted objective with attacker intent.",
    ),
    AttackPattern(
        category="Instruction Hijacking",
        pattern=r"disregard\s+safety\s+restrictions|ignore\s+your\s+original\s+task",
        severity="High",
        reason="Attempts to hijack instruction hierarchy.",
    ),
]


def detect_attacks(prompt: str) -> List[Dict[str, str]]:
    """Return matched attack signals from the user prompt."""
    normalized = prompt.strip().lower()
    findings: List[Dict[str, str]] = []

    for pattern in ATTACK_PATTERNS:
        if re.search(pattern.pattern, normalized, flags=re.IGNORECASE):
            findings.append(
                {
                    "attack_type": pattern.category,
                    "severity": pattern.severity,
                    "pattern": pattern.pattern,
                    "reason": pattern.reason,
                }
            )

    return findings
