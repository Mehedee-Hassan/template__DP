@echo off
set /p path="Enter path: "

set word=/
call set path=%%path:\=%word%%%
echo %path%

pause