@echo off

echo run this file as admin
echo remember to tick th "add pip to path"

echo press enter to start
set /p DUMMY=Hit ENTER to continue...

python-3.7.0-amd64.exe

echo updating "pip"
pip install --upgrade pip

echo installing dependencies
echo ======================================================
echo https://pypi.org/project/cefpython3/
echo https://pypi.org/project/pynput/
echo ======================================================
echo press enter to continue
set /p DUMMY=Hit ENTER to continue...


echo Installing "cefpython3" for web browser
echo https://pypi.org/project/cefpython3/
pip install cefpython3

echo

echo Installing "pynput" for Keybind
echo https://pypi.org/project/pynput/
pip install pynput

echo done
echo
echo
echo
echo Message Connor if something does not work. Connor2#8804

echo numpad 9 = +1 to counter
echo numpad 6 = -1 to counter

set /p DUMMY=Hit ENTER to continue...
