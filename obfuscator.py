import re
import random
#i need to remove the comments. everything will be ignored after "//" for now i will skip block comments ("/*...*/") to save time
def stripComments(line):
	for i in range(len(line)-1):
		if line[i]=="/" and line[i+1]=="/":
			#return everything up to the first "/"
			return line[:i]
	#return everything becasue "//" was not found
	return line

#this will be used in combonation with the findVars function.
# i do not need to find any thing that is in quotes becasue it is a literal string.
def stripQuotes(line):
	needToFind=""
	i=0
	result=""
	previous=0
	while i<len(line):
		#need to look for either kind of quote then find the matching one
		
		if line[i]=="'" or line[i]=='"':
			
			needToFind=line[i]
			j=i+1
			while j <len(line):
				if line[j]==needToFind:
					
					result+=line[previous:i]
					
					previous=j+1
					
					i=j+1
					break
				else: j+=1


		else: i+=1
	
	result+=line[previous:]
	return result




def createRandomVar():
	letters="abcdefghijklmnopqrstufwxyz"
	result=random.choice(letters)
	letters+="1234567890"
	#create variables with length between 3 and 10
	for i in range(random.randint(3, 10)):
		result+=random.choice(letters)
	return result

def findVars(line):
	noQuotes=stripQuotes(line)
	pattern=re.compile("[a-zA-Z_$][a-zA-Z_$0-9]*")
	result=pattern.findall(noQuotes)
	return result



#these are globals
reserveWords=['abstract', 'else', 'instanceof', 'super', 'boolean', 
		'enum', 'int', 'switch', 'break', 'export', 'interface', 'synchronized', 
		'byte', 'extends', 'let', 'this', 'case', 'false', 'long', 'throw', 'catch', 
		'final', 'native', 'throws', 'char', 'finally', 'new', 'transient', 'class', 
		'float', 'null', 'true', 'const', 'for', 'package', 'try', 'continue', 'function', 
		'private', 'typeof', 'debugger', 'goto', 'protected', 'var', 'default', 'if', 
		'public', 'void', 'delete', 'implements', 'return', 'volatile', 'do', 'import', 
		'short', 'while', 'double', 'in', 'static', 'with', 'console', 'log']
varmap={}
newVars=[]
newScript=[]

if __name__=="__main__":
	#ignore these words. these are important
	
	
	file=open("testScript.js","r")
	# print stripQuotes("this is a 'test' string")
	for line in file:
		line=stripComments(line)
		words=findVars(line)
		#check to see if the list of vars is empty
		if words:
			for var in words:
				if var in reserveWords:
					continue
				if var not in varmap:
					#create a new randon var. if it has been used before create a new random one untill we dont get a dup.
					newRandVar=createRandomVar()
					while newRandVar in newVars:
						newRandVar=createRandomVar()

					varmap[var]=newRandVar
					newVars.append(newRandVar)
				#replace all the old vars on the current line with the new ones
				line=line.replace(var, varmap[var])
		newScript.append(line)
	

		


	file.close()
	outputfile=open("newScript.js", "w+")
	for line in newScript:
		outputfile.write(line)
	outputfile.close

			




