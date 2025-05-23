using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

interface IDataSourceStrategy
{
    void Open();
    object Fetch();
    void Analyze(object data);
    void Close();
}

class DataAccessExecutor
{
    private readonly IDataSourceStrategy _strategy;

    public DataAccessExecutor(IDataSourceStrategy strategy)
    {
        _strategy = strategy;
    }

    public void Run()
    {
        _strategy.Open();
        var rawData = _strategy.Fetch();
        _strategy.Analyze(rawData);
        _strategy.Close();
    }
}

class MockDbStrategy : IDataSourceStrategy
{
    private List<Dictionary<string, object>> _mockTable;

    public void Open()
    {
        Console.WriteLine("Connecting to mock database...");
        _mockTable = new List<Dictionary<string, object>>
        {
            new Dictionary<string, object> { { "Amount", 15 }, { "Label", "ItemA" } },
            new Dictionary<string, object> { { "Amount", 25 }, { "Label", "ItemB" } },
            new Dictionary<string, object> { { "Amount", 40 }, { "Label", "ItemC" } }
        };
    }

    public object Fetch()
    {
        Console.WriteLine("Retrieving data from mock DB...");
        return _mockTable;
    }

    public void Analyze(object data)
    {
        Console.WriteLine("Summing 'Amount' values...");
        var records = data as List<Dictionary<string, object>>;
        int total = records.Sum(row => Convert.ToInt32(row["Amount"]));
        Console.WriteLine($"Total Amount: {total}");
    }

    public void Close()
    {
        Console.WriteLine("Disconnected from mock DB.");
    }
}

class XmlFileStrategy : IDataSourceStrategy
{
    private XDocument _xmlContent;

    public void Open()
    {
        Console.WriteLine("Parsing XML document...");
        string xml = @"
        <dataset>
            <entry label='tiny' />
            <entry label='extremelylonglabelvalue' />
            <entry label='moderateLength' />
        </dataset>";
        _xmlContent = XDocument.Parse(xml);
    }

    public object Fetch()
    {
        Console.WriteLine("Extracting entries from XML...");
        return _xmlContent;
    }

    public void Analyze(object data)
    {
        Console.WriteLine("Finding longest label in XML...");
        var doc = data as XDocument;
        var longestLabel = doc.Descendants("entry")
                              .Select(e => e.Attribute("label")?.Value)
                              .Where(label => label != null)
                              .OrderByDescending(label => label.Length)
                              .FirstOrDefault();
        Console.WriteLine($"Longest label: {longestLabel}");
    }

    public void Close()
    {
        Console.WriteLine("Finished processing XML.");
    }
}

public class Program
{
    static void Main()
    {
        var dbAccess = new DataAccessExecutor(new MockDbStrategy());
        dbAccess.Run();

        Console.WriteLine();

        var xmlAccess = new DataAccessExecutor(new XmlFileStrategy());
        xmlAccess.Run();
    }
}