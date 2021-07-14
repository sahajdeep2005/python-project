from cx_freeze import*
import sys
base=None
if sys.platform=='Win32':
   base='Win32GUI'
shortcut_table=[('desktopshortcut',
                'desktopFolder',
                'My calculator',
                 'TARGETDIR'
                ' [TARGETDIR]\Smartcalculator.exe',
                None,
                None,
                None,
                None,
                None,
                None)]
msi_data={'shortcut':shortcut_table}
bdist_msi_options={'data':msi_data}

setup(
    # the actual setup & the definition of other misc. info
    name = "Hello", # the program name
    version = "0.1",
    description = "Smart calculator",
    author = "sahaj",
    author_email = "sahajdeeep8949@email.com",
    options={
        "build_exe": msi_data,
        "bdist_msi": bdist_msi_options,
    },

     executables = [
         Executable(script='Smartcalculator',
                    base=base,
                    icon=None



    )




    ]
)




