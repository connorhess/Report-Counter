@echo off
echo Starting.........


pyinstaller --onefile --noconsole --noconfirm --name "Sit_Counter" "Main.py"

//pyinstaller --noconfirm --name "Sit_Counter" "Main.py"


echo ====================================
echo ================Done================
echo ====================================

set /p DUMMY=Hit ENTER to continue...

