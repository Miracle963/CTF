mov     eax, [rbp-4];
cdqe;
mov     rax, ds:note[rax*8];
test rax,rax;
jz 0x400A3E;
mov     eax, [rbp-4];
cdqe;
mov     rax, ds:note[rax*8];
mov rdi,rax;call 0x400710;
mov     eax, [rbp-4];
cdqe;
mov rcx,0;
mov ds:note[rax*8],rcx;
jmp 0x400A48 