Write-Host "Testing adversarial framework imports..." -ForegroundColor Cyan

$env:PYTHONPATH = "C:\Users\Lakshya\Desktop\YASH\AI_QA_Agent"

python "C:\Users\Lakshya\Desktop\YASH\AI_QA_Agent\test_adversarial.py"

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ All tests passed!" -ForegroundColor Green
} else {
    Write-Host "`n❌ Tests failed!" -ForegroundColor Red
    exit 1
}
