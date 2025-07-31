///
/// <summary>
/// Project 2: Banking Program
/// This is an implementation of the IAccount
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
    /// The account class to implement account functionality
    /// </summary>
    public class Account : IAccount
    {
        // states enum
        public enum AccountState { New, Active, UnderAudit, Frozen, Closed }

        // accounts vars
        private string name;
        private string address;
        private int accountNumber;
        private decimal balance;
        private AccountState accountState;
        private const decimal MIN_BALANCE = 100m;

        // set name
        public bool SetName(string inName)
        {
            if (string.IsNullOrWhiteSpace(inName)) return false;
            name = inName;
            return true;
        }
        // get name
        public string GetName() { return name; }

        // set address
        public bool SetAddress(string inAddress)
        {
            if (string.IsNullOrWhiteSpace(inAddress)) return false;
            address = inAddress;
            return true;
        }
        // get address
        public string GetAddress() { return address; }

        // add amount
        public void PayInFunds(decimal amount)
        {
            if (amount > 0) 
            { 
                balance += amount;
            }
        }

        // subtract amount
        public bool WithdrawFunds(decimal amount)
        {
            if (amount <= balance) 
            { 
                balance -= amount;
                return true;
            }
            return false;
        }

        // set balance
        public bool SetBalance(decimal inBalance)
        { 
            if (inBalance < MIN_BALANCE) return false;
            balance = inBalance;
            return true;
        }
        // get balance
        public decimal GetBalance() { return balance; }

        // set state
        public void SetState(AccountState inState) 
        {
            accountState = inState;
        }
        // get state
        public AccountState GetState() { return accountState; }

        // set acc num
        public void SetAccountNumber(int inNumber) 
        {
            accountNumber = inNumber;
        }
        // get acc num
        public int GetAccountNumber() { return accountNumber; }
    }
}
