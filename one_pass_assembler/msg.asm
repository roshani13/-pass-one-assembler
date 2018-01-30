section .data
	a dd 10
	b dd 20
	c dd 30
	d dd 50
	msg2 db "PUCSD",10,0
section .text
	global main
	extern printf
main:
	mov eax,a
	mov edx,b
	mov eax,ebx
	add eax,a
	add ebx,b
	mov ecx,12
	mov eax,14
	mov edx,12
	mov eax,13
	mov eax,'a'
	mov al,'z'
	
	
