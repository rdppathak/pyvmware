#include "vixDiskLib.h"
#include "VmwareApi.h"

VmwareApi::VmwareApi(){
	printf("VmwareApi constructor\n");
	VixDiskLibConnectParams cnxParams = {0};
}

VmwareApi::~VmwareApi(){
	printf("VmwareApi destructor\n");
}