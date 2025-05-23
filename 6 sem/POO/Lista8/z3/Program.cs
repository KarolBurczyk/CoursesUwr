using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

abstract class DataAccessTemplate
{
    public void Run()
    {
        OpenConnection();
        var rawData = LoadData();
        AnalyzeData(rawData);
        CloseConnection();
    }

    protected abstract void OpenConnection();
    protected abstract object LoadData();
    protected abstract void AnalyzeData(object data);
    protected abstract void CloseConnection();
}

class MockDatabaseAccess : DataAccessTemplate
{
    private List<Dictionary<string, object>> _mockTable;

    protected override void OpenConnection()
    {
        Console.WriteLine("Simulating database connection...");
        _mockTable = new List<Dictionary<string, object>>
        {
            new Dictionary<string, object> { { "Amount", 15 }, { "Description", "Item A" } },
            new Dictionary<string, object> { { "Amount", 25 }, { "Description", "Item B" } },
            new Dictionary<string, object> { { "Amount", 40 }, { "Description", "Item C" } }
        };
    }

    protected override object LoadData()
    {
        Console.WriteLine("Retrieving mock data from database...");
        return _mockTable;
    }

    protected override void AnalyzeData(object data)
    {
        Console.WriteLine("Analyzing retrieved database records...");
        var rows = data as List<Dictionary<string, object>>;
        int total = rows.Sum(r => Convert.ToInt32(r["Amount"]));
        Console.WriteLine($"Total 'Amount' field value: {total}");
    }

    protected override void CloseConnection()
    {
        Console.WriteLine("Simulated database connection closed.");
    }
}

class XmlFileAccess : DataAccessTemplate
{
    private XDocument _xmlData;

    protected override void OpenConnection()
    {
        Console.WriteLine("Loading XML content...");
        string xmlString = @"
        <data>
            <entry label='x' />
            <entry label='extremelylonglabelvalue' />
            <entry label='ccc' />
        </data>";
        _xmlData = XDocument.Parse(xmlString);
    }

    protected override object LoadData()
    {
        Console.WriteLine("Extracting XML elements...");
        return _xmlData;
    }

    protected override void AnalyzeData(object data)
    {
        Console.WriteLine("Processing XML nodes...");
        var doc = data as XDocument;
        var longestLabel = doc.Descendants("entry")
                              .Select(e => e.Attribute("label")?.Value)
                              .Where(label => label != null)
                              .OrderByDescending(label => label.Length)
                              .FirstOrDefault();

        Console.WriteLine($"Longest 'label' attribute: {longestLabel}");
    }

    protected override void CloseConnection()
    {
        Console.WriteLine("Finished processing XML file.");
    }
}

public class App
{
    public static void Main()
    {
        var db = new MockDatabaseAccess();
        db.Run();

        Console.WriteLine();

        var xml = new XmlFileAccess();
        xml.Run();
    }
}
