
//// arrays
/// in c# we have two types of Arrys 
/// single dimension and multi dimension
/// sigle dimension is Jagged   var numbers = new int[5];
/// multi dimension is rectangular  var numbers = new int [5] {1, 2, 3, 4, 5};

var matrix = new int[3, 5];
var matrix = new int[3, 5]
{
    {1, 2, 3, 4, 5, },
    {6, 7, 8 ,9, 10 },
    {11, 12, 13, 14, 15 }
};

// if you want to acsses an element its var element = matrix[0, -];

// if you want to declar 3d array car colors = new int [3, 5, 4];
//jagged array
// var array = new int [3] [];
// array [0] = new int [4];
// array [1] = new int [5];
// array [2] = new int [3];
// array [0] [0] =1; to accses an element 

// array types: clear (), copy(), indexOf() , reverse() and sort()
///////////
///


namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new int[] { 3, 7, 9, 2, 14, 6 };

            // length
            Console.WriteLine("Length: " + numbers.Length);

            // IndexOf 
            var index = Array.IndexOf(numbers, 9);
            Console.WriteLine("index of 9:" + index);

            // clear()
            Array.Clear(numbers, 0, 2);
            Console.WriteLine("Effect of Clear()");
            foreach (var n in numbers)
                Console.WriteLine(n);
            //copy 
            int[] another = new int[3];
            Array.Copy(numbers, another, 3);
            Console.WriteLine("Effect of Copy()");
            foreach (var n in another)
                Console.WriteLine(n);

            // sort 
            Array.Sort(numbers);
            Console.WriteLine("Effect of Sort()");
            foreach (var n in numbers)
                Console.WriteLine(n);

            // reverse()
            Array.Sort(numbers);
            Console.WriteLine("Effect of Reverse()");
            foreach (var n in numbers)
                Console.WriteLine(n);

        }
    }
}

//////////////////////////

/////lists

// to crate list
// var numbers = new List<int>();
//useful methods are usefull in class 
// Add() to add an object to the list
// , AddRange() to add list of onjects
// , Remove() to remove one object from the list
// , RemoveAt() to remove object and the given index,
// indexOf() which returns the index of the given object ,
// Contains()tell us if the list contains to givan object or not
// and count which return the number of object in the list 

namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new List<int>() { 1, 2, 3, 4 };
            numbers.Add(1);
            numbers.AddRange(new int[3] { 5, 6, 7 });

            foreach (var number in numbers)
                Console.WriteLine("Index of 1: " + numbers.IndexOf(1));
            //Console.WriteLine("Last Index of 1: " + numbers.Last IndexOf(1));
            //Console.WriteLine(number);

            Console.WriteLine("Count:" + numbers.Count);


            foreach (var number in numbers)
            {
                if (number == 1)
                    numbers.Remove(1);

            }
            foreach (var number in numbers)
                Console.WriteLine(number);
            /////////////////////
            ///
            for (var i = 0; i < numbers.Count;)
            {
                if (numbers[i] == 1)
                    numbers.Remove(1);

            }
            foreach (var number in numbers)
                Console.WriteLine(number);

            numbers.Clear();
            Console.WriteLine("Count:" + numbers.Count);

        }
    }
}

public class Lists
{
    /// <summary>
    /// Write a program and continuously ask the user to enter different names, until the user presses Enter 
    /// (without supplying a name). Depending on the number of names provided, display a message based on the above pattern.
    /// </summary>
    public void Exercise1()
    {
        var names = new List<string>();

        while (true)
        {
            Console.Write("Type a name (or hit ENTER to quit): ");

            var input = Console.ReadLine();
            if (String.IsNullOrWhiteSpace(input))
                break;
            names.Add(input);
        }

        if (names.Count > 2)
            Console.WriteLine("{0}, {1} and {2} others like your post", names[0], names[1], names.Count - 2);
        else if (names.Count == 2)
            Console.WriteLine("{0} and {1} like your post", names[0], names[1]);
        else if (names.Count == 1)
            Console.WriteLine("{0} likes your post.", names[0]);
        else
            Console.WriteLine();
    }

    /// <summary>
    /// Ask the user to enter their name. Use an array to reverse the name and then store the result in a new string. 
    /// Display the reversed name on the console.
    /// </summary>
    public void Exercise2()
    {
        Console.Write("What's your name? ");
        var name = Console.ReadLine();

        var array = new char[name.Length];
        for (var i = name.Length; i > 0; i--)
            array[name.Length - i] = name[i - 1];

        var reversed = new string(array);
        Console.WriteLine("Reversed name: " + reversed);
    }

    /// <summary>
    /// Write a program and ask the user to enter 5 numbers. If a number has been previously entered, display 
    /// an error message and ask the user to re-try. Once the user successfully enters 5 unique numbers, sort them 
    /// and display the result on the console.
    /// </summary>
    public void Exercise3()
    {
        var numbers = new List<int>();

        while (numbers.Count < 5)
        {
            Console.Write("Enter a number: ");
            var number = Convert.ToInt32(Console.ReadLine());
            if (numbers.Contains(number))
            {
                Console.WriteLine("You've previously entered " + number);
                continue;
            }

            numbers.Add(number);
        }

        numbers.Sort();

        foreach (var number in numbers)
            Console.WriteLine(number);
    }

    /// <summary>
    /// Write a program and ask the user to continuously enter a number or type "Quit" to exit. The list of numbers may 
    /// include duplicates. Display the unique numbers that the user has entered.
    /// </summary>
    public void Exercise4()
    {
        var numbers = new List<int>();

        while (true)
        {
            Console.Write("Enter a number (or 'Quit' to exit): ");
            var input = Console.ReadLine();

            if (input.ToLower() == "quit")
                break;

            numbers.Add(Convert.ToInt32(input));
        }

        var uniques = new List<int>();
        foreach (var number in numbers)
        {
            if (!uniques.Contains(number))
                uniques.Add(number);
        }

        Console.WriteLine("Unique numbers:");
        foreach (var number in uniques)
            Console.WriteLine(number);
    }


    /// <summary>
    /// Write a program and ask the user to supply a list of comma separated numbers (e.g 5, 1, 9, 2, 10). If the list is 
    /// empty or includes less than 5 numbers, display "Invalid List" and ask the user to re-try; otherwise, display 
    /// the 3 smallest numbers in the list.
    /// 
    /// </summary>
    public void Exercise5()
    {
        string[] elements;
        while (true)
        {
            Console.Write("Enter a list of comma-separated numbers: ");
            var input = Console.ReadLine();

            if (!String.IsNullOrWhiteSpace(input))
            {
                elements = input.Split(',');
                if (elements.Length >= 5)
                    break;
            }

            Console.WriteLine("Invalid List");
        }

        var numbers = new List<int>();
        foreach (var number in elements)
            numbers.Add(Convert.ToInt32(number));

        var smallests = new List<int>();
        while (smallests.Count < 3)
        {
            // Assume the first number is the smallest
            var min = numbers[0];
            foreach (var number in numbers)
            {
                if (number < min)
                    min = number;
            }
            smallests.Add(min);

            numbers.Remove(min);
        }

        Console.WriteLine("The 3 smallest numbers are: ");
        foreach (var number in smallests)
            Console.WriteLine(number);
    }
}

