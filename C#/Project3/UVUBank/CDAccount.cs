using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UVUBank
{
    /// <summary>
    /// A concrete class of account with a minimum balance of $500 and minimum service fee of $8
    /// </summary>
    public class CDAccount : Account
    {
        // type specific vars
        private const decimal MIN_BALANCE = 500m;
        private const decimal MIN_FEE = 8m;

        // Savings account constructor
        public CDAccount(string name, string address, decimal balance)
            : base(name, address, balance, AccountType.CD)
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