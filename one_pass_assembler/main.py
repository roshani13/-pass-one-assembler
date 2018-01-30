import sys
from opcode import *
sybl_names = []#TO store symbol names
sybl_size = []#TO store symbol  types size
sybl_totalsize = []#TO store symbol (require memory size in byte) 
sybl_value = []#TO store symbol value
sybl_lineno = []#TO store symbols line no
sybl_type= []#TO store symbol type
sybl_address=[]#to store address
lit = []#to store literal value
lithex = []# to store values of hex of literal
k = 1
reg=['eax','ebx','ecx','edx','esi','edi','esp','ebp','ax','bx','cx','dx','sp','bp','si','di','al','bl','cl','dl','ah','bh','ch','dh']
lenreg=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
ck=['1','2','3','4','5','6','7','8','9','0']
reglist=reglist_Data()
op_data=opcode_Data()
#print op_data[0][0][0]

def checksym(synames,sylist,l_no):
	if synames in sylist:
		print 'LINE ',l_no,":symbole redefin",'"',synames,'"'
		sys.exit()
	elif synames[0] in ck:
		print 'LINE ',l_no,":symbole name not correct",'"',synames,'"'
		sys.exit()
	else:
		return 1
def calsize(l_no,name,s_list,temp,type_size,stp,sum1):#To calculate dd,dq,dw
	tp = []	
	l =temp.count(',')				
	l =(l+1)*type_size
	sum1=sum1+l	
	t=hex_convert(sum1-l)
	sybl_address.append(str(t))
	sybl_lineno.append(str(l_no))				
	sybl_names.append(name)				
	sybl_size.append(str(type_size))
	sybl_totalsize.append(str(l))
	sybl_value.append(s_list)
	sybl_type.append(str(stp))
	return sum1
def calsize_db(l_no,name,temp,val,type_size,stp,sum1):#To calculate db
	k=''.join(temp)
	c = 1
	if(k[c-1]=="'"):
		while(k[c]!="'"):
			c = c + 1
	if(k[c-1]=='"'):
		while(k[c]!='"'):
			c = c + 1
	sybl_totalsize.append(str(c-1))
	sum1=sum1+(c-1)+2	
	t=hex_convert(sum1-(c-1)+2)
	sybl_address.append(str(t))
	if('10,0' in val):
		sybl_value.append(val[1:(len(val)-6)])
	elif(',10' in val):
		sybl_value.append(val[1:(len(val)-4)])
	else:
		sybl_value.append(val[1:(len(val)-1)])
	sybl_lineno.append(str(l_no))				
	sybl_names.append(name)	
	sybl_size.append(str(type_size))
	sybl_type.append(str(stp))
	return sum1
def cal_other(l_no,name,type_size,val,stp,sum1):#To calculate (resd,resb,resq,resw)
	k=type_size*int(val)
	sybl_value.append(val)
	sybl_lineno.append(str(l_no))				
	sybl_names.append(name)	
	sybl_size.append(str(type_size))
	sybl_totalsize.append(str(k))
	sybl_type.append(str(stp))
	sum1=sum1+k
	t=hex_convert(sum1-k)
	sybl_address.append(str(t))
	return sum1
def symbol_table(line,l_no,sum1):#create Symbol table
	list1=line.split()
	for i in range(len(list1)):
		if (list1[i]== 'dd'):
			if(checksym(list1[0],sybl_names,l_no)):
				s_list=list1[2].split()
				z=calsize(l_no,list1[0],s_list,list1[2],4,'dd',sum1)
				return z
		if (list1[i]== 'dq'):
			if(checksym(list1[0],sybl_names,l_no)):
				s_list=list1[2].split()
				z=calsize(l_no,list1[0],s_list,list1[2],8,list1[i],sum1)
				return z
		if (list1[i]== 'dw'):
			if(checksym(list1[0],sybl_names,l_no)):
				s_list=list1[2].split()
				z=calsize(l_no,list1[0],s_list,list1[2],2,list1[i],sum1)	
				return z
		if (list1[i]== 'db'):
			if(checksym(list1[0],sybl_names,l_no)):
				k=list1[i+1:]
				val=' '.join(k)
				z=calsize_db(l_no,list1[0],list1[i+1:],val,1,list1[i],sum1)
				return z
		if (list1[i]== 'resd'):
			if(checksym(list1[0],sybl_names,l_no)):
				z=cal_other(l_no,list1[0],4,list1[2],'resd',sum1)
				return z
		if (list1[i]== 'resq'):
			if(checksym(list1[0],sybl_names,l_no)):
				z=cal_other(l_no,list1[0],8,list1[2],'resq',sum1)
				return z
		if (list1[i]== 'resw'):
			if(checksym(list1[0],sybl_names,l_no)):
				z=cal_other(l_no,list1[0],2,list1[2],'resw',sum1)
				return z
		if (list1[i]== 'resb'):
			if(checksym(list1[0],sybl_names,l_no)):
				z=cal_other(l_no,list1[0],1,list1[2],'resb',sum1)
				return z
	return sum1
