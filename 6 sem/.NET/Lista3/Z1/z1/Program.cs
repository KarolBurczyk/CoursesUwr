using System.Text;

public interface IClassInfo
{
    string[] GetFieldNames();
    object GetFieldValue(string fieldName);
}

public class XMLGenerator
{
    public string GenerateXML(IClassInfo dataObject)
    {
        StringBuilder xml = new StringBuilder();
        xml.Append("<object>");
        foreach (var field in dataObject.GetFieldNames())
        {
            xml.Append($"<{field}>{dataObject.GetFieldValue(field)}</{field}>");
        }
        xml.Append("</object>");
        return xml.ToString();
    }
}

public class Person : IClassInfo
{
    public string Name { get; set; }
    public string Surname { get; set; }

    public string[] GetFieldNames() => new[] { "Name", "Surname" };
    public object GetFieldValue(string fieldName) => fieldName switch
    {
        "Name" => Name,
        "Surname" => Surname,
        _ => null
    };
}

public class main
{
    static void Main(string[] args)
    {
        Person person =
        new Person()
        {
            Name = "Jan",
            Surname = "Kowalski"
        };
        XMLGenerator generator = new XMLGenerator();
        string xml = generator.GenerateXML(person);
        Console.WriteLine(xml);
    }
}
