//Conditional Statement
/// if / else statements
/// Switch / case statements 
/// conditional operator: a ? b : c

//if (condition)
// somestetment
//else if (anothercondition)
// anotherstetment
//else 
// yet otherstetment

//switch / case
// case role.admin
// ....
/// break;

//case Role.moderator:
//...
//break

// default:
//...
// break;

class Program
{
    static void Main(string[] args)
    {
        int hour = 10;

        if (hour 6 >= && < 12) 
        {
            Console.WriteLine("its morning.");
        }

        else if (hour >= 12 && hour < 18)
        {
            Console.WriteLine("its Afternoon");
        }

        else if (hour >= 18 && < 24)
        {
            Console.WriteLine("its evening");

        }

        else if (hour >= 24 && < 6)
        {
            Console.WriteLine("its night");

        }

        else
        {
            Console.WriteLine("I dont know");
        }
    }
}


class Program
{
    static void Main(string[] args)
    {
        bool isGoldCustomer = true;

        float price;
        if (isGoldCustomer)
            price = 20.99f;
        else
            price = 29.33f;

        float price = (isGoldCustomer) ? 19.95f : 20.99f;
        Console.WriteLine(price);
    }
}


namespace ConsoleApp12
{
    public enum Season
    {
        Spring,
        Summer,
        Autumn,
        Winter,
    }
    class Program
    {
        static void Main(string[] args)
        {
            var season = Season.Autumn;

            switch (season)
            {
                case season.Autumn:
                    Console.WriteLine("its autumn and beautiful season.");
                    break;

                case season.Summer:
                    Console.WriteLine("its perfect to go to beach.");
                    break;

                default;
                    Console.WriteLine(" i dont know this season");
                    break;


            }



        }
    }
}

public class Conditionals
{
    /// <summary>
    /// Write a program and ask the user to enter a number. The number should be between 1 to 10. If the user enters 
    /// a valid number, display "Valid" on the console. Otherwise, display "Invalid". (This logic is used a lot in 
    /// applications where values entered into input boxes need to be validated.)
    /// </summary>
    public void Exercise1()
    {
        Console.Write("Enter a number between 1 to 10: ");
        var input = Console.ReadLine();
        var number = Convert.ToInt32(input);
        if (number >= 1 && number <= 10)
            Console.WriteLine("Valid");
        else
            Console.WriteLine("Invalid");
    }

    /// <summary>
    /// Write a program which takes two numbers from the console and displays the maximum of the two.
    /// </summary>
    public void Exercise2()
    {
        Console.Write("Enter a number: ");
        var number1 = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter another number: ");
        var number2 = Convert.ToInt32(Console.ReadLine());

        var max = (number1 > number2) ? number1 : number2;
        Console.WriteLine("Max is " + max);
    }

    /// <summary>
    /// Write a program and ask the user to enter the width and height of an image. Then tell if the image 
    /// is landscape or portrait.
    /// </summary>
    public void Exercise3()
    {
        Console.Write("Image width: ");
        var width = Convert.ToInt32(Console.ReadLine());

        Console.Write("Image height: ");
        var height = Convert.ToInt32(Console.ReadLine());

        var orientation = width > height ? ImageOrientation.Landscape : ImageOrientation.Portrait;
        Console.WriteLine("Image orientation is " + orientation);
    }

    public enum ImageOrientation
    {
        Landscape,
        Portrait
    }

    /// <summary>
    /// Your job is to write a program for a speed camera. For simplicity, ignore the details such as camera, sensors, 
    /// etc and focus purely on the logic. Write a program that asks the user to enter the speed limit. Once set, 
    /// the program asks for the speed of a car. If the user enters a value less than the speed limit, program should 
    /// display Ok on the console. If the value is above the speed limit, the program should calculate the number of 
    /// demerit points. For every 5km/hr above the speed limit, 1 demerit points should be incurred and displayed on 
    /// the console. If the number of demerit points is above 12, the program should display License Suspended.
    /// </summary>
    public void Exercise4()
    {
        Console.Write("What is the speed limit? ");
        var speedLimit = Convert.ToInt32(Console.ReadLine());

        Console.Write("What is the speed of this car? ");
        var carSpeed = Convert.ToInt32(Console.ReadLine());

        if (carSpeed < speedLimit)
            Console.WriteLine("Ok");
        else
        {
            const int kmPerDemeritPoint = 5;
            var demeritPoints = (carSpeed - speedLimit) / kmPerDemeritPoint;
            if (demeritPoints > 12)
                Console.WriteLine("License Suspended");
            else
                Console.WriteLine("Demerit points: " + demeritPoints);
        }
    }
}

////////////////////////////////////////////

/////////////////Forloops


// Ietration Statement
// For loops 
// Foreach loops
// While loops
// Do-While

for (var i = 0; i < 10; ++)
{

}


foreach (var number in object)
{

}

while (i < 10)
{

    i++;
}

do
{

    i++;
    while (i < 10) ;
}

// break; jump out of the loop 
// continue; jum[ to the mext iteration

//examples

namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            for (var i = 1; i <= 00; i++)
            {
                if (i % 2 == 0)
                {
                    Console.WriteLine(i);
                }
            }

            for (var i = 10; i >= 1; i--)
            {
                Console.WriteLine(i);
            }

            for (var i = 10; i >= 1; i * *)
            {
                Console.WriteLine(i);
            }

            for (var i = 10; i >= 1; i//)
            {
                Console.WriteLine(i);
            }
            //var name = "abd";
            //for (var i = 0; i < name.Length; i++)
            //{
            //    Console.WriteLine(name[i]); 
            //}

            //foreach (var character in name)
            //{
            //    Console.WriteLine(character);
            //}

            var numbers = new int[] { 1, 2, 3, 4 };
            foreach (var number in numbers)
            {
                Console.WriteLine(number);
            }


            //for (var i = 1; i <= 10; i++)
            //{
            //    if (i% 2 == 0)
            //        Console.WriteLine(i);
            //}

            var i = 0;
            while (i < 10)
            {
                if (i % 2 == 0)
                    Console.WriteLine(i);
                i++;
            }
            //while (true)
            //{
            //    Console.Write("type your name");
            //    var input = Console.ReadLine();

            //    if (string.IsNullOrWhiteSpace(input))
            //        break;

            //    Console.WriteLine("@Echo:"input);}



            while (true)
            {
                Console.Write("type your name");
                var input = Console.ReadLine();

                if (!string.IsNullOrWhiteSpace(input))
                {
                    Console.WriteLine("@Echo:"input);
                }
                continue;

            }
            break;



        }
    }
}

////////////////////////////////////////
/// random classes
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            //var random = new Random();
            //for (var i = 0; i < 10; i++)
            //    Console.WriteLine(random.Next());


            //var random = new Random();
            //for (var i = 0; i < 10; i++)
            //    Console.WriteLine(random.Next(1, 10));


            //var random = new Random();
            //for (var i = 0; i < 10; i++)
            //    Console.Write((char)random.Next(97, 122));
            //Console.WriteLine();

            var random = new Random();

            const int passwordLength = 32;
            char[] buffer = new char[passwordLength];
            for (var i = 0; i < passwordLength; i++)
                buffer[i] = (char)'a'random.Next(0, 26));

            var password = "";
            var Password = new string(buffer);
            Console.WriteLine();

            //Console.WriteLine((int)'a' );
        }


    }
}


public class Loops
{
    /// <summary>
    /// Write a program to count how many numbers between 1 and 100 are divisible by 3 with no remainder. 
    /// Display the result on the console.
    /// </summary>
    public void Exercise1()
    {
        var count = 0;
        for (var i = 1; i <= 100; i++)
        {
            if (i % 3 == 0)
                count++;
        }
        Console.WriteLine("There are {0} numbers divisible by 3 between 1 and 100.", count);
    }

    /// <summary>
    /// Write a program and continuously ask the user to enter a number. The loop terminates when the user 
    /// enters “ok". Calculate the sum of all the previously entered numbers and display it on the console.
    /// </summary>
    public void Exercise2()
    {
        var sum = 0;
        while (true)
        {
            Console.Write("Enter a number (or 'ok' to exit): ");
            var input = Console.ReadLine();

            if (input.ToLower() == "ok")
                break;

            sum += Convert.ToInt32(input);
        }
        Console.WriteLine("Sum of all numbers is: " + sum);
    }

    /// <summary>
    /// Write a program which takes a single argument from the console, computes the factorial and prints the 
    /// value on the console. For example, if the user enters 5, the program should calculate 5 x 4 x 3 x 2 x 1 
    /// and display it as 5! = 120.
    /// </summary>
    public void Exercise3()
    {
        Console.Write("Enter a number: ");
        var number = Convert.ToInt32(Console.ReadLine());

        var factorial = 1;
        for (var i = 1; i <= number; i++)
            factorial *= i;

        Console.WriteLine("{0}! = {1}", number, factorial);
    }

    /// <summary>
    /// Write a program that picks a random number between 1 and 10. Give the user 4 chances to guess the number. 
    /// If the user guesses the number, display “You won". Otherwise, display “You lost".
    /// </summary>
    public void Exercise4()
    {
        var number = new Random().Next(1, 10);

        Console.WriteLine("Secret is " + number);
        for (var i = 0; i < 4; i++)
        {
            Console.Write("Guess the secret number: ");
            var guess = Convert.ToInt32(Console.ReadLine());

            if (guess == number)
            {
                Console.WriteLine("You won!");
                return;
            }
        }

        Console.WriteLine("You lost!");
    }

    /// <summary>
    /// Write a program and ask the user to enter a series of numbers separated by comma. Find the maximum of the 
    /// numbers and display it on the result. For example, if the user enters “5, 3, 8, 1, 4", the program should 
    /// display 8 on the console.
    /// </summary>
    public void Exercise5()
    {
        Console.Write("Enter commoa separated numbers: ");
        var input = Console.ReadLine();

        var numbers = input.Split(',');

        // Assume the first number is the max 
        var max = Convert.ToInt32(numbers[0]);

        foreach (var str in numbers)
        {
            var number = Convert.ToInt32(str);
            if (number > max)
                max = number;
        }

        Console.WriteLine("Max is " + max);

    }
}



//////////////////////////////////