# CodeObfuscation

---
## Brain storming
 12:00 pm
The first think I am going to do is create a test file in js so i can actually ru this thing
then read in the file and look for non reserve words that are not in quotes. so all the variables and function names. 
create a function that will create random strings then replace all variables and function names with the corrisponding random word

I think ill do this in python just to make it a little easier for reading the file and whatnot.

---

12:35	i went online to get a list of js reserve words to ignore. i need to make sure i dont replace these.
		added re as import for python. simple libary to use regex
		added random to create random variable names

---
13:40	all variables and and function names seem to be replaces correctly and the new script runs correctly
		all comments have been removed. 
		I'm going to try to concat some of the lines so it looks enem more confusing. cant be too confused.


---
14:20	ok i think im done with this for now. it should be working at least with teh short script i gave it. 

---
## instructions

just call the python script with a single argument, the name of the js script to be changed. 
eg `python obfuscator.py testSctipt.js`
it will create a new file called "newScript.js". i have provided a small test script that it works with. it will create a bunch of random variables to replace the old variable names and will concatinate lines together to be really confusing. i dont really want to read the new script. its a pain in my ass

---
## future
(maybe)
ont thing i could try to do but seems a bit too dificult right now would be to look at some objects and see if i can change some of the string names in side it 
for example `{"start":2,"end":7}`
in this JSON i could change "start" and "end" to be anything else. but it is kinda hard to tell when someting is a literal or just a JSON key. i think im going to stop here.
