// Class = combines related variables (fields) and functions (methods)
// Methorths: for example walk() talk() eat() sleep()
// Fields = Name ; string , Age; bute , Height; float , weight ; byte  
// how to carte calsses or declaring classes

public class Person
{

    public string Name;
    public void Introduce()
    {
        Console.WriteLine("hi, my name is + Name ");

    }
}

/////
public class Calculator
{
    public static int Add(int a, int b)
    {

        return a + b;
        var person = new Person();
        person.Name = "AbdulRahman";
        person.Introduce();
        int result = Calculator.Add(1, 2);
    }
}
/////


namespace ConsoleApp12
{
    public class Person
    {
        public string FirstName;
        public string LastName;

        public void Introduce()
        {
            Console.WriteLine("my name is " + FirstName + " " + LastName);

        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            var AbdulRahman = new Person();
            AbdulRahman.FirstName = "AbdulRahman";
            AbdulRahman.LastName = "Bani Almarjeh";
            AbdulRahman.Introduce();
        }
    }
}



namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            var AbdulRahman = new Person();
            AbdulRahman.FirstName = "AbdulRahman";
            AbdulRahman.LastName = "Bani Almarjeh";
            AbdulRahman.Introduce();

            Calculator calulator = new Calculator();
            var result = calulator.Add(1, 2);
            Console.WriteLine(result);
        }
    }
}

//Structs class
public struct RgbColor
{
    public int red;
    public int green;
    public int blue;
}


// Array: a data structure to store a collection of variables of the same type.
// for example 
// int number 1; int number 2; int number 3;
// you cab use arrays like that int [] numbers =  new int [3] {1, 2, 3,};

namespace ConsoleApp12
{
    class program
    {
        static void Main(String[] args)
        {
            int[] number = new int[3];
            number[0] = 1;

            Console.WriteLine(number[0]);
            Console.WriteLine(number[1]);
            Console.WriteLine(number[2]);

            var flags = new bool[3];
            flags[0] = true;
            Console.WriteLine(0);
            Console.WriteLine(1);
            Console.WriteLine(2);

            var names = new string[3];
            //{ "mmm", "jaaa", "what" }

        }
    }
}


//////////////////////////////////////////////////// 
//Strings 

// string; sequence of characters. e.g. "Hellow World"
// fitstName = "AbdulRahman"
// name = firstName + " " + lastName;
//string format:
// string name = string.Format ("{0} {1}" firstName, lastName);

// using string join
// var numbers = new int [3] {1, 2, 3};
// string list = string.Join(",", numbers);
// string name = "abdul";
// to accses to charcater  char firstChar = name [0];

//escape characters 

// \n ; new line
// \t ; tap
// \\ ;backslash
// \' ;single quotation mark
// \" ; bouble quotation mark
// verbatimg strings = @ ......

class proram
{
    static void Main(string[] args)
    {

        var firstName = "Ghost";
        var lastName = "GG";

        var fullName = firstName + " " + lastName;

        var myFullName = string.Format("My name is{0} {1} ", firstName, lastName);

        var names = new string[3] { "ja", "aaa", "ssss" };
        var formattedNames = string.Join(", ", names);
        Console.WriteLine(formattedNames);

        var text = "hi mmm/n Look at meee\nn:\\sss\aaa\\aaaaa\\cc:\\";
        Console.WriteLine(text);

        var Text = @"hi mmm
Look at meee
n:\sss\aaa\aaaaa\cc:\";
        Console.WriteLine(text);


    }
}
/////////////////////////////
//Enums

public enum ShippingMethod
{
    RegularAirMail = 1,
    RegisteredairMail = 2,
    Express = 3
}




class program
{
    static void Main(string[] args)
    {
        var method = ShippingMethod.Express;
        Console.WriteLine((int)method);

        var methodId = 3;
        Console.WriteLine((ShippingMethod)methodId);

        Console.WriteLine(method.ToString());

        var methodName = "Express";
        //var (ShippingMethod) = Enum.Parse(typeof(ShippingMethod), methodName);
    }
}
/////////////////////////////////////

/// Reference types and balue types

class Program
{
    static void Main(string[] args)
    {
        var a = 10;
        var b = a;
        b++;
        Console.WriteLine(string.Format("a: {0}, b: {1}", a, b));

        var array1 = new int[3] { 1, 2, 3 };
        var array2 = array1;
        array2[0] = 0;
        Console.WriteLine(string.Format("array[0]: {0}, array2[0]: { 1}", array1[0], array2[0]));

    }
}



public class Person
{
    public int Age;
}

class Program
{
    static void Main(string[] args)
    {
        var number = 1;
        Increment(number);
        Console.WriteLine(number);

        var person = new Person() { Age = 20 };
        MakeOld(person);
        Console.WriteLine(person.Age);
    }

    public static void Increment(int number)
    {
        number += 10;
    }

    public static void MakeOld(Person person)
    {
        person.Age += 10;
    }
}
