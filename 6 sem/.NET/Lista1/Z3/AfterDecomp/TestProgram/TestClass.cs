using System;

namespace TestProgram;

public class TestClass
{
	private int _number;

	public int Number
	{
		get
		{
			return _number;
		}
		set
		{
			_number = value;
		}
	}

	public string this[int index] => $"Index {index}";

	public event TestDelegate TestEvent;

	public void TriggerEvent()
	{
		this.TestEvent?.Invoke("Event triggered!");
	}

	public void Loop()
	{
		for (int i = 0; i < 5; i++)
		{
			Console.WriteLine($"Loop iteration: {i}");
		}
	}

	public void Condition(int x)
	{
		if (x > 0)
		{
			Console.WriteLine("Positive");
		}
		else if (x < 0)
		{
			Console.WriteLine("Negative");
		}
		else
		{
			Console.WriteLine("Zero");
		}
	}

	public void Switch(int day)
	{
		switch (day)
		{
		case 1:
			Console.WriteLine("Monday");
			break;
		case 2:
			Console.WriteLine("Tuesday");
			break;
		default:
			Console.WriteLine("Other day");
			break;
		}
	}
}
