set PYTHONUNBUFFERED=1
SET PYTHONPATH=C:\Dev\AskYourCode\AskYourCodePlugin\src
set HTTP_PORT=50201
python -O -u src\embed\embedder.py
rem >C:\tmp\embedder-%HTTP_PORT%.log 2>&1
echo "!!! CRASHED !!!"
pause
