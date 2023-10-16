#!D:\test\hrun\web_auto\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==20.2.3','console_scripts','pip'
__requires__ = 'pip==20.2.3'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==20.2.3', 'console_scripts', 'pip')()
    )
