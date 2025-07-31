using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UVUBank
{
    /// <summary>
    /// A concrete class of account with a minimum balance of $100 and minimum service fee of $0
    /// </summary>
    public class SavingsAccount : Account
    {
        // type specific vars
        private const decimal MIN_BALANCE = 100m;
        private const decimal MIN_FEE = 0m;

        // Savings account constructor
        public SavingsAccount(string name, string address, decimal balance)
            : base(name, address, balance, AccountType.Savings)
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
