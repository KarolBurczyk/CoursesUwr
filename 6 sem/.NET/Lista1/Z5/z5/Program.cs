using System;

namespace AccessModifiersDemo
{
    class BaseClass
    {
        public string PublicField = "Public Field";      // Dostępne wszędzie
        protected string ProtectedField = "Protected Field"; // Dostępne w klasach dziedziczących
        internal string InternalField = "Internal Field"; // Dostępne w obrębie tego samego assembly
        private string PrivateField = "Private Field";   // Dostępne tylko w tej klasie

        public void ShowFields()
        {
            Console.WriteLine($"Inside BaseClass: {PublicField}, {ProtectedField}, {InternalField}, {PrivateField}");
        }
    }

    class DerivedClass : BaseClass
    {
        public void ShowInheritedFields()
        {
            Console.WriteLine($"Inside DerivedClass: {PublicField}, {ProtectedField}, {InternalField}");
            // Console.WriteLine(PrivateField); // Error
        }
    }

    class Program
    {
        static void Main()
        {
            BaseClass baseObj = new BaseClass();
            Console.WriteLine($"From Main: {baseObj.PublicField}, {baseObj.InternalField}");
            // Console.WriteLine(baseObj.ProtectedField); // Error
            // Console.WriteLine(baseObj.PrivateField); // Error

            DerivedClass derivedObj = new DerivedClass();
            derivedObj.ShowInheritedFields();

            baseObj.ShowFields();
        }
    }
}
