@echo off
echo.
echo ============================================
echo   AI Agent QA Suite v2.0
echo ============================================
echo.
echo Starting restructured application...
echo.

cd /d "C:\Users\Lakshya\Desktop\YASH\AI_QA_Agent"

REM Check if .env exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Create a .env file with your API keys:
    echo   GROQ_API_KEY=your_key_here
    echo   GEMINI_API_KEY=your_key_here
    echo.
)

REM Run the new app
streamlit run app_v2.py

pause
