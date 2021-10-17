#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
		int fibCalc(int);
	private:
		int val;
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}

int Integer::fib(){
	return fibCalc(val);

}

int Integer::fibCalc(int x){
	if (x <= 1)
        return x;
    return fibCalc(x-1) + fibCalc(x-2);
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	int Integer_fib(Integer* integer) {return integer->fib();}
	}