import re
import random
#i need to remove the comments. everything will be ignored after "//" for now i will skip block comments to save time
def stripComments(line):
	for i in range(len(line)-1):
		if line[i]=="/" and line[i+1]=="/":
			return line[:i]
	return line

def createRandomVar():
	letters="abcdefghijklmnopqrstufwxyz1234567890"
	result=""
	#create variables with length between 3 and 10
	for i in range(random.randint(3, 10)):
		result+=random.choice(letters)
	return result


if __name__=="__main__":
	#ignore these words. these are important
	reserveWords=['abstract', 'else', 'instanceof', 'super', 'boolean', 
		'enum', 'int', 'switch', 'break', 'export', 'interface', 'synchronized', 
		'byte', 'extends', 'let', 'this', 'case', 'false', 'long', 'throw', 'catch', 
		'final', 'native', 'throws', 'char', 'finally', 'new', 'transient', 'class', 
		'float', 'null', 'true', 'const', 'for', 'package', 'try', 'continue', 'function', 
		'private', 'typeof', 'debugger', 'goto', 'protected', 'var', 'default', 'if', 
		'public', 'void', 'delete', 'implements', 'return', 'volatile', 'do', 'import', 
		'short', 'while', 'double', 'in', 'static', 'with']
	varmap={}
	newVars=[]
	newScript=[]
	file=open("testScript.js","r")
	print createRandomVar()
	# for line in file:
	# 	print stripComments(line)


