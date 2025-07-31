///
/// <summary>
/// Project 3: Banking Program - Account Types
/// This is an interface to define the Account class
/// </summary>
/// 
/// M. Bigler
/// 07/10/2025
///  

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UVUBank
{
    /// <summary>
    /// The interface to define the account class
    /// </summary>
    public interface IAccount
    {
        // contact info
        bool SetName(string inName);
        string GetName();

        bool SetAddress(string inAddress);
        string GetAddress();

        // money
        void PayInFunds(decimal amount);
        bool WithdrawFunds(decimal amount);

        bool SetBalance(decimal inBalance);
        decimal GetBalance();

        // account info
        void SetState(Account.AccountState state);
        Account.AccountState GetState();
        Account.AccountType GetAccountType();
        string GetAccountNumber();

        // service fee
        bool SetServiceFee(decimal fee);
        decimal GetServiceFee();

    }
}
