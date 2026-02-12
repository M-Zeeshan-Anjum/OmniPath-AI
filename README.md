🤖 OmniPath AI: Conversational Fleet Orchestration
A 3D Digital Twin for Autonomous Warehouse Logistics

🌟 Overview
OmniPath AI is a next-generation warehouse management system that bridges the gap between human intent and robotic execution. By combining Gemini 2.5 Flash-Lite with a Three.js Digital Twin, we enable warehouse managers to orchestrate entire robotic fleets using simple, natural language.

🚀 Features
Natural Language Dispatch: Issue complex, multi-step missions like "Move Red Bot to the dock, pick up cargo, and deliver to Storage A."

Gemini-Powered Reasoning: The AI doesn't just move bots—it evaluates battery levels, calculates step-by-step logic, and manages inventory states.

Real-Time 3D Digital Twin: Built with Three.js, providing 1:1 visual telemetry of the warehouse floor.

Autonomous Safety Overrides: If a robot's battery is critical ( < 20%), the system autonomously reroutes it to a charging station, overriding user commands to prevent fleet downtime.

🛠️ Tech Stack
Cloud Infrastructure: Hosted on Vultr Cloud Compute (VC2) for high-performance API handling.

AI Engine: Gemini 2.5 Flash-Lite (Google AI Studio) for low-latency, structured JSON mission generation.

Backend: Python 3.10+, FastAPI, Uvicorn.

Frontend: Three.js (WebGL), GSAP (Animations), JavaScript.

🏗️ Architecture
User Input: Manager types a command into the terminal.

AI Orchestration: The FastAPI backend on Vultr sends the prompt to Gemini.

JSON Dispatch: Gemini returns a structured RobotAction list.

Simulation: The 3D frontend executes the movement via asynchronous GSAP sequences.

⚙️ Installation & Setup
Prerequisites
Python 3.10+

A Gemini API Key from Google AI Studio.

Local Deployment
Clone the repository:

Bash
git clone https://github.com/your-username/OmniPath-AI.git
cd OmniPath-AI
Install dependencies:

Bash
pip install -r requirements.txt
Environment Variables: Create a .env file and add your API Key:

Plaintext
GEMINI_API_KEY=your_key_here
Run the server:

Bash
uvicorn main:app --reload
🌐 Live Demo
Access the live deployment hosted on Vultr: 👉 http://149.28.64.112.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
