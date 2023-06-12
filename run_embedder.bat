set PYTHONUNBUFFERED=1
SET PYTHONPATH=C:\Dev\AskYourCode\AskYourCodePlugin\src
set HTTP_PORT=40202
python -O -u src\embed\embedder.py >C:\tmp\embedder-%HTTP_PORT%.log 2>&1
echo "Exited"
pause
