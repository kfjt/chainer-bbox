:: @echo off

if "x"=="x%1" goto usage

call :write_ps %1
call :run_ps
call :del_ps

goto :eof

:write_ps
>%~dpn0.ps1 echo ^
[void][Reflection.Assembly]::LoadWithPartialName("System.Drawing"^);^
$image = New-Object System.Drawing.Bitmap("%1"^);^
$image.RotateFlip("Rotate90FlipNone"^);^
$image.Save("%~dpn1_r90%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.RotateFlip("Rotate90FlipNone"^) ;^
$image.Save("%~dpn1_r180%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.RotateFlip("Rotate90FlipNone"^);^
$image.Save("%~dpn1_r270%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.RotateFlip("Rotate90FlipX"^);^
$image.Save("%~dpn1_x0%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.RotateFlip("Rotate90FlipNone"^);^
$image.Save("%~dpn1_x90%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.RotateFlip("Rotate90FlipNone"^);^
$image.Save("%~dpn1_x180%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.RotateFlip("Rotate90FlipNone"^);^
$image.Save("%~dpn1_x270%~x1", [System.Drawing.Imaging.ImageFormat]::Png^);^
$image.Dispose(^);^

exit /b

:run_ps
powershell -NoProfile -ExecutionPolicy Unrestricted %~dpn0.ps1
exit /b

:del_ps
del %~dpn0.ps1
exit /b

:usage
echo usage: %~nx0 filepath
>nul pause
goto :eof
