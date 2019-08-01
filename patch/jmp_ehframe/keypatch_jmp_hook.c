/* intel syntax for keypatch */
mov     eax, [rbp-4];
cdqe;
mov     rax, ds:note[rax*8];
test rax,rax;
jz 0x400A3E; //keypatch 在跳转（jmp、call）采用十六进制地址进行（否则无法编码）
mov     eax, [rbp-4];
cdqe;
mov     rax, ds:note[rax*8];
mov rdi,rax;
call 0x400710;//call _free
mov     eax, [rbp-4];cdqe;
mov rcx,0;
mov ds:note[rax*8],rcx;//关于mov寻址操作约定：段地址不能直接赋予立即数
jmp 0x400A48

//keypatch 使用一行

//mov     eax, [rbp-4];cdqe;mov     rax, ds:note[rax*8];test rax,rax;jz 0x400A3E;mov     eax, [rbp-4];cdqe;mov     rax, ds:note[rax*8];mov rdi,rax;call 0x400710;mov     eax, [rbp-4];cdqe;mov rcx,0;mov ds:note[rax*8],rcx;jmp 0x400A48