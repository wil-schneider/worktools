#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^2::
Run, mspaint.exe
WinWait, Untitled - Paint ; wait for Paint to open
WinActivate, Untitled - Paint ; bring Paint to the front
Sleep, 500 ; may or may not be necessary
Send, {ctrl down}{v down}{v up}{ctrl up} ; paste
Sleep, 500 ; may or may not be necessary
Send, ^X ; cut
Send, {ctrl down}{s down}{s up}{ctrl up} ; save
return

Esc::ExitApp
