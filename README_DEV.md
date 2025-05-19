# 🛠️ HOOK Dev Starter Kit

Welcome to the HOOK Travel Dev Team's base kit. This folder is your foundation for building the world's first fiduciary AI travel assistant.

---

## ✨ Planned UI/UX Features

| Section | Functionality |
|---------|---------------|
| **Home Page** | Smart input box to describe trips, call-to-action to "Let's Book with HOOK" |
| **KnownTraveler Dashboard** | View profile, loyalty level, completion status, alerts, and rewards |
| **Itinerary Viewer** | Beautiful, exportable trip summaries (HTML + PDF) |
| **Cost Breakdown** | Show itemized cost: flights, hotels, fees, taxes, Hook margin |
| **Price Alerts** | Notify unbooked users of price changes and forecast dips |
| **Admin Console** | RFT data grader panel + contributor reward tracking |
| **Community Hub** | Contribute training samples, earn tokens, view leaderboard |

---

## 🧱 Core Modules

### `hook_ai_parser.py`
Takes a raw prompt like:

```text
"Fly from NYC to Tokyo in April. I want cherry blossoms and budget hotels."
```

Outputs structured JSON:

```json
{
  "origin": "NYC",
  "destination": "Tokyo",
  "dates": ["2025-04-01", "2025-04-10"],
  "preferences": ["cherry blossoms", "budget hotels"]
}
```

---

### `generate_itinerary.py`
Generates an HTML trip view from the parsed JSON above. Can be plugged into PDF or email output modules.

---

### `utils/token_tracker.py`
Tracks TOL tokens earned by contributors. Add real wallet addresses or user IDs later.

---

## 🎯 Feature Roadmap

| Phase | Goals |
|-------|-------|
| **Dev** | Prompt parsing, JSON handling, RFT collection |
| **Alpha** | Grading UI, token reward panel, basic email alerts |
| **Beta** | Full UI/UX deployed, HookTokens live, KnownTraveler reward system |
| **Launch** | Hook Pro 1.0 live with model inference, RFT-tuned concierge bot |

---

## 👨‍💻 For Developers

- Clone the repo
- Use `devkit/` to start testing modules
- Submit pull requests for:
  - Prompt/response validators
  - Trip generators
  - Reward backends
  - Dashboard or Make.com integrations

---

Let’s Hook the world 🌍  
— HOOK Travel Engineering
