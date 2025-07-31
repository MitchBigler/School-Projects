///
/// <summary>
/// Project 3: Banking Program - Account Types
/// This is an abstract class implementation of the IAccount
/// </summary>
/// 
/// M. Bigler
/// 07/12/2025
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
    public abstract class Account : IAccount
    {
        /* ------------- ACCOUNT VARIABLES ------------- */
        // enums
        public enum AccountState { New, Active, UnderAudit, Frozen, Closed }
        public enum AccountType { Savings, Checking, CD }

        // account vars
        protected string name;
        protected string address;
        protected string accountNumber;

        protected decimal balance;
        protected decimal serviceFee = 0m;

        protected AccountState accountState;
        protected AccountType accountType;

        // counter for acc nums
        private static int numCounter = 1000;


        /* ------------- ACCOUNT CONSTRUCTOR ------------- */
        protected Account(string name, string address, decimal balance, AccountType type)
        {
            // check valid name & address
            if (!SetName(name) || !SetAddress(address))
            {
                throw new ArgumentException("Invalid name or address.");
            }
            // set valid
            this.accountType = type;
            this.accountNumber = GenerateAccountNumber(type);
            SetState(AccountState.New);

            // check balance
            if (!SetBalance(balance))
            {
                throw new ArgumentException("Invalid balance for account type");
            }
        }

        /* ------------- CONSTRUCTOR METHODS ------------- */
        // generate an account number using counter and acc type
        protected string GenerateAccountNumber(AccountType type) 
        {
            char typeSuffix = type switch
            // assign suffix based on type
            {
                AccountType.Savings => 'S',
                AccountType.Checking => 'C',
                AccountType.CD => 'D',
                _ => throw new ArgumentException($"Cannot generate account number for this type: {type}")
            };
            return $"{++numCounter}{typeSuffix}";
        }

        /* ------------- CONTACT GET/SET ------------- */
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

        /* ------------- MONEY METHODS ------------- */
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

        /* ------------- MONEY GET/SET ------------- */
        // set balance (virtual)
        public virtual bool SetBalance(decimal inBalance)
        { 
            balance = inBalance;
            return true;
        }
        // get balance
        public decimal GetBalance() { return balance; }

        // set service fee (virtual)
        public virtual bool SetServiceFee(decimal fee)
        {
            serviceFee = fee;
            return true;
        }
        // get service fee
        public decimal GetServiceFee() { return serviceFee; }

        /* ------------- ACCOUNT INFO GET/SET ------------- */
        // set state
        public void SetState(AccountState inState) 
        {
            accountState = inState;
        }
        // get state
        public AccountState GetState() { return accountState; }

        // get acc num
        public string GetAccountNumber() { return accountNumber; }

        // get acc type
        public AccountType GetAccountType() { return accountType; }
    }

        
}
