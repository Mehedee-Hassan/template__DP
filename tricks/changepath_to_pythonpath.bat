@echo off
set /p path="Enter path: "

set word=/
call set path=%%path:\=%word%%%
echo %path%

pause


:: if you want to run from python with console
::# convert file 
::# """
::# if you need to change path format 


::from subprocess import Popen
::import subprocess
::def run_batch_file(file_path):
::    Popen(file_path,creationflags=subprocess.CREATE_NEW_CONSOLE)
::run_batch_file([r'C:\Users\mehedee\Documents\Python Scripts\mycode_tepmlate\tricks\changepath_to_pythonpath.bat'])

::"""