public class Person { }

public abstract class AbstractPersonRegistry1
{
    public INotifier _notifier;
    public abstract List<Person> GetPersons();
    public void NotifyPersons()
    {
        foreach (Person person in GetPersons())
            _notifier.Notify(person);
    }
}
public interface INotifier
{
    void Notify(Person person);
}

//-----------------------------------------------------------

public abstract class AbstractPersonRegistry2
{
    public IPersonGetter _personGetter;
    public List<Person> GetPersons()
    {
        return _personGetter.Load();
    }

    public abstract void NotifyPersons();
}
public interface IPersonGetter
{
    List<Person> Load();
}