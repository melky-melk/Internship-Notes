using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorldBetter
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Convert.ToInt32("24");
            Console.WriteLine("Hello, World");

            Console.ReadLine();

            double num1 = Convert.ToDouble(Console.ReadLine());

            string colour, pluralNoun, celebrity;

            Console.Write("Enter a colour");
            colour = Console.ReadLine();

            Console.Write("Enter a plural noun");
            pluralNoun = Console.ReadLine();

            Console.Write("Enter a celebrity");
            celebrity = Console.ReadLine();

            string[] friends = new string[5];

            friends[0] = "Jim";
            friends[1] = "Kelly"

            SayHello();

            
        }

        static void SayHello()
        {
            Console.WriteLine("Hello");
        }

        static int GetMax(int num1, int num2)
        {
            return num1 > num2 ? num1 : num2 ;
        }

        static string GetDay(int dayNum)
        {
            string dayName = "No day";

            switch (dayNum)
            {
                case 0:
                    dayName = "Sunday";
                    break;
                case 1:
                    dayName = "Monday";
                    break;
            }

            return dayName;
        }
    }
}