def symbol():
	fp=open("msg.asm","r")									
	l_no = 1
	sum1 = 0
	line=fp.readline()
	while(line!=""):
		z=symbol_table(line,l_no,sum1)
		l_no = l_no + 1
		sum1=z
		line=fp.readline()
	fp.close()
fp=open("msg.asm","r")
fp1=open("output.txt","w")

def printsymboltable():#  print symbol table
	fp1.write("\t******************SYMBOL TABLE********************")
	fp1.write("\nlineno\taddress\t\tsymbol\tsize\ttotals\ttype\tvalue\n")
	for i in range(len(sybl_names)):
		fp1.write(sybl_lineno[i])
		fp1.write('\t'+sybl_address[i])
		fp1.write('\t'+sybl_names[i])
		fp1.write('\t'+sybl_size[i])
		fp1.write('\t'+sybl_totalsize[i])
		fp1.write('\t'+str(sybl_type[i]))
		fp1.write('\t'+str(sybl_value[i]))
		fp1.write("\n")
def checkregister(opr):#To check register type
	for i in reglist:
		if opr in reglist[i]:
			return i
def checkmemory(opr):#To check memory type
	i =0
	temp=0
	while(sybl_names[i] != opr):
		i= i+1
	temp =int(sybl_totalsize[i]) * 8
	if( temp > 0 and  temp <256):	
		return 8
	elif( temp > 256 and  temp <65536):
		return 16
	elif( temp > 65536 and  temp <4294967296):
		return 32


def checkopcode(string):#To check register type
	for i in opcode_data:
		if string in opcode_data[i]:
			return i

def hex_convert(sum1):#TO calculate address for instruction in hexadecimal
	str1='00000000'
	k=hex(sum1)
	k=k[2::]
	k=k.upper()
	str1= '0' * (8-len(k))
	str1=str1+str(k)
	return str1
def calline(f,s,lno,name,sum1,line,temp):#TO check instruction type ,address,lieral,memory_type,register_type
	k =0
	i =0
	z=0 
	if s in sybl_names and f in reg:		
		while(sybl_names[i] != s):
			k = k+1
			i = i+1
		i=0
		while(reg[i]!=f):
			i=i+1
		if(temp==1):
			sum1=sum1+5
			t=hex_convert(sum1-5)
		else:
			sum1=sum1+5
			t=hex_convert(sum1-5)
		fp1.write(t)
		regtp=checkregister(f)
		mem=checkmemory(s)
		string1=name+'_reg'+str(regtp)+'_imm'+str(mem)
		kk=checkopcode(string1)
		fp1.write('\t'+str(kk))
		fp1.write(' '+'reg'+str(lenreg[i]))
 		fp1.write(','+'sym#'+str(sybl_lineno[k]))
		fp1.write('\t'+line)
		return sum1
	if f in reg and s in reg:
		i =0
		while(reg[i]!=f):
			i=i+1
		k =0
		while(reg[k]!=s):
			k=k+1
		if(temp==1):
			sum1=sum1+2
			t=hex_convert(sum1-2)
		else:
			sum1=sum1+2
			t=hex_convert(sum1-2)
		fp1.write(t)
		regtp=checkregister(f)
		regtp2=checkregister(s)
		string1=name+'_reg'+str(regtp)+'_reg'+str(regtp2)
		z=checkopcode(string1)
		fp1.write('\t'+str(z))
		fp1.write(' '+'reg'+str(lenreg[i]))
		fp1.write(','+'reg'+str(lenreg[k]))
		fp1.write('\t'+line)
		return sum1
	if f in reg and s not in sybl_names:
		while(reg[k]!=f):
			k=k+1
		if(temp==1):
			sum1=sum1+5
			t=hex_convert(sum1-5)
		else:
			sum1=sum1+3
			t=hex_convert(sum1-3)	
		fp1.write(t)
		regtp=checkregister(f)
		if('dword' in s and str(regtp) == '32'):
			regtp=checkregister(f)
			string1=name+'_reg'+str(regtp)+'_mem32'
			z=checkopcode(string1)
			fp1.write('\t'+str(z))
		else:
			regtp=checkregister(f)
			string1=name+'_reg'+str(regtp)+'_imm8'
			z=checkopcode(string1)
			fp1.write('\t'+str(z))
		fp1.write(' '+'reg'+str(lenreg[k]))	 
		if('dword' in s):
			i =0
			k =0
			if (s[6] in sybl_names):
				while(sybl_names[i]!= s[6]):
					k = k+1
					i = i+1
			fp1.write(','+'dword[sym#'+str(sy_lineno[k])+']')
			fp1.write(''+line)

		else:
			if(len(s)==3 and s[0]=="'"):
				if((ord(s[1])>=65 and ord(s[1])<=90) or (ord(s[1])>=97 and ord(s[1])<=122)):
					if(s[1] not in lit):
						lit.append(str(s[1]))
						lithex.append(hex(ord(s[1])))
						while(lit[i]!=str(s[1])):
							i=i+1
			else:	
				if(int(s) not in lit):
					lit.append(int(s))
					lithex.append(hex(int(s)))
				while(lit[i]!=int(s)):
					i=i+1
			fp1.write(','+'lit'+str(i))
			fp1.write('\t'+line)
		return sum1
	if s in reg and f not in sybl_names:		
		c =0	
		sum1=sum1+6
		while(reg[c]!=s):
			c=c+1
		t=hex_convert(sum1-6)		
		fp1.write(t)
		regtp=checkreg(s)
		if('dword' in f):
			if('dword' in f and str(regtp) == '32'):
				regtp=checkreg(s)
				string1=name+'_mem32'+'_reg'+str(regtp)
				z=checkopcode(string1)
				fp1.write('\t'+str(z))
			i =0
			k =0
			if (f[6] in sybl_names):
				while(sybl_names[i]!= f[6]):
					k = k+1
					i = i+1
			fp1.write(' '+'dword[sym#'+str(sy_lineno[k])+']')
			fp1.write(','+'reg'+str(lenreg[c]))
		if('byte' in f):
			if('byte' in f and str(regtp) == '8'):
				regtp=checkreg(s)
				string1=name+'_mem8'+'_reg'+str(regtp)
				z=checkopcode(string1)
				fp1.write('\t'+str(z))
			i =0
			k =0
			if (f[5]+f[6] in sybl_names):
				while(sybl_names[i]!= f[5]+f[6]):
					k = k+1
					i = i+1
			fp1.write(' '+'byte[sym#'+str(sy_lineno[k])+']')
			fp1.write(','+'reg'+str(lenreg[c]))
		fp1.write(''+line)
		return sum1
