#include <iostream>

template<typename T>
void allocMemory(T ** y, size_t n){

	/*
		Arguments are passed by assignment.

		Recall how you can change arrays in function:
		When you have func(int * arr) and you call it as func(origArr)
		then it executes arr = origArr.
		Hence when you make arr[0] = 0 then its same as changing
		the value in the memory address contained in origArr

		Now you want to allocate in memory.
		You kind of want to change arr[0] but this arr[0]
		will contain the address of allocated memory.
		This makes arr a pointer to a pointer.
		Thus *y or y[0] is of the type that contains address.


	*/

	*y		= (T *)malloc(sizeof(T) * n); //y[0] = ... also works.

	return;

}
