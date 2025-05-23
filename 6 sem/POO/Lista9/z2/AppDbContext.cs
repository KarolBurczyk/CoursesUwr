using Microsoft.EntityFrameworkCore;
using ORMExample.Models;

public class AppDbContext : DbContext
{
    public DbSet<Author> Authors { get; set; }
    public DbSet<Book> Books { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        options.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=OrmDemoDb;Trusted_Connection=True;");
    }
}
