using System.Reflection;
using System.Text;

[AttributeUsage(AttributeTargets.Property)]
public class IgnoreInXMLAttribute : Attribute { }
public class XMLGenerator
{
    public string GenerateXML(object dataObject)
    {
        Type type = dataObject.GetType();
        StringBuilder xml = new StringBuilder();
        xml.Append("<" + type.Name + ">");

        foreach (PropertyInfo property in type.GetProperties())
        {
            if (Attribute.IsDefined(property, typeof(IgnoreInXMLAttribute)))
                continue;

            xml.Append($"<{property.Name}>{property.GetValue(dataObject)}</{property.Name}>");
        }

        xml.Append("</" + type.Name + ">");
        return xml.ToString();
    }
}

public class Person
{
    [IgnoreInXML]
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
