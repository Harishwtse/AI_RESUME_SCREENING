def redact_email_phone(text: str) -> str:
    # Basic demo redaction; production must use tested PII detection and secure storage.
    import re
    text=re.sub(r"[\\w.+-]+@[\\w-]+\\.[\\w.-]+","[EMAIL]",text)
    text=re.sub(r"(?<!\\w)(?:\\+?\\d[\\d .()-]{7,}\\d)(?!\\w)","[PHONE]",text)
    return text
