# index.py
# CLI-style entry point for running itinerary + reward test

from generate_itinerary import generate
from pdf_generator import generate_pdf
from utils.formatter import format_currency, format_date
from utils.token_tracker import reward_user, get_user_total

sample_trip = {
    "origin": "NYC",
    "destination": "Rome",
    "traveler_name": "Hook Tester",
    "departure_date": "2025-06-01",
    "return_date": "2025-06-10",
    "preferences": ["history", "wine", "walking tours"],
    "flights": [],
    "accommodations": [],
    "activities": ["Colosseum", "Vatican Museums", "Trastevere Dinner"],
    "budget": 2300,
    "currency": "USD"
}

html = generate(sample_trip)
html = html.replace("<body>", f"<body><div style='text-align:center'><h1>HOOK Trip Preview</h1></div>")

# Output PDF
generate_pdf(html, "hook_trip_preview.pdf")
print("🧾 PDF saved to hook_trip_preview.pdf")

# Reward user
reward_user("user_xyz", 15)
print("🎖 TOL Tokens awarded:", get_user_total("user_xyz"))
