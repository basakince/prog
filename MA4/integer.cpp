#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
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
	if (val <= 1)
        return val;
    return fib(val-1) + fib(val-2);
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