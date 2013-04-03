
# BIN2LC3.PY
# This program deciphers binary into easy to read LC-3 instructions.
# @author: Jasper Micah Davey
# @version: 1.0

import re, sys

def main():
	print "\nWelcome to BIN2LC3!"
	print "This program deciphers binary into easy to read LC-3 instructions."
	inst = raw_input("Input the 16-bit binary LC-3 instruction: ")
	# Checks if input is binary
	if not re.match("^[0-1]*$", inst):
		print "\nError! Your input must be in binary!\n"
		sys.exit()
	print "\n"
	# Checks input is 16 characters long
	if len(inst) == 16:
		opcode_op(inst)
		print "\n"
	else:
		print "Your binary instruction is not 16-bit long!\n"

def opcode_op(inst):
	instlist = inst
	opcode = instlist[0:4]
	# Converts instlist into a list to remove the opcode, then converts back to string
	convert = list(instlist)
	del convert[0:4]
	instlist = "".join(convert)
	# Creates a dictionary with the opcodes
	ops = {"adder":"0001","ander":"0101","brer":"0000",
	"jmper":"1100","jsrer":"0100","lder":"0010","ldier":"1010",
	"ldrer":"0110","leaer":"1110","noter":"1001",
	"rtier":"1000","ster":"0011","stier":"1011","strer":"0111",
	"traper":"1111","reserver":"1101"}
	if opcode == ops["adder"]:
		add_op(instlist)
	elif opcode == ops["ander"]:
		and_op(instlist)
	elif opcode == ops["brer"]:
		br_op(instlist)
	elif opcode == ops["jmper"]:
		jmp_op(instlist)
	elif opcode == ops["jsrer"]:
		jsr_op(instlist)
	elif opcode == ops["lder"]:
		ld_op(instlist)
	elif opcode == ops["ldier"]:
		ldi_op(instlist)
	elif opcode == ops["ldrer"]:
		ldr_op(instlist)
	elif opcode == ops["leaer"]:
		lea_op(instlist)
	elif opcode == ops["noter"]:
		not_op(instlist)
	elif opcode == ops["rtier"]:
		rti_op(instlist)
	elif opcode == ops["ster"]:
		st_op(instlist)
	elif opcode == ops["stier"]:
		sti_op(instlist)
	elif opcode == ops["strer"]:
		str_op(instlist)
	elif opcode == ops["traper"]:
		trap_op(instlist)
	elif opcode == ops["reserver"]:
		reserved_op(instlist)
	else:
		print "Your opcode does not match."
	

def add_op(instlist):
	dr = int(instlist[0:3], 2)
	sr1 = int(instlist[3:6], 2)
	if instlist[-6] == "0":
		sr2 = int(instlist[9:12], 2)
		print "ADD: R%r + R%r. Store in R%r." % (sr1, sr2, dr)
	else:
		imm = int(instlist[7:12], 2)
		print "ADD: R%r + %r. Store in R%r." % (sr1, imm, dr)

def and_op(instlist):
	dr = int(instlist[0:3], 2)
	sr1 = int(instlist[3:6], 2)
	if instlist[-6] == "0":
		sr2 = int(instlist[9:12], 2)
		print "AND: R%r and R%r. Store in R%r." % (sr1, sr2, dr)
	else:
		imm = int(instlist[7:12], 2)
		print "AND: R%r and %r. Store in R%r." % (sr1, imm, dr)

def br_op(instlist):
	if instlist[0] == "1":
		n = "N"
	else:
		n = " "
	if instlist[1] == "1":
		z = "Z"
	else:
		z = " "
	if instlist[2] == "1":
		p = "P"
	else:
		p = " "
	offset = int(instlist[3:12], 2)
	print "BR: %s|%s|%s are tested. Memory location in [%r + PC]." % (n, z, p, offset)

def jmp_op(instlist):
	base = int(instlist[3:6], 2)
	if base == 7:
		print "RET: The PC is loaded with the value in R7. \nThis causes a return from a previous JSR instruction."
	else:
		print "JMP: R%r is loaded to PC." % (base)

