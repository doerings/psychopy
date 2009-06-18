#emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: t -*- 
#ex: set sts=4 ts=4 sw=4 noet:
"""
 Little helper script to minimize intrusion into upstream code relying
 on psychopy.serial availability.

 Copyright (C) 2009, Yaroslav Halchenko

 Distributed under the license terms of python-psychopy package.
"""
import sys

if sys.version_info[:2] >= (2, 5):
	# enforce absolute import
 	serial = __import__('serial', globals(), locals(),
						['Serial', 'PARITY_EVEN', 'STOPBITS_TWO'], 0)
	# hackish way to bind needed names, not sure why
	# fromlist argument wasn't in effect
	locals().update(serial.__dict__)
	#Serial = serial.Serial
	#PARITY_EVEN = serial.PARITY_EVEN
	#STOPBITS_TWO = serial.STOPBITS_TWO
else:
	# little trick to be able to import 'serial' package (which has same
	# name)
	oldname = __name__
	# crazy name with close to zero possibility to cause whatever
	__name__ = 'iaugf9zrkjsbdv99'
	from serial import *
	# restore old settings
	__name__ = oldname
