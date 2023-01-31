{
    //ToLower(),  "hellow world" , ToUpper HELLOW WORLD
    // Trim(), Subtring(startIndex), Substring(StartIndex, length)
    // Replace()'a', 'r'), Replace ("abd", "mohamed")
    // String.IsNullorEmpty(str)..... String.IsnullOrwhiteSpace(str)
    // str.Split('')
    // to converting strings to numbers 
    // sting s = "1234";  int i = int.Parse(s);  int j = Convert.ToInt32(s)
    //converting numbers to strings
    //string s = i.toString(" ");, i.toString("c)";, i.toString("c0")
    ///////////
    var fullName = "Ghostsy RealGhost ";
    Console.WriteLine("Trim '{0}'", fullName.Trim());
    Console.WriteLine("ToLower '0'", fullName.Trim().ToLower());
    Console.WriteLine("ToUpper '0'", fullName.Trim().ToUpper());

    var index = fullName.IndexOf(' ');
    var firstName = fullName.Substring(0, index);
    var lastName = fullName.Substring(index + 1);
    Console.WriteLine("firstName: " + firstName);
    Console.WriteLine("lastName: " + lastName);
    var names = fullName.Split(' ');
    Console.WriteLine("firstName: " + names[0]);
    Console.WriteLine("lastName: " + names[1]);
    Console.WriteLine(fullName.Replace("Ghostsy", "Ghostsy123"));
    //fullName.Replace('o ', '0');
    //fullName.Replace(' ', '');
    if (String.IsNullOrWhiteSpace(" "))
        Console.WriteLine("invalid");
    var str = "24";
    var age = Convert.ToByte(str);
    Console.WriteLine(age);
    float price = 29.95f;
    Console.WriteLine(price.ToString("C"));
    Console.WriteLine(price.ToString("C0"));


}

////////////////////////////////////////////////////////////////////

static string SummerizeText(string sentence, int maxLength = 20)
{
    //const int maxLength = 20;

    if (sentence.Length > maxLength)
    {
        return sentence;
    }

    //Console.WriteLine(sentence);

    //else
    //{
    //sentence.Substring(0, maxLength);
    var words = sentence.Split(' ');
    var totalCharacters = 0;
    var summaryWords = new List<string>();

    foreach (var word in words)
    {
        summaryWords.Add(word);

        totalCharacters += word.Length + 1;
        if (totalCharacters > maxLength)
            break;
    }

    //var summary = String.Join(" ", summaryWords) + "...";
    //Console.WriteLine(summary);
    return String.Join(" ", summaryWords) + "...";
    //}
}

//string builder
{
    var builder = StringBuilder("Hello wroldd")
        .Append('-', 10)
        .AppendLine()
        .Append("Header")
        .AppendLine()
        //.Append('_','10')
        .Replace('_', '+')
        .Remove(0, 10)
        .Insert(0, new string('_', 10));
    Console.WriteLine(builer);

    Console.WriteLine("First Char: " + builder[0]);

}

