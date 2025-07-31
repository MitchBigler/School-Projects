///
/// <summary>
/// Project 3: Banking Program - Account Types
/// This is a program create a new account class from input using the IAccount interface
/// </summary>
/// 
/// M. Bigler
/// 07/12/2025
///  
using System;
using System.Security.Principal;

namespace UVUBank
{
    /// <summary>
    /// Driver program to handle console IO for creation of an account
    /// </summary>
    class Program
    {
        static AccountManager manager = new AccountManager(); // instatiate a manager

        static void Main(string[] args)
        {
            /* ------------- MENU LOOP ------------- */
            bool running = true;
            while (running)
            {
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine(" ========= UVU Bank =========");
                Console.ResetColor();

                Console.WriteLine("\nChoose an option:");
                Console.WriteLine(" - [1]: Create New Account");
                Console.WriteLine(" - [2]: Access Existing Account");
                Console.WriteLine(" - [3]: Quit");

                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "1": // Create New Account
                        Console.Clear();
                        IAccount newAccount = CreateNewAccount();
                        if (manager.StoreAccount(newAccount))
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                            Console.WriteLine("\nSUCCESS: Account Created and Saved.");
                            Console.ResetColor();
                            System.Threading.Thread.Sleep(600); // 0.6 seconds
                            OutputAccountInfo(newAccount);
                            WaitForUser();
                            break;
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("\nError: Failed to save account. Try a different name.");
                            Console.ResetColor();
                            WaitForUser();
                        }
                        break;

                    case "2": // Access Existing Account
                        Console.Clear();
                        Console.WriteLine("\n ----- Access an Account ----\n");
                        Console.Write("\nEnter account name:");

                        string search = Console.ReadLine().ToLower();
                        IAccount foundAccount = manager.GetAccount(search);

                        if (foundAccount != null) // if found
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                            Console.WriteLine("\nAccount Found");
                            Console.ResetColor();
                            System.Threading.Thread.Sleep(600); // 0.6 seconds
                            Console.Clear();
                            AccessAccount(foundAccount);
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("\nNo account found.");
                            Console.ResetColor();
                            WaitForUser();
                        }
                        break;

                    case "3": // Quit
                        running = false;
                        Console.ForegroundColor = ConsoleColor.DarkGreen;
                        Console.WriteLine("\nThank you for using UVU Bank.");
                        Console.ResetColor();
                        break;

                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("\nInvalid choice.");
                        Console.ResetColor();

