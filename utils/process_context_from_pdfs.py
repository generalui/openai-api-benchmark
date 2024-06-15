import os
import fitz  # PyMuPDF
import asyncio

async def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    document = fitz.open(file_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

async def process_pdfs():
    files = os.listdir("./files")
    pdfs = [file for file in files if file.endswith(".pdf")]

    context_files_text = await asyncio.gather(
        *[extract_text_from_pdf(f"./files/{file}") for file in pdfs]
    )

    return "\n".join(context_files_text)