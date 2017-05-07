import re
import random
import sys
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
					#add everything from the previous quost to the current quote
					result+=line[previous:i]
					#make the previous match location equal to the end of the current match
					previous=j+1
					
					i=j+1
					#stop looking
					break
				else: j+=1


		else: i+=1
	
	result+=line[previous:]
	return result




def createRandomVar():
	letters="abcdefghijklmnopqrstufwxyz"
	#start with only letters
	result=random.choice(letters)
	letters+="1234567890"
	#create variables with length between 3 and 10
	for i in range(random.randint(3, 10)):
		result+=random.choice(letters)
	if result in newVars:
		#recursivly call if the created variable has been made before
		#this has not really been tested be cause the odds of creating a dup name is very low
		return createRandomVar()
	return result

#use regex to find all the variable names 
def findVars(line):
	noQuotes=stripQuotes(line)
	pattern=re.compile("[a-zA-Z_$][a-zA-Z_$0-9]*")
	result=pattern.findall(noQuotes)
	return result



#these are globals
varmap={}
newVars=[]
newLines=[]
#ignore these words. these are important
reserveWords=['abstract', 'else', 'instanceof', 'super', 'boolean', 
		'enum', 'int', 'switch', 'break', 'export', 'interface', 'synchronized', 
		'byte', 'extends', 'let', 'this', 'case', 'false', 'long', 'throw', 'catch', 
		'final', 'native', 'throws', 'char', 'finally', 'new', 'transient', 'class', 
		'float', 'null', 'true', 'const', 'for', 'package', 'try', 'continue', 'function', 
		'private', 'typeof', 'debugger', 'goto', 'protected', 'var', 'default', 'if', 
		'public', 'void', 'delete', 'implements', 'return', 'volatile', 'do', 'import', 
		'short', 'while', 'double', 'in', 'static', 'with', 'console', 'log']


if __name__=="__main__":
	#look for the file passed in form command line
	filename=sys.argv[1]
	file=open(filename,"r")
	# print stripQuotes("this is a 'test' string")
	for line in file:
		line=stripComments(line)
		words=findVars(line)
		#check to see if the list of vars is empty
		if words:
			#go through all the variables in the list
			for var in words:
				if var in reserveWords:
					#ignore the word if it is in the list of reserved words
					continue
				if var not in varmap:
					#create a new randon var. 
					newRandVar=createRandomVar()
					# add new var to varmap and list of other new vars
					varmap[var]=newRandVar
					newVars.append(newRandVar)
				#replace all the old vars on the current line with the new ones
				line=line.replace(var, varmap[var])
		#add the changed line to the list of changed lines
		newLines.append(line)
	file.close()
	lineIndex=0
	newScript=[]
	# go through the list of new lines and concatinate them if the new lines are less than 50 characters
	while lineIndex<len(newLines):
		newScriptLine=""
		while len(newScriptLine)<50:

			try:
				#get new line if i can and remove all leading and trailing whitespace
				currentLine=newLines[lineIndex].strip()
			except:
				# if the curent index is out of bounds just end here. this should oly iccur at the end of the script
				break
			if currentLine:
				lastChar=currentLine[len(currentLine)-1]
				#test the last character in the changed line. if it already has a ";" 
				#or is a bracket i dont need to add a ";"
				if lastChar!=";" and not(lastChar=="}" or lastChar=="{"):
					currentLine+=";"
				#add the current short changed line to a longer line that will be added to the new script
				newScriptLine+=currentLine
			lineIndex+=1
		newScript.append(newScriptLine)


	#write new file
	outputfile=open("newScript.js", "w+")
	for line in newScript:
		outputfile.write(line)
		outputfile.write("\n")
	outputfile.close

			




