from weasyprint import HTML
from pathlib import Path

def generate_pdf(html_content: str, output_path: str = "itinerary_output.pdf") -> str:
    output_file = Path(output_path)
    HTML(string=html_content).write_pdf(target=output_file)
    return str(output_file)
