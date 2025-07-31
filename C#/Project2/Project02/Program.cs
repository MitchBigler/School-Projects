///
/// <summary>
/// Project 2: Banking Program
/// This is a program create a new account class from input using the IAccount interface
/// </summary>
/// 
/// M. Bigler
/// 07/10/2025
///  
using System;

namespace UVUBank
{
    /// <summary>
    /// Driver program to handle console IO for creation of an account
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(" ========= UVU Bank =========\n");

            // atart with creating account
            Console.WriteLine(" ----- Create an Account ----\n");
            IAccount account = new Account();

            // get name from user
            string name;
            do
            {
                Console.WriteLine("Enter Name: ");
                name = Console.ReadLine();
                if (!account.SetName(name))
                {
                    Console.WriteLine("Name cannot be empty. Please enter a new name: ");
                }
            } while (!account.SetName(name)); // loop until returns true

            // get address from user
            string address;
            do
            {
                Console.WriteLine("Enter Address: ");
                address = Console.ReadLine();
                if (!account.SetAddress(address))
                {
                    Console.WriteLine("Address cannot be empty. Please enter a new address: ");
                }
            } while (!account.SetAddress(address)); // loop until returns true

            // get account number from user
            int accNumber;
            bool validAccNumber = false;
            do
            {
                Console.WriteLine("Enter Account Number: ");

                if (int.TryParse(Console.ReadLine(), out accNumber) && accNumber > 0)
                {
                    account.SetAccountNumber(accNumber);
                    validAccNumber = true;
                }
                else 
                {
                    Console.WriteLine("Invalid input. Please enter a valid whole number: ");
                }
            } while (!validAccNumber);

            // get balance from user
            decimal balance;
            bool balanceIsValid;

            do
            {
                Console.WriteLine("Enter starting balance (minimum 100): ");
                balanceIsValid = decimal.TryParse(Console.ReadLine(), out balance) && account.SetBalance(balance);
                if (!balanceIsValid)
                {
                    Console.WriteLine("Balance must be at least $100. Please enter a new amount: ");
                }
            } while (!balanceIsValid);

            // set state to new
            account.SetState(Account.AccountState.New);

            // print new account results
            Console.WriteLine("\nSUCCESS: New Account Created");
            OutputAccountInfo(account);

            // get deposit amount from user
            bool depositIsValid;
            do
            {
                Console.WriteLine("\nEnter amount to deposit: ");
                depositIsValid = decimal.TryParse(Console.ReadLine(), out decimal depositAmt);
                if (depositIsValid)
                {
                    account.PayInFunds(depositAmt);
                    Console.WriteLine($"\nSUCCESS: Deposited ${depositAmt}. \nCurrent Balance: ${account.GetBalance()}");
                }
            } while (!depositIsValid);

            // get withdrawal amount from user
            bool withdrawalIsValid;
            do
            {
                Console.WriteLine("\nEnter amount to withdrawal: ");
                withdrawalIsValid = decimal.TryParse(Console.ReadLine(), out decimal withdrawalAmt);
                if (withdrawalIsValid)
                {
                    bool success = account.WithdrawFunds(withdrawalAmt);
                    if (success)
                    {
                        Console.WriteLine($"\nSUCCESS: Withdrawn ${withdrawalAmt}.");
                    }
                    else {
                        Console.WriteLine("\nFAILED: Insufficient funds");
                    }
                    Console.WriteLine($"Current Balance: ${account.GetBalance()}");
                }
            } while (!withdrawalIsValid);

            OutputAccountInfo(account); // show acc info before quitting

        }

        /// <summary>
        /// Displays the current account's information
        /// </summary>
        /// <param name="account"></param>
        static void OutputAccountInfo(IAccount account)
        {
            Console.WriteLine("\n------ Account Info ------\n");
            Console.WriteLine($"       Name: {account.GetName()}");
            Console.WriteLine($"    Address: {account.GetAddress()}");
            Console.WriteLine($"   Account#: {account.GetAccountNumber()}");
            Console.WriteLine($"    Balance: ${account.GetBalance()}");
            Console.WriteLine($"      State: {account.GetState()}");
            Console.WriteLine("\n-----------------------------\n");
        }
    }
}
