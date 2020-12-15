# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)
block_cipher = None


a = Analysis(['AppMain.py','adding.py','adhikari.py','carlson.py','charef.py','error.py','FirstCauer.py','FirstFoster.py','mastuda.py','Methodss.py','modoustaloup.py','oustaloup.py','phik.py','readOut.py','SecondCauer.py','SecondFoster.py','TheileSecondCFE.py','valsa.py'],
             pathex=['D:\\DocumentsHDD\\BTP\\GUIapp\\Python_files','C:\\Program Files\\Python37\\Lib\\site-packages\\PyQt5\\Qt\\bin'],
             binaries=[('C:\\Program Files\\Python37\\Lib\\site-packages\\PyQt5\\Qt\\plugins\\platforms\\qwindows.dll','.'),('C:\\Program Files\\Python37\\Lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Core.dll','.'),('C:\\Program Files\\Python37\\Lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Gui.dll','.'),('C:\\Program Files\\Python37\\Lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Widgets.dll','.')],
             datas=[('D:\\DocumentsHDD\\BTP\\GUIapp\\Python_files\\Pspice_files','Pspice_files'),('C:\\Program Files\\Python37\\Lib\\site-packages\\PySpice\\Spice\\NgSpice','PySpice\\Spice\\Ngspice')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.binaries,
          a.datas,
          [],
          name='AppMain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=True,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )