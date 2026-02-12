import os
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from google import genai
from google.genai import types

# --- CONFIGURATION ---
os.environ["GOOGLE_API_KEY"] = "TYPE-YOUR-GEMINI-API-HERE"   	#------ Here Type Gemini API which this use to excess gemini as brain _______
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATA MODELS ---
class RobotStep(BaseModel):
    target_location: str
    load_action: str # "pick_up", "drop_off", or "none"
    reasoning: str

class RobotAction(BaseModel):
    robot_id: str
    steps: List[RobotStep]

class FleetResponse(BaseModel):
    dispatch_list: List[RobotAction]

@app.post("/dispatch")
async def dispatch(payload: dict = Body(...)):
    user_prompt = payload.get("prompt")
    battery = payload.get("battery", {"red_bot": 100, "blue_bot": 100})
    
    # SYSTEM INSTRUCTION: The core intelligence
    sys_instr = f"""You are the OmniPath Fleet Manager. 
    LOCATIONS: loading_dock (Pickup/Charge), storage_A, storage_B, shipping_bay (Dropoff).
    FLEET STATUS: Red Bot: {battery['red_bot']}%, Blue Bot: {battery['blue_bot']}%.
    
    CRITICAL PROTOCOLS:
    1. If battery < 20%, force robot to 'loading_dock' to charge. 
    2. Multi-step tasks must be broken down: 'pick_up' at source, then 'drop_off' at target.
    3. Use IDs 'red_bot' and 'blue_bot'.
    4. Provide reasoning for every step taken."""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=sys_instr,
                response_mime_type="application/json",
                response_schema=FleetResponse
            )
        )
        print(f"Mission Dispatched: {response.parsed}")
        return response.parsed
    except Exception as e:
        print(f"Detailed Error: {e}")
        # Send a 429 status code specifically if it's a quota issue
        if "429" in str(e):
            return {"error": "Quota exceeded. Please wait a minute before trying again."}
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
