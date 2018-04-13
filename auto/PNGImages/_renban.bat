@echo off

if "x%1"=="x" goto usage

setlocal

set _xhakusi=%~dp0hakusi.png
set _xtarget=%~dp0%1

set _xstart=%2
if not defined _xstart set _xstart=1

set _xend=%3
if not defined _xend set _xend=250

for /l %%a in (%_xstart%, 1, %_xend%) do call :_copy %%a

endlocal
:: pause
goto :eof

:_copy
 >nul copy %_xhakusi% %_xtarget%\%1.png
 echo created %1.png
exit /b

:usage
echo usage
echo %~nx0 shape start end
echo  shape maru or sankaku or batu
echo  start default 1
echo  end default 250
pause
goto :eof
