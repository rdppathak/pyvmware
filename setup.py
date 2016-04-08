from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(name="pyvmware",
	version='1.0',
    ext_modules=cythonize([Extension('pyvmware',
                             ['pyvmware.pyx'],
                             language="c++",
                             include_dirs=["C:\\Program Files (x86)\\VMware\\VMware Virtual Disk Development Kit\\include"],
                             library_dirs=["C:\\Program Files (x86)\\VMware\\VMware Virtual Disk Development Kit\\lib"]
                             # extra_compile_args=['/EHs'],
                             # extra_link_args=["-std=c++11"]
                             )])
    )