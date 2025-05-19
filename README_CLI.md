# 🚀 HOOK CLI – Itinerary Generator

This CLI lets you generate branded HOOK travel itineraries from sample data, export to PDF, and reward contributors using TOL tokens.

---

## 🧰 Requirements

- Python 3.7+
- `pip` (Python package installer)
- WeasyPrint (auto-installed via `requirements.txt`)
- Linux/macOS/WSL (for WeasyPrint dependencies)

---

## 📦 Setup & Usage

### 1. Clone or unzip this repository

```bash
git clone https://github.com/TolaniCorp/HOOK_Travel.git
cd HOOK_Travel
```

### 2. Run the CLI (first time)

```bash
chmod +x run.sh
./run.sh
```

This will:
- Create a virtual environment (`venv`)
- Install dependencies
- Generate a sample itinerary PDF to `hook_trip_preview.pdf`
- Log TOL token activity for the test user

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `run.sh` | Bash script to bootstrap and run the project |
| `index.py` | CLI entry point for PDF generation and token rewards |
| `generate_itinerary.py` | Builds styled HTML from trip data |
| `pdf_generator.py` | Converts HTML to PDF via WeasyPrint |
| `utils/` | Token tracker and formatter utilities |
| `.env.example` | Configure logo, default currency, etc. |

---

## ✅ Output

- PDF file saved: `hook_trip_preview.pdf`
- Token reward logged for `user_xyz`

---

Let’s Hook the world 🌍  
— HOOK Travel Engineering
