from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

adc2dac_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'SINEV', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'Sinusoidal voltage source', 'amplitude':UnitValue(2 V), 'pyspice':{'name': 'SinusoidalVoltageSource', 'kw': {'dc_offset': 'dc_offset', 'ac_magnitude': 'ac_magnitude', 'ac_phase': 'ac_phase', 'offset': 'offset', 'amplitude': 'amplitude', 'frequency': 'frequency', 'delay': 'delay', 'damping_factor': 'damping_factor', 'p': 'node_plus', 'n': 'node_minus'}, 'add': <function add_part_to_circuit at 0x7fddd85aba60>}, '_match_pin_regex':False, '_aliases':Alias({'sinusoidalvoltage', 'SINUSOIDALVOLTAGE', 'sinev'}), 'frequency':50000000.0, 'keywords':'sinusoidal voltage source', 'offset':UnitValue(0.0 V), 'ref_prefix':'V', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias({'sinusoidalvoltage', 'SINUSOIDALVOLTAGE', 'sinev'}), 'pin':None, 'footprint':None, 'pins':[
            Pin(num='1',name='p',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='n',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'A', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'XSPICE code module', 'pyspice':{'name': 'A', 'kw': {'model': 'model'}, 'add': <function add_xspice_to_circuit at 0x7fddd85abd30>}, 'model':<skidl.tools.spice.XspiceModel object at 0x7fddd83fadf0>, '_match_pin_regex':False, '_aliases':Alias({'XSPICE', 'xspice'}), 'keywords':'XSPICE', 'ref_prefix':'A', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias({'XSPICE', 'xspice'}), 'pin':None, 'footprint':None, 'pins':[
            Pin(func=Pin.types.UNSPEC,do_erc=True),
            Pin(func=Pin.types.UNSPEC,do_erc=True)] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'Resistor', 'pyspice':{'name': 'R', 'kw': {'value': 'resistance', 'resistance': 'resistance', 'ac': 'ac', 'multiplier': 'multiplier', 'm': 'multiplier', 'scale': 'scale', 'temp': 'temperature', 'temperature': 'temperature', 'dtemp': 'device_temperature', 'device_temperature': 'device_temperature', 'noisy': 'noisy', 'p': 'plus', 'n': 'minus'}, 'add': <function add_part_to_circuit at 0x7fddd85aba60>}, 'keywords':'res resistor', '_match_pin_regex':False, 'ref_prefix':'R', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':None, 'pins':[
            Pin(num='1',name='p',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='n',func=Pin.types.PASSIVE,do_erc=True)] })])