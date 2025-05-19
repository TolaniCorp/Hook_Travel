# generate_itinerary.py
# Generates an HTML itinerary from structured travel data

def generate(data):
    return f"""<h1>Trip to {data['destination']}</h1>
<p>Departing from {data['origin']} from {data['dates'][0]} to {data['dates'][1]}</p>
<p>Preferences: {', '.join(data['preferences'])}</p>"""
