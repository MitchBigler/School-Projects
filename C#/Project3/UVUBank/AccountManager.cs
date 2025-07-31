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

            string key = account.GetName().ToLower(); // assign lowercase account name to key

            // add account to dict if not already
            if (!accounts.ContainsKey(key))
            {
                accounts.Add(key, account);
                return true;
            }

            // false if account already in dict
            return false;

        }

        public IAccount GetAccount(string accountName)
        {
            // check if null or empty
            if (string.IsNullOrWhiteSpace(accountName))
            {
                return null;
            }

            accounts.TryGetValue(accountName, out IAccount account);
            return account;
        }
        
    }
}
