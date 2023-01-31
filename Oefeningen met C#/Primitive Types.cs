//Primitive Types 
Console.WriteLine("Hello, World!");

//var number = 2;
//var count = 10;
//var totalPrice = 20.99f;
//var character = 'a';
//var firstName = "AbdulRahman";
// var isWorking = false;

byte number = 2;
int count = 10;
float totalPrice = 20.99f;
char character = 'a';
string firstName = "AbdulRahman";
bool isWorking = false;
Console.WriteLine(count);
Console.WriteLine(totalPrice);
Console.WriteLine(character);
Console.WriteLine(firstName);
Console.WriteLine(isWorking);
Console.WriteLine(number);
////////////////

Console.WriteLine("{0} {1}", byte.MinValue, byte.MinValue);
Console.WriteLine("{0}{1}", float.MinValue, float.Maxvalue);
const float Pi = 3.14f;
//Pi = 1; that is not gonna work coz pi is alread has a value of 3.14
////////////////////////


//byte b = 1;
//int i = b;
//Console.WriteLine(i); that is good

//int i = 1000;
int i = 1;
//byte b = i;
//that is wrong or need to use cast
byte b = (byte)i;
// that is good be careful do not use more than 252,
// number coz you might get data lost if you use int i = 100 it only spicify the cast

//example 1
string number = "1234";
//example2 
var number = "1234";
//int i = (int)number;
int i = Convert.ToInt32(number);
//int i = Convert.ToByte(number); if you do that you will crash the program you can fix that by  with function TRY
// other example is 
string str = "true";
bool b = Convert.ToBoolean(str);// that not gonna work with casting,
Console.WriteLine(b);
// that why we convert it coz its not compatible like that it word
// you can not cast int to int  you need to convert it 
//we can not run the program coz its string the program tells us that so we need to convert it.
//////////////////////////////////////
// operators

//{arithmetic  operators
//+, -, *,/,% ++ a++ = a=a +1, -- a-- = a=a-1,
//you can you them as postfix increment int a = 1     = 2
//                                      int b = a++;  = 1
//                                      example 2 
//                                      int a = 1     = 2
//                                      int b = ++a;  = 2 }
//{Comparison operators
//== equal, not equal!=, greater than >, greater than or equal >=, less than or equal to <=, les than <}
//{Assignment operators
//= Assignment += Addition assignment, Subtraction assigement, -=, Multiplication assigment *=, Division assignment /=}
//{Logical operators And &&, Or || not!}
//{What are Logical Operations?Logical operations are part of Boolean algebra, which is often taught to students of computer science and electronic engineering at University.
//So, if you’re not familiar with Boolean algebra, here is a brief introduction.In Boolean algebra, the value of variables can only be true or false, also denoted 1 and 0 respectively.
//Unlike elementary algebra, where the main operations are addition, subtraction, etc, the main operations of Boolean algebra are conjunction (AND), disjunction (OR) and negation (NOT).}
//{Bitwise operators and & , or |}
////////////////////////////////////////////////

// single line comment = //
/* 

muilti-line comment

*/

