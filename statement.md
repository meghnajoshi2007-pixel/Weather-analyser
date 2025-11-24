# Project Statement — Weather Analyzer

## 1. Problem Statement
Many users need a simple way to understand current local weather and get practical recommendations (dress, carry umbrella, stay indoors) without reading long forecasts. Students and casual users often want a lightweight tool that gives essential weather facts.

## 2. Scope of the Project
This project implements a command-line Weather Analyzer that:
- Accepts a city name (or local temperature input for the offline version).
- Fetches current weather from OpenWeatherMap API (or accepts user temperature input for the offline demo).
- Parses and displays key weather details: description, temperature (°C), humidity, wind speed.
- Provides a short, human-friendly recommendation (“Carry umbrella”, “Stay hydrated”, “Wear jacket”, etc.).
- Is implemented in modular Python code and is easy to extend (GUI, graphs, or scheduled checks can be added later).

*In-scope (minimum required):*
- Three major functional modules: Input handling, Weather retrieval & parsing, Analysis & suggestion output.
- Clear input/output flow and graceful error handling (missing API key, network error, invalid city).
- Use of Git for version control and repository documentation (README.md, statement.md, code files).

*Out of scope (for the current submission):*
- Full web or mobile app UI (optional future enhancement).
- Historical weather analytics (can be added as future work).

## 3. Target Users
- Students and learners who want a simple demo project (education use).
- Casual users who want quick, practical weather suggestions.
- Instructors evaluating basic integration of APIs and Python programming.

## 4. High-Level Features
1. *User Input Module*
   - Get city name (or accept offline temperature for demo).
   - Validate input and handle empty entries.

2. *Weather Retrieval Module*
   - Call OpenWeatherMap API (or read offline input) and retrieve JSON.
   - Handle network errors and “city not found” responses.

3. *Analysis & Recommendation Module*
   - Convert temperature from Kelvin to Celsius.
   - Determine mood/suggestion based on temperature and description (rain, thunder).
   - Produce formatted output for user.

4. *Documentation & Repo*
   - README.md with setup & run instructions.
   - statement.md (this file) describing problem, scope, users, features.
   - .gitignore, requirements.txt, and source files (e.g., weather.py or weather_analyzer.py).

## 5. Deliverables
- GitHub repository containing source code, README.md, statement.md, and requirements.txt.
- Project report (PDF) upload to the portal as per VITyarthi instructions.
