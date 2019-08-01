import lief
from pwn import *

def patch_jmp(file,op,srcaddr,dstaddr,arch="amd64"):
	length = (dstaddr-srcaddr-2)
	print hex(length)
	order = chr(op)+chr(length)
	print disasm(order,arch=arch)
	file.patch_address(srcaddr,[ord(i) for i in order])

def patch_call(file,srcaddr,dstaddr,arch="amd64"):
	length = p32((dstaddr-srcaddr-5)&0xffffffff)
	order = "\xe8"+length
	print disasm(order,arch=arch)
	file.patch_address(srcaddr,[ord(i) for i in order])
	
# add hook's patched func to binary as a new segment
binary = lief.parse("./vul")
hook = lief.parse("./hook")

print hook.get_section(".text").content
print hook.segments[0].content

segment_added = binary.add(hook.segments[0])
hook_fun = hook.get_symbol("my_delete_note")
print hex(segment_added.virtual_address)
print hex(hook_fun.value)

# hook call delete_note
dstaddr = segment_added.virtual_address + hook_fun.value
srcaddr = 0x400B9A
patch_call(binary,srcaddr,dstaddr)

# patch print_inputidx
dstaddr = 0x400760
srcaddr = segment_added.virtual_address + 0x2f2
patch_call(binary,srcaddr,dstaddr)

# patch call read_int
dstaddr = 0x4008d6
srcaddr = segment_added.virtual_address +0x2fc
patch_call(binary,srcaddr,dstaddr)

# patch call free
dstaddr = 0x400710
srcaddr = segment_added.virtual_address + 0x323
patch_call(binary,srcaddr,dstaddr)

# patch call puts
dstaddr = 0x400740
srcaddr = segment_added.virtual_address + 0x340
patch_call(binary,srcaddr,dstaddr)

# patch jmp printnosuchnote short jmp
dstaddr = segment_added.virtual_address+0x33b
srcaddr = segment_added.virtual_address+0x314
patch_jmp(binary,0x74,srcaddr,dstaddr)

# patch jmp end_func
srcaddr = segment_added.virtual_address + 0x339
dstaddr = segment_added.virtual_address + 0x345
patch_jmp(binary,0xeb,srcaddr,dstaddr)

binary.write("patch_add_segment")