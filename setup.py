from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(name="pyvmware",
	version='1.0',
    ext_modules=cythonize([Extension('pyvmware',
                             ['pyvmware.pyx'],
                             language="c++",
                             # extra_compile_args=['/EHs'],
                             # extra_link_args=["-std=c++11"]
                             )])
    )