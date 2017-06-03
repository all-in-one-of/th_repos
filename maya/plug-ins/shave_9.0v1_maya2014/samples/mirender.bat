@echo off
REM
REM This sample script shows how to render a Maya scene from the command line
REM using the mental ray standalone renderer.
REM
set /a retries=10
if a%1b==ab goto badArgs
if a%2b==ab goto checkFile
:badArgs
echo Usage: mirender mayaSceneFile
goto done

:checkFile
if exist %1 goto getTempFile
echo Cannot read scene file '%1'.
goto done

:getTempFile
set tempFile=%RANDOM%.mi
if not exist %tempFile% goto doRender
set /a retries = retries - 1
if not a%retries%b==a0b goto getTempFile
echo Error: could not find a temp file name which is not already in use.
goto done

:doRender
mayabatch -command "Mayatomr -mi -file \"%tempFile%\" \"%1\""
ray -v 4 %tempFile%

if exist %tempFile% del %tempFile%

:done
