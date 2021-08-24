from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

__init___lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'SINEV', 'dest':TEMPLATE, 'tool':SKIDL, 'amplitude':UnitValue(1.0 V), '_aliases':Alias({'sinev', 'sinusoidalvoltage', 'SINUSOIDALVOLTAGE'}), 'frequency':FrequencyValue(1 kHz), 'keywords':'sinusoidal voltage source', 'description':'Sinusoidal voltage source', 'pyspice':{'name': 'SinusoidalVoltageSource', 'kw': {'dc_offset': 'dc_offset', 'ac_magnitude': 'ac_magnitude', 'ac_phase': 'ac_phase', 'offset': 'offset', 'amplitude': 'amplitude', 'frequency': 'frequency', 'delay': 'delay', 'damping_factor': 'damping_factor', 'p': 'node_plus', 'n': 'node_minus'}, 'add': <function add_part_to_circuit at 0x7f85a067d550>}, '_match_pin_regex':False, 'offset':UnitValue(0.0 V), 'ref_prefix':'V', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias({'sinev', 'sinusoidalvoltage', 'SINUSOIDALVOLTAGE'}), 'pin':None, 'footprint':None, 'pins':[
            Pin(num='1',name='p',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='n',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'A', 'dest':TEMPLATE, 'tool':SKIDL, 'model':<skidl.tools.spice.XspiceModel object at 0x7f861efcc880>, '_aliases':Alias({'xspice', 'XSPICE'}), 'keywords':'XSPICE', 'description':'XSPICE code module', 'pyspice':{'name': 'A', 'kw': {'model': 'model'}, 'add': <function add_xspice_to_circuit at 0x7f85a067d820>}, '_match_pin_regex':False, 'ref_prefix':'A', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias({'xspice', 'XSPICE'}), 'pin':None, 'footprint':None, 'pins':[
            Pin(func=Pin.types.UNSPEC,do_erc=True),
            Pin(func=Pin.types.UNSPEC,do_erc=True)] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'res resistor', 'description':'Resistor', '_match_pin_regex':False, 'pyspice':{'name': 'R', 'kw': {'value': 'resistance', 'resistance': 'resistance', 'ac': 'ac', 'multiplier': 'multiplier', 'm': 'multiplier', 'scale': 'scale', 'temp': 'temperature', 'temperature': 'temperature', 'dtemp': 'device_temperature', 'device_temperature': 'device_temperature', 'noisy': 'noisy', 'p': 'plus', 'n': 'minus'}, 'add': <function add_part_to_circuit at 0x7f85a067d550>}, 'ref_prefix':'R', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':None, 'pins':[
            Pin(num='1',name='p',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='n',func=Pin.types.PASSIVE,do_erc=True)] })])