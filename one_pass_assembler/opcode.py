opcode_data = {'00':['add_reg8_reg8','add_mem8_reg8']
,'01':['add_reg16_reg16','add_reg32_reg32','add_mem16_reg16','add_mem32_reg32','add_mem16_reg32','add_mem32_reg16']
,'02':['add_reg8_reg8','add_reg8_mem8']
,'03':['add_reg16_mem16','add_reg32_mem32','add_reg32_mem16','add_reg16_mem32']
,'04':['add_reg8_imm8']
,'05':['add_reg32_imm16','add_reg32_imm32','add_reg32_imm8']
,'28':['sub_reg8_reg8','sub_mem8_reg8']
,'29':['sub_reg16_reg16','sub_reg32_reg32','sub_mem16_reg16','sub_mem32_reg32','sub_mem16_reg32','sub_mem32_reg16']
,'2A':['sub_reg8_reg8','sub_reg8_mem8']
,'2B':['sub_reg16_mem16','sub_reg32_mem32','sub_reg32_mem16','sub_reg16_mem32']
,'2C':['sub_reg8_imm8']
,'2D':['sub_reg32_imm16','sub_reg32_imm32']
,'88':['mov_reg8_reg8','mov_mem8_reg8']
,'89':['mov_reg16_reg16','mov_reg16,reg32','mov_mem16_reg16','mov_mem32_reg32','mov_mem16_reg32','mov_mem32_reg32']
,'8A':['mov_reg8_reg8','mov_reg8_mem8','mov_reg8_imm8']
,'8B':['mov_reg16_reg16','mov_reg16_reg32','mov_reg16_mem32''mov_reg16_mem16','mov_reg32_reg32','mov_reg32_reg16','mov_reg32_mem32','mov_reg32_mem16']
,'B8':['mov_reg32_imm32','mov_reg16_imm16']
,'8C':['mov_reg32_imm8']
,'FC':['cld','std']
,'BF':['mov_reg32_imm16']
,'F2':['repnz']
,'F3':['rep']
,'AC':['lodsb','stosb']
,'A4':['movsb']
,'A5':['movsd']}

reglist={8:['al','bl','cl','dl','ah','bh','ch','dh'],16:['ax','bx','cx','dx','sp','bp','si','di'],32:['eax','ebx','ecx','edx','esi','edi','esp','ebp']}
def opcode_Data():
	return opcode_data
	
def reglist_Data():	
	return reglist
