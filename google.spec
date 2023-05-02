# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None
javascript_pkg = []

javascript_pkg += collect_data_files('javascript')
javascript_pkg += [('.\\node_modules\\', '.\\node_modules')]
added_files = ('.\\utils\\img_display.mjs', '.\\utils')
javascript_pkg.append(added_files)
pkg_json = ('.\\package.json', '.')

javascript_pkg.append(pkg_json)

a = Analysis(
    ['google'],
    pathex=[],
    binaries=[],
    datas=javascript_pkg,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='google',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
