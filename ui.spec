# -*- mode: python -*-
a = Analysis(['ui.py'],
             pathex=['E:\\Workspace\\GitHub\\CrewPairing'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ui.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
