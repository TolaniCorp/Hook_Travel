from pathlib import Path
from generate_itinerary import generate
from pdf_generator import generate_pdf

sample_data = {
    "origin": "New York (JFK)",
    "destination": "Tokyo (NRT)",
    "traveler_name": "Jane Doe",
    "departure_date": "2025-04-02",
    "return_date": "2025-04-10",
    "preferences": ["Cherry Blossoms", "Street Food", "Modern Art"],
    "flights": [
        {
            "airline": "ANA",
            "flight_number": "NH101",
            "departure": "JFK",
            "arrival": "NRT",
            "date": "2025-04-02",
            "price": 920.00
        },
        {
            "airline": "ANA",
            "flight_number": "NH100",
            "departure": "NRT",
            "arrival": "JFK",
            "date": "2025-04-10",
            "price": 890.00
        }
    ],
    "accommodations": [
        {
            "name": "Park Hotel Tokyo",
            "nights": 8,
            "total": 1120.00
        }
    ],
    "activities": ["Visit Ueno Park", "Tsukiji Market Tour", "TeamLab Planets Museum"],
    "budget": 3200.00,
    "currency": "USD"
}

html_output = generate(sample_data)

html_output = html_output.replace("<body>", """<body>
<div style='text-align:center; margin-bottom:30px;'>
    <img src='https://hooktravel.com/assets/logo.png' alt='HOOK Travel Logo' style='height:60px;'/>
    <h2 style='color:#0063ff;'>HOOK: Your Intelligent Travel Assistant</h2>
</div>""")

output_pdf_path = "hook_sample_itinerary.pdf"
generate_pdf(html_output, output_pdf_path)

print(f"PDF generated: {output_pdf_path}")
