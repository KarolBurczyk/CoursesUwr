using System;

namespace TestProgram;

internal class Program
{
	private static void Main()
	{
		TestClass testClass = new TestClass();
		testClass.TestEvent += delegate(string msg)
		{
			Console.WriteLine(msg);
		};
		testClass.TriggerEvent();
		testClass.Loop();
		testClass.Condition(-5);
		testClass.Switch(1);
		Console.WriteLine(testClass[2]);
	}
}
