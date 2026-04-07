@echo off
echo Testing adversarial framework imports...
cd /d C:\Users\Lakshya\Desktop\YASH\AI_QA_Agent
python test_adversarial.py
if %errorlevel% == 0 (
    echo.
    echo ✅ All imports successful!
    echo.
    echo You can now run: streamlit run app.py
) else (
    echo.
    echo ❌ Import test failed!
    exit /b 1
)
pause
