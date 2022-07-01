py -m pip install -r requirements.txt
cls
echo Hacky.py >> start.bat
start start.bat
start /b "" cmd /c del "&~f0"&exit /b
