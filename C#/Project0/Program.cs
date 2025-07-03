///
/// <summary>
/// Project 0: Command Line Program
/// This is a program to read and output command line arguments
/// </summary>
/// 
/// M. Bigler
/// 07/01/2025
///  

using System;

class Program
{
	static void Main(string[] args)
	{
		if (args.Length < 2) // check number of args
		{
			Console.WriteLine("Please enter at least 2 arguments\n");
			return;
		}

		// assign vars
		string arg1 = args[0];
		string arg2 = args[1];

		// output to console
		Console.WriteLine("Hello your entered args are: \n\tARG 1:{0}\n\tARG 2:{1}", arg1, arg2);

		// wait for input to exit
		Console.ReadKey();
	}
}