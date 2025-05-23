using System;

abstract class AtmState
{
    protected AtmMachine Machine;

    public AtmState(AtmMachine machine)
    {
        Machine = machine;
    }

    public abstract void Handle(string action);
}

class IdleState : AtmState
{
    public IdleState(AtmMachine machine) : base(machine) { }

    public override void Handle(string action)
    {
        if (action == "insert_card")
        {
            Console.WriteLine("Card inserted. Please enter your PIN.");
            Machine.SetState(Machine.CardInsertedState);
        }
        else
        {
            Console.WriteLine("Please insert your card first.");
        }
    }
}

class CardInsertedState : AtmState
{
    private bool pinVerified = false;

    public CardInsertedState(AtmMachine machine) : base(machine) { }

    public override void Handle(string action)
    {
        if (!pinVerified && action == "enter_pin")
        {
            Console.WriteLine("PIN accepted. You can now withdraw.");
            pinVerified = true;
        }
        else if (pinVerified && action == "withdraw")
        {
            Console.WriteLine("Dispensing cash. Thank you!");
            Machine.SetState(Machine.IdleState);
        }
        else if (!pinVerified)
        {
            Console.WriteLine("Please enter your PIN.");
        }
        else
        {
            Console.WriteLine("Invalid action.");
        }
    }
}

class AtmMachine
{
    public AtmState IdleState { get; }
    public AtmState CardInsertedState { get; }

    private AtmState _currentState;

    public AtmMachine()
    {
        IdleState = new IdleState(this);
        CardInsertedState = new CardInsertedState(this);
        _currentState = IdleState;
    }

    public void SetState(AtmState state)
    {
        _currentState = state;
    }

    public void Handle(string action)
    {
        _currentState.Handle(action);
    }
}

public class Program
{
    static void Main()
    {
        var atm = new AtmMachine();

        atm.Handle("withdraw");       // Please insert your card first.
        atm.Handle("insert_card");    // Card inserted. Please enter your PIN.
        atm.Handle("withdraw");       // Please enter your PIN.
        atm.Handle("enter_pin");      // PIN accepted. You can now withdraw.
        atm.Handle("withdraw");       // Dispensing cash. Thank you!
        atm.Handle("withdraw");       // Please insert your card first.
    }
}
