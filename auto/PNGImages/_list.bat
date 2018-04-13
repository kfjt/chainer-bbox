@echo off
pushd %~dp0

>..\ImageSets\Main\train.txt type nul
FOR /F %%a IN ('dir /b /od *.png') DO call :_fn %%a

popd
:: pause
goto :eof

:_fn
if "hakusi"=="%~n1" exit /b
>>..\ImageSets\Main\train.txt echo %~n1
exit /b
