
//this is a test function
function thisIsAFunction(inputVar){
	console.log('this is a test');
	console.log(inputVar);
	//add 3
	inputVar+=3;
	console.log(inputVar);

}

function testBool(anotherInput){
	if (anotherInput<4){ //see if the input is less than 4
		return true ;
	}
	//else is not necissory here just want to add more reserve words
	else{
		return false;
	}
}

//call a function
thisIsAFunction(3);
//simple for loop
for (var forLoopVar=0; forLoopVar<5; forLoopVar++){
	console.log(forLoopVar)
}
var hereIsAThing =0;
while (testBool(hereIsAThing)){
	console.log("all is good");
	hereIsAThing+=1;
}
var finished="Done!";
console.log(finished);