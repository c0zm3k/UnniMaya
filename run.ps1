# Activate .venv and run app
if (Test-Path ".\.venv\Scripts\Activate.ps1" ) {
    Write-Host "🚀 Activating virtual environment and launching FutureFit..." -ForegroundColor Cyan
    .\.venv\Scripts\Activate.ps1
    python app.py
} else {
    Write-Error "❌ Virtual environment not found at .venv. Please run: python -m venv .venv"
}
