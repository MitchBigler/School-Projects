using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UVUBank
{
    /// <summary>
    /// A concrete class of account with a minimum balance of $10 and minimum service fee of $5
    /// </summary>
    public class CheckingAccount : Account
    {
        // type specific vars
        private const decimal MIN_BALANCE = 10m;
        private const decimal MIN_FEE = 5m;

        // Savings account constructor
        public CheckingAccount(string name, string address, decimal balance)
            : base(name, address, balance, AccountType.Checking)
        {
            serviceFee = MIN_FEE;
        }

        // override set balance
        public override bool SetBalance(decimal inBalance)
        {
            if (inBalance < MIN_BALANCE)
            {
                return false;
            }

            balance = inBalance;
            return true;
        }

        // override set service fee
        public override bool SetServiceFee(decimal fee)
        {
            if (fee < MIN_FEE)
            {
                return false;
            }

            serviceFee = fee;
            return true;
        }
    }
}