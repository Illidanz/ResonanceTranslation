# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['tool.py'],
             pathex=['D:\\roms\\resonance'],
             binaries=[('xdelta.exe', '.'), ('sign_np.exe', '.'), ('armips.exe', '.'), ('UMD-replace.exe', '.')],
             datas=[('bin_patch.asm', '.'), ('bin_patch_PS2.asm', '.')],
             hiddenimports=['pkg_resources.py2_warn'],
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
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon.ico')
