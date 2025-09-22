# FastAPI GitHub & Weather API

This project is a simple FastAPI application that provides two endpoints:

1. **Get GitHub User Info**  
   - Endpoint: `/get_github_user?username=<username>`  
   - Returns login, name, public repos, followers, and following count for a GitHub user.

2. **Get Weather Data**  
   - Endpoint: `/get_weather/{city}`  
   - Returns city name, temperature, and weather description.  
   - Requires an OpenWeatherMap API key stored in a `.env` file.

---
## Setup

### 1. Clone the repository

```python
git clone https://github.com/USERNAME/REPO.git
cd REPO 
``` 
### 2. Create and activate a virtual environment
```python
python3 -m venv venv
source venv/bin/activate
``` 
### 3. Install dependencies & .env 
```python
pip install -r requirements.txt
touch .env
``` 
### 4. Add your OpenWeatherMap API key inside .env & Run the FastAPI server
```python
API_KEY=your_openweathermap_api_key
uvicorn main:app --reload
```