def calstring(op,sum1,line,lno):
	sum1=sum1+1
	t=hex_convert(sum1-1)
	fp1.write(t)	
	kk=checkopcode(op)
	fp1.write('\t'+str(kk))
	fp1	.write('\t\t'+line)
	return sum1
def calstringother(op,op2,sum1,line,lno):
	sum1=sum1+2
	t=hex_convert(sum1-2)
	fp1.write(t)	
	kk=checkopcode(op)
	kk1=checkopcode(op2)
	fp1.write('\t'+str(kk)+str(kk1))
	fp1.write('\t\t'+line)
	return sum1

def print_literaltable():#print literal table
	fp1.write("\n\n\t******************LITERAL TABLE********************")
	fp1.write("\nLiteral_no\tLiteral\tLIteral(in hex)\n\n")
	for i in range(len(lit)):
		fp1.write(str(i))
		fp1.write('\t\t'+str(lit[i]))
		fp1.write('\t'+lithex[i])		
		fp1.write("\n")
def table2(line,lno,sum1):#  make opcode table
	z=0
	if(len(line)!=1):
		list1=line.split()
		for i in range(len(list1)):
			if (list1[i]== 'mov') or (list1[i]== 'add'):
				name=list1[i]
				k=list1[1].replace(',',' ')		
				k1=k.split()		
				if(list1[i]== 'mov'):
					z=calline(k1[0],k1[1],lno,name,sum1,line,1)
					return z
				else:
					z=calline(k1[0],k1[1],lno,name,sum1,line,0)
					return z
			elif(list1[i]=='cld') or (list1[i]=='std') or (list1[i]=='lodsb')or (list1[i]=='stosb'):
				z=calstring(list1[i],sum1,line,lno)
				return z
			elif(list1[i]=='rep' or list1[i]=='repnz'):
				z=calstringother(list1[0],list1[1],sum1,line,lno)
				return z	
			else:
				return sum1
	return sum1
def opcodeGenrator():
	lno =0	
	sum1 = 0
	line=fp.readline()
	while(line!=""):#for opcode 
		lno = lno + 1	
		temp=table2(line,lno,sum1)
		sum1= temp
		line=fp.readline()


symbol()
printsymboltable()#writing symbol table in file
fp1.write("\n\nAddress  \tInstruction\t\tOriginal\n\n")
opcodeGenrator() 
print_literaltable()#writing liteltablel in file

