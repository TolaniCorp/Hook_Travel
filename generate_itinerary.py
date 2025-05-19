# generate_itinerary.py
# Generates a styled HTML travel itinerary from structured travel data

from datetime import datetime
from typing import Dict, List

def format_currency(amount, currency="USD"):
    return f"{currency} {amount:,.2f}"

def generate(data: Dict) -> str:
    """
    Generate a full HTML itinerary page from structured travel data.
    
    Expected keys in `data`:
        - origin (str)
        - destination (str)
        - departure_date (str: YYYY-MM-DD)
        - return_date (str: YYYY-MM-DD)
        - traveler_name (str)
        - preferences (List[str])
        - flights (List[Dict])
        - accommodations (List[Dict])
        - activities (List[str])
        - budget (float)
        - currency (str)
    """
    destination = data.get("destination", "Unknown")
    origin = data.get("origin", "Unknown")
    traveler = data.get("traveler_name", "Traveler")
    dep_date = data.get("departure_date", "")
    ret_date = data.get("return_date", "")
    currency = data.get("currency", "USD")

    # Flights
    flights_html = ""
    for flight in data.get("flights", []):
        flights_html += f"""
        <li>{flight['airline']} — {flight['flight_number']}<br/>
        {flight['departure']} → {flight['arrival']} on {flight['date']} ({format_currency(flight['price'], currency)})</li>
        """

    # Accommodations
    hotels_html = ""
    for hotel in data.get("accommodations", []):
        hotels_html += f"""
        <li>{hotel['name']} ({hotel['nights']} nights) - {format_currency(hotel['total'], currency)}</li>
        """

    # Activities
    activities_html = "".join(f"<li>{activity}</li>" for activity in data.get("activities", []))

    # Preferences
    prefs_html = ", ".join(data.get("preferences", []))

    # Budget
    budget_html = format_currency(data.get("budget", 0.0), currency)

    return f"""
    <html>
    <head>
        <title>Itinerary for {traveler}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #0063ff; }}
            h2 {{ color: #333; }}
            ul {{ line-height: 1.6; }}
        </style>
    </head>
    <body>
        <h1>📍 Trip to {destination}</h1>
        <p><strong>Traveler:</strong> {traveler}</p>
        <p><strong>From:</strong> {origin} — <strong>Dates:</strong> {dep_date} to {ret_date}</p>
        <p><strong>Preferences:</strong> {prefs_html}</p>

        <h2>✈️ Flights</h2>
        <ul>{flights_html or "<li>No flights listed</li>"}</ul>

        <h2>🏨 Accommodations</h2>
        <ul>{hotels_html or "<li>No hotels listed</li>"}</ul>

        <h2>🗺 Activities & Highlights</h2>
        <ul>{activities_html or "<li>No activities planned</li>"}</ul>

        <h2>💰 Budget</h2>
        <p><strong>Total Estimated Budget:</strong> {budget_html}</p>
    </body>
    </html>
    """
