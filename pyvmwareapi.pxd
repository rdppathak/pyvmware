# distutils: language = c++

cdef extern from "VmwareApi.h":

	cppclass VmwareApi:
		VmwareApi() except +