/////////////huiswerk 
{
    /// <summary>
    /// Write a program and ask the user to enter a few numbers separated by a hyphen. Work out 
    /// if the numbers are consecutive. For example, if the input is "5-6-7-8-9" or "20-19-18-17-16", 
    /// display a message: "Consecutive"; otherwise, display "Not Consecutive".
    /// </summary>
    //public void Exercise1()
    {
        Console.Write("Enter a few numbers (eg 1-2-3-4): ");
        var input = Console.ReadLine();

        var numbers = new List<int>();
        foreach (var number in input.Split('-'))
            numbers.Add(Convert.ToInt32(number));

        numbers.Sort();

        var isConsecutive = true;
        for (var i = 1; i < numbers.Count; i++)
        {
            if (numbers[i] != numbers[i - 1] + 1)
            {
                isConsecutive = false;
                break;
            }
        }

        var message = isConsecutive ? "Consecutive" : "Not Consecutive";
        Console.WriteLine(message);
    }

    /// <summary>
    /// Write a program and ask the user to enter a few numbers separated by a hyphen. If the user simply 
    /// presses Enter without supplying an input, exit immediately; otherwise, check to see if there are 
    /// any duplicates. If so, display "Duplicate" on the console.
    /// </summary>
    //public void Exercise2()
    {
        Console.Write("Enter a few numbers (eg 1-2-3-4): ");
        var input = Console.ReadLine();

        if (String.IsNullOrWhiteSpace(input))
            return;

        var numbers = new List<int>();
        foreach (var number in input.Split('-'))
            numbers.Add(Convert.ToInt32(number));

        var uniques = new List<int>();
        var includesDuplicates = false;
        foreach (var number in numbers)
        {
            if (!uniques.Contains(number))
                uniques.Add(number);
            else
            {
                includesDuplicates = true;
                break;
            }
        }

        if (includesDuplicates)
            Console.WriteLine("Duplicate");
    }

    /// <summary>
    /// Write a program and ask the user to enter a time value in the 24-hour time format (e.g. 19:00).
    /// A valid time should be between 00:00 and 23:59. If the time is valid, display "Ok"; otherwise, 
    /// display "Invalid Time". If the user doesn't provide any values, consider it as invalid time. 
    /// </summary>
    //public void Exercise3()
    {
        Console.Write("Enter time: ");
        var input = Console.ReadLine();

        if (String.IsNullOrWhiteSpace(input))
        {
            Console.WriteLine("Invalid Time");
            return;
        }

        var components = input.Split(':');
        if (components.Length != 2)
        {
            Console.WriteLine("Invalid Time");
            return;
        }

        try
        {
            var hour = Convert.ToInt32(components[0]);
            var minute = Convert.ToInt32(components[1]);

            if (hour >= 0 && hour <= 23 && minute >= 0 && minute <= 59)
                Console.WriteLine("Ok");
            else
                Console.WriteLine("Invalid Time");
        }
        catch (Exception)
        {
            Console.WriteLine("Invalid Time");
        }
    }

    /// <summary>
    /// Write a program and ask the user to enter a few words separated by a space. Use the words to 
    /// create a variable name with PascalCase convention. For example, if the user types: 
    /// "number of students", display "NumberOfStudents". Make sure the program is not dependent on 
    /// the casing of the input. So if the input is "NUMBER OF STUDENTS", it should still display 
    /// "NumberOfStudents". If the user doesn't supply any words, display "Error".
    /// </summary>
    //public void Exercise4()
    {
        Console.Write("Enter a few words: ");
        var input = Console.ReadLine();

        if (String.IsNullOrWhiteSpace(input))
        {
            Console.WriteLine("Error");
            return;
        }

        var variableName = "";
        foreach (var word in input.Split(' '))
        {
            var wordWithPascalCase = char.ToUpper(word[0]) + word.ToLower().Substring(1);
            variableName += wordWithPascalCase;
        }

        Console.WriteLine(variableName);
    }


    /// <summary>
    /// Write a program and ask the user to enter an English word. Count the number of vowels 
    /// (a, e, o, u, i) in the word. So, if the user enters "inadequate", the program should display 
    /// 6 on the console. Make sure the program calculates the number of vowels irrespective of the 
    /// casing of the word (eg "Inadequate", "inadequate" and "INADEQUATE" all include 6 vowels).
    /// </summary>
   // public void Exercise5()
    {
        Console.Write("Enter a word: ");
        // Note the ToLower() here. This is used to count for both A and a. 
        var input = Console.ReadLine().ToLower();

        var vowels = new List<char>(new char[] { 'a', 'e', 'o', 'u', 'i' });
        var vowelsCount = 0;
        foreach (var character in input)
        {
            if (vowels.Contains(character))
                vowelsCount++;
        }

        Console.WriteLine(vowelsCount);
    }
}
//}
/////////////////////////////////////
// Procedural Programming