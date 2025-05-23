using System;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

public interface IShape
{
    double Area();
}

public class Square : IShape
{
    private double _side;
    public Square(double side) => _side = side;
    public double Area() => _side * _side;
}

public class Rectangle : IShape
{
    private double _width, _height;
    public Rectangle(double width, double height)
    {
        _width = width;
        _height = height;
    }
    public double Area() => _width * _height;
}

public interface IShapeFactoryWorker
{
    string ShapeName { get; }
    IShape Create(params object[] parameters);
}

public class SquareFactoryWorker : IShapeFactoryWorker
{
    public string ShapeName => "Square";
    public IShape Create(params object[] parameters)
    {
        double side = Convert.ToDouble(parameters[0]);
        return new Square(side);
    }
}

public class RectangleFactoryWorker : IShapeFactoryWorker
{
    public string ShapeName => "Rectangle";
    public IShape Create(params object[] parameters)
    {
        double width = Convert.ToDouble(parameters[0]);
        double height = Convert.ToDouble(parameters[1]);
        return new Rectangle(width, height);
    }
}

public class ShapeFactory
{
    private readonly Dictionary<string, IShapeFactoryWorker> _workers = new();

    public void RegisterWorker(IShapeFactoryWorker worker)
    {
        _workers[worker.ShapeName] = worker;
    }

    public IShape CreateShape(string shapeName, params object[] parameters)
    {
        if (_workers.TryGetValue(shapeName, out var worker))
        {
            return worker.Create(parameters);
        }

        throw new InvalidOperationException($"Shape '{shapeName}' is not registered.");
    }
}

public class Tests
{
    public static void CanCreateSquare()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new SquareFactoryWorker());

        var shape = factory.CreateShape("Square", 4);
        Console.WriteLine($"CanCreateSquare: Area of Square with side 4 = {shape.Area()}");
        try
        {
            Assert.AreEqual(16, shape.Area(), 0.001);
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void CanCreateRectangle()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new RectangleFactoryWorker());

        var shape = factory.CreateShape("Rectangle", 3, 5);
        Console.WriteLine($"CanCreateRectangle: Area of Rectangle with width 3 and height 5 = {shape.Area()}");
        try
        {
            Assert.AreEqual(15, shape.Area(), 0.001);
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void ThrowsExceptionWhenShapeNotRegistered()
    {
        var factory = new ShapeFactory();

        Console.WriteLine("ThrowsExceptionWhenShapeNotRegistered: Trying to create an unregistered shape (Triangle).");
        try
        {
            Assert.ThrowsException<InvalidOperationException>(() =>
            {
                factory.CreateShape("Triangle", 1, 1, 1);
            });
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void CanRegisterMultipleWorkers()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new SquareFactoryWorker());
        factory.RegisterWorker(new RectangleFactoryWorker());

        var square = factory.CreateShape("Square", 2);
        var rect = factory.CreateShape("Rectangle", 2, 4);

        Console.WriteLine($"CanRegisterMultipleWorkers: Area of Square with side 2 = {square.Area()}");
        Console.WriteLine($"CanRegisterMultipleWorkers: Area of Rectangle with width 2 and height 4 = {rect.Area()}");
        
        try
        {
            Assert.AreEqual(4, square.Area(), 0.001);
            Assert.AreEqual(8, rect.Area(), 0.001);
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void CanOverrideExistingWorker()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new RectangleFactoryWorker());

        factory.RegisterWorker(new RectangleFactoryWorker());

        var shape = factory.CreateShape("Rectangle", 2, 3);
        Console.WriteLine($"CanOverrideExistingWorker: Area of Rectangle with width 2 and height 3 = {shape.Area()}");
        
        try
        {
            Assert.AreEqual(6, shape.Area(), 0.001);
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}

class Program
{
    static void Main()
    {
        Tests.CanCreateSquare();
        Tests.CanCreateRectangle();
        Tests.ThrowsExceptionWhenShapeNotRegistered();
        Tests.CanRegisterMultipleWorkers();
        Tests.CanOverrideExistingWorker();
    }
}
