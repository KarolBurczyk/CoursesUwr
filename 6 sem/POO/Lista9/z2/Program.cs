using Microsoft.EntityFrameworkCore;

using var context = new AppDbContext();

if (!context.Authors.Any())
{
    var author = new Author { Name = "Jan Kowalski" };
    author.Books.Add(new Book { Title = "Pierwsza książka" });
    author.Books.Add(new Book { Title = "Druga książka" });

    context.Authors.Add(author);
    context.SaveChanges();
}

foreach (var a in context.Authors.Include(a => a.Books))
{
    Console.WriteLine($"{a.Name} napisał:");
    foreach (var book in a.Books)
    {
        Console.WriteLine($" - {book.Title}");
    }
}
