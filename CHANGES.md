# URL Shortener - Implementation Notes

## AI Usage Disclosure

**Tools Used:**
- ChatGPT 

**Purpose of AI Usage:**
- To understand best practices in Flask architecture (Blueprints, utils, modular design)
- To draft the testing structure using `pytest`
- To clarify the expected structure of the application per the prompt

**Human Contributions:**
- I fully structured the folders (`app/`, `routes/`, `utils/`, `models/`, etc.)
- Integrated and debugged Flask routes
- Wrote, ran, and validated test cases using Postman and pytest
- Organized the final codebase for modularity and submission

**AI-Generated Code:**
- Some parts of route patterns and test scaffolding were AI-suggested
- All suggestions were reviewed, adapted, and tested manually

## Assumptions

- I chose to use **in-memory storage (Python dictionary)** for simplicity and per assignment requirements.
- If this were to be extended, I would prefer using a **NoSQL database like MongoDB**, as it’s more flexible for storing evolving metadata for URLs.

## What I’d Do With More Time

- Implement a basic frontend UI to interact with the shortener visually
- Add rate-limiting, custom short code support, and expiry options
- Use persistent storage (SQLite or MongoDB) instead of in-memory

## Project Structure
    url-shortener/
    
    ├── app/
    
    │ ├── init.py
    
    │ ├── main.py
    
    │ ├── utils.py
    
    │ ├── models.py
    
    │ └── routes/
    
    │ └── url_routes.py
    
    ├── main.py
    
    ├── tests/
    
    │ └── test_basic.py
    
    ├── requirements.txt
    
    ├── NOTES.md

