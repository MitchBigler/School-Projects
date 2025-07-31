using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UVUBank
{
    /// <summary>
    /// Manager with dictionary for storing and retreiving back accounts
    /// </summary>
    public class AccountManager
    {
        // dict for accounts
        private Dictionary<string, IAccount> accounts = new Dictionary<string, IAccount>();

        /// <summary>
        /// Adds a new account to accounts dictionary
        /// </summary>
        /// <param name="account"></param>
        /// <returns></returns>
        public bool StoreAccount(IAccount account)
        {
            // check if null or empty
            if (account == null || string.IsNullOrWhiteSpace(account.GetName()))
            { 
                return false;
            }

            string key = account.GetAccountNumber().ToLower(); // assign lowercase account num to key

            // add account to dict if not already
            if (!accounts.ContainsKey(key))
            {
                accounts.Add(key, account);
                return true;
            }

            // false if account already in dict
            return false;

        }

        /// <summary>
        /// Returns an account by accountNumber
        /// </summary>
        /// <param name="accountNumber"></param>
        /// <returns></returns>
        public IAccount GetAccount(string accountNumber)
        {
            // check if null or empty
            if (string.IsNullOrWhiteSpace(accountNumber))
            {
                return null;
            }

            accounts.TryGetValue(accountNumber.ToLower(), out IAccount account);
            return account;
        }
    }
}
