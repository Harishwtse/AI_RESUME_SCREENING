from io import BytesIO
def extract_text(data: bytes, filename: str) -> str:
    ext=filename.lower().rsplit(".",1)[-1]
    if ext=="pdf":
        from pypdf import PdfReader
        reader=PdfReader(BytesIO(data))
        text="\\n".join(page.extract_text() or "" for page in reader.pages)
    elif ext=="docx":
        from docx import Document
        doc=Document(BytesIO(data))
        text="\\n".join(p.text for p in doc.paragraphs)
        for table in doc.tables:
            text += "\\n" + "\\n".join(" | ".join(c.text for c in row.cells) for row in table.rows)
    elif ext=="txt":
        text=data.decode("utf-8",errors="ignore")
    else:
        raise ValueError("Unsupported file type")
    if not text.strip(): raise ValueError("No readable text found. Try a text-based PDF/DOCX.")
    return text[:50000]
