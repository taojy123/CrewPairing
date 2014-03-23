# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'ui.py'],
             pathex=['C:\\Users\\TJY\\Desktop\\CrewPairing'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'ui.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
