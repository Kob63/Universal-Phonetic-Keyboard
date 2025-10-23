# Universal Phonetic Keyboard (UPK)

A simple, multilingual typing engine written in Python.  
It uses JSON mappings to type any world language — Tamil, Hindi, Sinhala, Greek, or more.

## 🌍 Highlights
- Works with any script or language — just change the JSON mapping.
- Stage-based system (supports up to 5 stages).
- Uses only Python’s standard libraries.
- Great for phonetic typing and Unicode-based scripts.

## 🧠 How It Works
1. Run `main.py`.
2. Load your desired mapping JSON (e.g., Tamil).
3. Start typing — the characters appear in your console.

Example:
```
ka → க  
koo → கூ  
```

## 🪶 Creating Your Own Mapping
Each key combination points to a character and stage:
```json
"ka": {"char": "க", "stage": 1}
```
You can easily create mappings for Hindi, Malayalam, or any script.

## 👨‍🌾 Credits
Concept by Oldman (Tamil farmer) — made with ChatGPT (OpenAI)

## 🗣️ தமிழில்
இந்த மென்பொருள் உலகின் எந்த மொழியையும் தட்டச்சு செய்ய உதவும்.  
தமிழிலிருந்து தொடங்கி அனைத்து மொழிகளுக்கும் பயன்படும்.

## 📜 License
Released under the MIT License — open and free for educational, cultural, and community use.
