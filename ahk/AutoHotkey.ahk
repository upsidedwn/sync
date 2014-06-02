
; Define functions here
RunConEmu(path=false)
{
  if(path)
  {
    Run, "C:\Program Files\ConEmu\ConEmu64.exe" /dir "%path%"
  }
  else
  {
    Run, "C:\Program Files\ConEmu\ConEmu64.exe" /dir "%A_Desktop%"
  }
}

IsDir(path) {
  return InStr(FileExist(path), "D")
}

; Define hotkeys here
F6::Reload

^Space::
if WinActive("ahk_class CabinetWClass")
{
  WinGetText, text
  found_pos:= RegExMatch(text, "m)Address: (.*)$", found_address)
  if(found_pos >0) {
    if InStr(found_address1, ":") {
      RunConEmu(found_address1)
    }
    else {
      saved_clipboard := clipboard
      clipboard := " "
      Send ^c
      ClipWait
      if(InStr(clipboard, ":")) {
        if(IsDir(clipboard)) {
          updir := clipboard
        }
        else {
          updir := clipboard . "\..\"
        }
      }
      else {
        updir := A_Desktop
      }

      RunConEmu(updir)
      clipboard := saved_clipboard
    }
  }
}
else {
  RunConEmu()
}
return