                        System.Threading.Thread.Sleep(400); // 0.40 seconds
                        Console.Clear();
                        break;

                }
            }
        }

        /// Prompt for user creation of a new account
        /// </summary>
        /// <returns></returns>
        /// <exception cref="Exception"></exception>
        static IAccount CreateNewAccount()
        {
            Console.WriteLine("----- Create an Account -----\n");

            // get name from user
            string name;
            do
            {
                Console.Write("\n   Enter Name: ");
                name = Console.ReadLine();

            } while (string.IsNullOrWhiteSpace(name)); // loop until valid string

            // get address from user
            string address;
            do
            {
                Console.Write("\nEnter Address: ");
                address = Console.ReadLine();

            } while (string.IsNullOrWhiteSpace(address)); // loop until valid string

            // get account type from user
            Account.AccountType type;

            while (true)
            {
                Console.WriteLine("\nSelect Account Type:\n -[1] Savings\n -[2] Checking\n -[3] CD");
                string choice = Console.ReadLine();

                switch (choice) 
                {
                    case "1": // Savings
                        type = Account.AccountType.Savings;
                        break;

                    case "2": // Checking
                        type = Account.AccountType.Checking;
                        break;

                    case "3": // CD
                        type = Account.AccountType.CD;
                        break;

                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Invalid input. Try again.");
                        Console.ResetColor();
                        continue;
                }
                break;
            }

            decimal balance;
            decimal requiredMin = type switch
            {
                Account.AccountType.Savings => 100m,
                Account.AccountType.Checking => 10m,
                Account.AccountType.CD => 500m,
                _ => throw new Exception("Unknown account type")
            };

            while (true)
            {
                Console.Write($"\nEnter starting balance (minimum {requiredMin:C}): ");
                if (decimal.TryParse(Console.ReadLine(), out balance))
                {
                    if (balance >= requiredMin)
                    {
                        break;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine($"\nAmount must be at least {requiredMin:C}.");
                        Console.ResetColor();
                    }
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\nInvalid input. Please enter a valid number.");
                    Console.ResetColor();
                }
            }

            // Create account by type
            return type switch
            {
                Account.AccountType.Savings => new SavingsAccount(name, address, balance),
                Account.AccountType.Checking => new CheckingAccount(name, address, balance),
                Account.AccountType.CD => new CDAccount(name, address, balance),
                _ => throw new Exception("Invalid account type")
            };
        }

        /// <summary>
        /// Show menu that allows user to manipulate account values 
        /// </summary>
        /// <param name="account"></param>
        static void AccessAccount(IAccount account) 
        {
            bool accessing = true;

            while (accessing)
            {
                Console.WriteLine(" ----- Access Account -----\n");

                OutputAccountInfo(account);
                Console.WriteLine("\nSelect an option:\n -[1] Deposit\n -[2] Withdraw\n -[3] Change Service Fee\n -[4] Back");
                string choice = Console.ReadLine();
                switch (choice) {
                    case "1": // DEPOSIT
                        bool depositIsValid;

                        do // get amount from user
                        {
                            Console.Write("\nEnter amount to deposit: ");
                            depositIsValid = decimal.TryParse(Console.ReadLine(), out decimal depositAmt);
                            if (depositIsValid)
                            {
                                account.PayInFunds(depositAmt);
                                Console.ForegroundColor = ConsoleColor.Green;
                                Console.WriteLine($"\nSUCCESS: Deposited ${depositAmt}.");
                                Console.ResetColor();
                                Console.WriteLine($"Current Balance: ${account.GetBalance()}");
                                WaitForUser();
                            }
                        } while (!depositIsValid);
                        break;

                    case "2": // WITHDRAW
                        bool withdrawalIsValid;

                        do // get amount from user
                        {
                            Console.Write("\nEnter amount to withdrawal: ");
                            withdrawalIsValid = decimal.TryParse(Console.ReadLine(), out decimal withdrawalAmt);
                            if (withdrawalIsValid)
                            {
                                bool success = account.WithdrawFunds(withdrawalAmt);
                                if (success)
                                {
                                    Console.ForegroundColor = ConsoleColor.Green;
                                    Console.WriteLine($"\nSUCCESS: Withdrawn ${withdrawalAmt}.");
                                    Console.ResetColor();
                                    Console.WriteLine($"Current Balance: ${account.GetBalance()}");
                                    WaitForUser();
                                }
                                else
                                {
                                    Console.ForegroundColor = ConsoleColor.Red;
                                    Console.WriteLine("\nFAILED: Insufficient funds");
                                    Console.ResetColor();
                                    WaitForUser();
                                }
                            }
                        } while (!withdrawalIsValid);
                            break;

                    case "3": // CHANGE SERVICE FEE
                        bool feeIsValid;

                        do // get amount from user
                        {
                            Console.Write("\nEnter new service fee: ");
                            feeIsValid = decimal.TryParse(Console.ReadLine(), out decimal fee);
                            if (feeIsValid)
                            {
                                bool success = account.SetServiceFee(fee);
                                if (success)
                                {
                                    Console.ForegroundColor = ConsoleColor.Green;
                                    Console.WriteLine($"\nSUCCESS: New Fee: ${fee}.");
                                    Console.ResetColor();
                                    WaitForUser();
                                }
                                else
                                {
                                    Console.ForegroundColor = ConsoleColor.Red;
                                    Console.WriteLine("\nFAILED: Invalid or below minimum amount");
                                    Console.ResetColor();
                                    WaitForUser();
                                }
                            }
                        } while (!feeIsValid);
                        break;

                    case "4": // BACK
                        accessing = false;
                        Console.WriteLine("Returning...");
                        System.Threading.Thread.Sleep(300); // 0.3 seconds
                        Console.Clear();
                        break;

                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Invalid input. Try again.");
                        Console.ResetColor();

                        System.Threading.Thread.Sleep(400); // 0.4 seconds
                        Console.Clear();
                        break;
                }
            }
        }

        /// <summary>
        /// Displays the current account's information
        /// </summary>
        /// <param name="account"></param>
        static void OutputAccountInfo(IAccount account)
        {
            Console.WriteLine("\n------- Account Info --------\n");
            Console.WriteLine($"        Name: {account.GetName()}");
            Console.WriteLine($"     Address: {account.GetAddress()}");
            Console.WriteLine($"    Account#: {account.GetAccountNumber()}");
            Console.WriteLine($"Account Type: {account.GetAccountType()}");
            Console.WriteLine($"       State: {account.GetState()}");
            Console.WriteLine($" Service Fee: ${account.GetServiceFee()}");
            Console.WriteLine($"\n     Balance: ${account.GetBalance()}");

            Console.WriteLine("\n-----------------------------\n");
        }

        /// <summary>
        /// Pause console until user inputs a value
        /// </summary>
        static void WaitForUser()
        {
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
            Console.Clear();
        }

    }
}
