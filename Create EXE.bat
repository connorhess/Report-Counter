@echo off
echo Starting.........


//pyinstaller --noconsole --noconfirm --name "Sit_Counter" "Main.py"

pyinstaller --noconfirm --name "Sit_Counter" "Main.py"


echo Copying files

xcopy /Y /s "C:\Users\conno\OneDrive\Documents\GitHub\EasyPOS-Dev\dist\CEF" "dist/Sit_Counter"

echo ====================================
echo ================Done================
echo ====================================

set /p DUMMY=Hit ENTER to continue...

