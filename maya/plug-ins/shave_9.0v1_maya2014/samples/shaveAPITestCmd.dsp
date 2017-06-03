# Microsoft Developer Studio Project File - Name="shaveAPITestCmd" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Dynamic-Link Library" 0x0102

CFG=shaveAPITestCmd - Win32 Debug50
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "shaveAPITestCmd.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "shaveAPITestCmd.mak" CFG="shaveAPITestCmd - Win32 Debug50"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "shaveAPITestCmd - Win32 Release50" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "shaveAPITestCmd - Win32 Debug50" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
MTL=midl.exe
RSC=rc.exe

!IF  "$(CFG)" == "shaveAPITestCmd - Win32 Release50"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release50"
# PROP BASE Intermediate_Dir "Release50"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "shaveAPITestCmd_Release50"
# PROP Intermediate_Dir "shaveAPITestCmd_Release50"
# PROP Ignore_Export_Lib 1
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MT /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "SHAVEAPITESTCMD_EXPORTS" /YX /FD /c
# ADD CPP /nologo /MT /W3 /GX /I "$(MAYA_5_0_LOCATION)\include" /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "NT_PLUGIN" /FD /c
# SUBTRACT CPP /YX
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x1009 /d "NDEBUG"
# ADD RSC /l 0x1009 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /machine:I386
# ADD LINK32 libShaveAPI.lib Foundation.lib OpenMaya.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /machine:I386 /out:"shaveAPITestCmd_Release50/shaveAPITestCmd.mll" /libpath:"$(MAYA_5_0_LOCATION)\lib" /export:initializePlugin /export:uninitializePlugin
# SUBTRACT LINK32 /pdb:none /incremental:yes

!ELSEIF  "$(CFG)" == "shaveAPITestCmd - Win32 Debug50"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "shaveAPITestCmd___Win32_Debug50"
# PROP BASE Intermediate_Dir "shaveAPITestCmd___Win32_Debug50"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "shaveAPITestCmd_Debug50"
# PROP Intermediate_Dir "shaveAPITestCmd_Debug50"
# PROP Ignore_Export_Lib 1
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MTd /W3 /Gm /GX /ZI /Od /D "WIN32" /D "_DEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "SHAVEAPITESTCMD_EXPORTS" /YX /FD /GZ /c
# ADD CPP /nologo /G6 /MT /W3 /ZI /Od /I "$(MAYA_5_0_LOCATION)\include" /D "WIN32" /D "_DEBUG" /D "_WINDOWS" /D "_MBCS" /D "NT_PLUGIN" /FR /FD /GZ /c
# SUBTRACT CPP /YX
# ADD BASE MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x1009 /d "_DEBUG"
# ADD RSC /l 0x1009 /d "_DEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /debug /machine:I386 /pdbtype:sept
# ADD LINK32 libShaveAPI.lib Foundation.lib OpenMaya.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /incremental:no /debug /machine:I386 /out:"shaveAPITestCmd_Debug50/shaveAPITestCmd.mll" /pdbtype:sept /libpath:"$(MAYA_5_0_LOCATION)\lib" /export:initializePlugin /export:uninitializePlugin
# SUBTRACT LINK32 /pdb:none

!ENDIF 

# Begin Target

# Name "shaveAPITestCmd - Win32 Release50"
# Name "shaveAPITestCmd - Win32 Debug50"
# Begin Group "Source Files"

# PROP Default_Filter "cpp;c;cxx;rc;def;r;odl;idl;hpj;bat"
# Begin Source File

SOURCE=.\shaveAPITestCmd.cpp
# End Source File
# End Group
# Begin Group "Header Files"

# PROP Default_Filter "h;hpp;hxx;hm;inl"
# End Group
# Begin Group "Resource Files"

# PROP Default_Filter "ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe"
# End Group
# End Target
# End Project
