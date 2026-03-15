from __future__ import annotations
from pathlib import Path
from gemini_client import ask_gemini

PROMPT_PATH = Path(__file__).parent.parent / "prompts/summary_prompt.txt"

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    _PROMPT_TEMPLATE = f.read()

def generate_summary(schema: str) -> str:
    try:
        prompt = _PROMPT_TEMPLATE.format(schema=schema)
        summary = ask_gemini(prompt).strip()        
        
        if not summary or not summary[-1] in ".!?":
            return _fallback_summary(schema)
        
        return summary + "\nAsk me anything using the examples below or type your own question in the chat bar!"
    except Exception:
        return _fallback_summary(schema)


def _fallback_summary(schema: str) -> str:
    """Generate a simple summary without Gemini."""
    lines = schema.splitlines()
    cols = [l.strip("- ").split("(")[0].strip() for l in lines if l.strip().startswith("-")]
    col_count = len(cols)
    return (
        f"Your data has been loaded with {col_count} columns ready to explore. "
        "Ask me anything using the examples below or type your own question!"
    )