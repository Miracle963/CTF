import lief
from pwn import *

def patch_jmp(file,srcaddr,dstaddr,arch="amd64"):
	length = p32((dstaddr-srcaddr-5)&0xffffffff) # long jmp address calc
	print length
	order = "\xe9"+length
	print disasm(order,arch=arch)
	file.patch_address(srcaddr,[ord(i) for i in order])
    
def patch_jz(file,srcaddr,dstaddr,arch="amd64"):
    length = p32((dstaddr-srcaddr-6)&0xffffffff)
    order = "\x0f\x84"+length
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


# hook delete_note to eh_frame
dstaddr = bin_eh_frame.virtual_address
srcaddr = 0x400A15
patch_jmp(binary,srcaddr,dstaddr)

# patch jz put_nosuchnote
dstaddr = 0x400A3E
srcaddr = bin_eh_frame.virtual_address + (0x289-hook_func_base)
patch_jz(binary,srcaddr,dstaddr)

# patch call free
dstaddr = 0x400710
srcaddr = bin_eh_frame.virtual_address + (0x29c-hook_func_base)
patch_call(binary,srcaddr,dstaddr)

# patch jmp back to delete_note end
dstaddr = 0x400A48
srcaddr = bin_eh_frame.virtual_address + (0x2b2 - hook_func_base)
patch_jmp(binary,srcaddr,dstaddr)

binary.write("patch_jmp_ehframe")