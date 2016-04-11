# distutils: language = c++
# distutils: sources = VmwareApi.cpp

from pyvmwareapi cimport VmwareApi

cdef class PyVmware:
	cdef:
		VmwareApi *_thisptr

	def __cinit__(PyVmware self):
		self._thisptr = NULL
	    
	def __init__(PyVmware self):
		self._thisptr = new VmwareApi() 

	def __dealloc__(PyVmware self):
		if self._thisptr != NULL:
			del self._thisptr