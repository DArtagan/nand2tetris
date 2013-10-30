from CS410_inst_py import hack2xml
from asm import asm
from instruction import *

# MAIN
hack2xml('machine.hack', 'machine.xml')
assembly = asm('machine.xml', 'assembly.asm')
print(assembly)
assembly.write()
