import sys
from ctypes import *

dl = CDLL("",RTLD_GLOBAL)

class call_frame_t (Structure):
	pass

class xlator_t (Structure):
	pass

class dict_t (Structure):
	pass

class loc_t (Structure):
	_fields_ = [
		( "path",	c_char_p ),
		( "name",	c_char_p ),
		( "inode",	c_void_p ),
		( "parent",	c_void_p ),
		( "gfid", c_char * 16 ),
		( "pargfid", c_char * 16 )
	]

class inode_t (Structure):
	pass

class iatt_t (Structure):
	pass

lookup_fop_sig = (c_int, POINTER(call_frame_t), POINTER(xlator_t),
						 POINTER(loc_t), POINTER(dict_t))
lookup_fop_t = apply(CFUNCTYPE,lookup_fop_sig)

lookup_cbk_sig = (c_int, POINTER(call_frame_t), c_long, POINTER(xlator_t),
						 c_int, c_int, POINTER(inode_t),
						 POINTER(iatt_t), POINTER(dict_t), POINTER(iatt_t))
lookup_cbk_t = apply(CFUNCTYPE,lookup_cbk_sig)

dl.set_lookup_fop.restype = None
dl.set_lookup_fop.argtypes = [ c_long, lookup_fop_t ]
dl.set_lookup_cbk.restype = None
dl.set_lookup_cbk.argtypes = [ c_long, lookup_cbk_t ]
dl.wind_lookup.restype = None
dl.wind_lookup.argtypes = list(lookup_fop_sig[1:])
dl.unwind_lookup.restype = None
dl.unwind_lookup.argtypes = list(lookup_cbk_sig[1:])

