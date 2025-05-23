using System.Reflection;
using System.Text;
public class XMLGenerator
{
    public string GenerateXML(object dataObject)
    {
        Type type = dataObject.GetType();
        StringBuilder xml = new StringBuilder();
        xml.Append("<" + type.Name + ">");

        foreach (PropertyInfo property in type.GetProperties())
        {
            xml.Append($"<{property.Name}>{property.GetValue(dataObject)}</{property.Name}>");
        }

        xml.Append("</" + type.Name + ">");
        return xml.ToString();
    }
}

public class Person
{
    public string Name { get; set; }
    public string Surname { get; set; }
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
