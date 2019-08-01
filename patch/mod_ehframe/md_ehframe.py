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

hook_func_base = 0x279

hook_sec = hook.get_section(".text")
bin_eh_frame =  binary.get_section(".eh_frame")

print hook_sec.content
print bin_eh_frame.content

bin_eh_frame.content = hook_sec.content
print bin_eh_frame.content


# hook call delete_note
dstaddr = bin_eh_frame.virtual_address
srcaddr = 0x400B9A
patch_call(binary,srcaddr,dstaddr)

# patch print_inputidx
dstaddr = 0x400760
srcaddr = bin_eh_frame.virtual_address + (0x28b-hook_func_base)
patch_call(binary,srcaddr,dstaddr)

# patch call read_int
dstaddr = 0x4008d6
srcaddr = bin_eh_frame.virtual_address +(0x295-hook_func_base)
patch_call(binary,srcaddr,dstaddr)

# patch call free
dstaddr = 0x400710
srcaddr = bin_eh_frame.virtual_address + (0x2bc-hook_func_base)
patch_call(binary,srcaddr,dstaddr)

# patch call puts
dstaddr = 0x400740
srcaddr = bin_eh_frame.virtual_address + (0x2d9-hook_func_base)
patch_call(binary,srcaddr,dstaddr)

# patch jmp printnosuchnote short jmp
dstaddr = bin_eh_frame.virtual_address+(0x2d4-hook_func_base)
srcaddr = bin_eh_frame.virtual_address+(0x2ad -hook_func_base)
patch_jmp(binary,0x74,srcaddr,dstaddr)

# patch jmp end_func
srcaddr = bin_eh_frame.virtual_address + (0x2d2-hook_func_base)
dstaddr = bin_eh_frame.virtual_address + (0x2de-hook_func_base)
patch_jmp(binary,0xeb,srcaddr,dstaddr)

binary.write("patch_md_ehframe")