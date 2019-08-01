asm(
	"push %rbp\n"
	"mov %rsp,%rbp\n"
	"sub $0x10,%rsp\n"
	"mov $0x400c87,%edi\n"
	"mov $0x0,%eax\n"
	/*call printf*/
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	"mov $0x0,%eax\n"
	/*call read_int*/
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	/* save idx to [rbp-4]*/
	"mov %eax,-0x4(%rbp)\n"
	/* load idx from [rbp-4]*/
	"mov -0x4(%rbp),%eax\n"
	"cdqe\n"
	/* load ptr from ds:note[rax*8]*/
	"mov 0x6020e0(,%rax,8),%rax\n"
	"test %rax,%rax\n"
	/*jmp short print nosuchnote*/
	/* 0x2d2-0x2ad-2 */
	"nop\n"
	"nop\n"
	/*end jmp*/
	"mov -0x4(%rbp),%eax\n"
	"cdqe\n"
	"mov 0x6020e0(,%rax,8),%rdi\n"
	/*call free*/
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	/* ptr = NULL,段寄存器不能传立即数*/
	"mov $0x0,%ecx\n"
	"mov %ecx,0x6020e0(,%rax,8)\n"
	/*end*/
	/*jmp end delete_func*/
	/* 0x2dc-0x2d0-2*/
	"nop\n"
	"nop\n"
	/*print nosuchnote*/
	"mov $0x400C8E,%edi\n"
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	"nop\n"
	/*end delete_func*/
	"leave\n"
	"ret\n"
);