def jsr_op(instlist):
	if instlist[0] == "1":
		offset = int(instlist[1:12], 2)
		print "JSR: PC stored in TEMP. PC = [%r + PC]. TEMP stored in R7" % (offset)
	else:
		base = int(instlist[3:6], 2)
		print "JSRR: PC stored in TEMP. PC = [R%r + PC]. TEMP stored in R7" % (base)

def ld_op(instlist):
	dr = int(instlist[0:3], 2)
	offset = int(instlist[3:12], 2)
	print "LD: [%r + PC] = a memory address. Content of the address is loaded to R%r." % (offset, dr)

def ldi_op(instlist):
	dr = int(instlist[0:3], 2)
	offset = int(instlist[3:12], 2)
	print "LDI: [%r + PC] = a memory location with the address to another location. \nThe content of the address is loaded to R%r." % (offset, dr)
	print "*Memory interrogated twice*"

def ldr_op(instlist):
	dr = int(instlist[0:3], 2)
	base = int(instlist[3:6], 2)
	offset = int(instlist[6:12], 2)
	print "LDR: [R%r + %r] = a memory address. Content of the address is loaded to R%r." % (base, offset, dr)

def lea_op(instlist):
	dr = int(instlist[0:3], 2)
	offset = int(instlist[3:12], 2)
	print "LEA: [%r + PC] = a memory address. The address in loaded to R%r." % (offset, dr)

def not_op(instlist):
	dr = int(instlist[0:3], 2)
	sr = int(instlist[3:6], 2)
	print "NOT: The bit-wise complement of R%r is stored in R%r." % (sr, dr)

def rti_op(instlist):
	print "RTI: If the processor is running in Supervisor mode, the top two elements\non the Supervisor Stack are popped and loaded into PC, PSR.\nElse returns exception."

def st_op(instlist):
	sr = int(instlist[0:3], 2)
	offset = int(instlist[3:12], 2)
	print "ST: [%r + PC] = a memory address. The content in R%r is stored in this address." % (offset, sr)

def sti_op(instlist):
	sr = int(instlist[0:3], 2)
	offset = int(instlist[3:12], 2)
	print "STI: [%r + PC] = a memory location with the address to another location. \nThe content of R%r is stored in this address." % (offset, sr)
	print "*Memory interrogated twice*"

def str_op(instlist):
	sr = int(instlist[0:3], 2)
	base = int(instlist[3:6], 2)
	offset = int(instlist[6:12], 2)
	print "STR: [R%r + %r] = a memory address. The content in R%r is stored in this address" % (base, offset, sr)

def trap_op(instlist):
	vector = int(instlist[4:12], 2)
	if vector == 32:
		print "TRAP: R7 is loaded with incremented PC. PC is loaded with x20. \nReads a single character from keyboard. ASCII code is copied to R0."
	elif vector == 33:
		print "TRAP: R7 is loaded with incremented PC. PC is loaded with x21. \nWrites a character in R0[7:0] to the console display."
	elif vector == 34:
		print "TRAP: R7 is loaded with incremented PC. PC is loaded with x22. \nWrites a string of ASCII characters to the console display. \nOne character per memory location. \nStarting with address specified in R0 until x0000 in memory location."
	elif vector == 35:
		print "TRAP: R7 is loaded with incremented PC. PC is loaded with x23. \nPrints a prompt on the screen and reads a single character from the keyboard. \nASCII code is copied to R0."
	elif vector == 36:
		print "TRAP: R7 is loaded with incremented PC. PC is loaded with x24. \nWrites a string of ASCII characters to the console display. \nTwo characters per memory location. Bits[7:0] printed first. \nStarting with address specified in R0 until x0000 in memory location."
	elif vector == 37:
		print "TRAP: R7 is loaded with incremented PC. PC is loaded with x25. \nHalts execution and prints a message on the console."
	else:
		print "TRAPVECTOR NOT KNOWN."

def reserved_op(instlist):
	print "RESERVED: Initiates an illegal opcode exception."

main()