from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
import random
from typing import Dict

app = FastAPI(title="Space Rescue API")

# Constants
SYSTEMS = [
    "navigation",
    "communications",
    "life_support",
    "engines",
    "deflector_shield"
]

SYSTEM_CODES = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Store the last returned damaged system
last_damaged_system = None

@app.get("/status")
async def get_status() -> Dict[str, str]:
    """
    Returns a random damaged system from the available systems.
    Updates the last_damaged_system to be used by repair-bay.
    """
    global last_damaged_system
    # Generate a new random system every time
    last_damaged_system = random.choice(SYSTEMS)
    return {"damaged_system": last_damaged_system}

@app.get("/repair-bay", response_class=HTMLResponse)
async def get_repair_bay() -> str:
    """
    Returns an HTML page with the repair code for the last damaged system.
    If no system has been generated yet, generates a random one.
    """
    global last_damaged_system
    if last_damaged_system is None:
        last_damaged_system = random.choice(SYSTEMS)
    
    repair_code = SYSTEM_CODES[last_damaged_system]
    
    html_content = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{repair_code}</div>
    </body>
    </html>"""
    return html_content

@app.post("/teapot")
async def teapot(response: Response):
    """
    Returns a 418 I'm a teapot status code
    """
    response.status_code = status.HTTP_418_IM_A_TEAPOT
    return {"message": "I'm a teapot"}



