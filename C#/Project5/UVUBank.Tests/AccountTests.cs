using Microsoft.VisualStudio.TestTools.UnitTesting;
using UVUBank;

namespace UVUBank.Tests
{
    [TestClass]
    public class AccountTests
    {
        /* ---------- GETTERS AND SETTERS ---------- */

        [TestMethod]
        public void SetAndGetName()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            // should be valid
            bool success = account.SetName("New Name");
            Assert.IsTrue(success);
            Assert.AreEqual("New Name", account.GetName());

            // should be invalid
            success = account.SetName("");
            Assert.IsFalse(success);
            Assert.AreEqual("New Name", account.GetName());
        }

        [TestMethod]
        public void SetAndGetAddress()
        {
            var account = new SavingsAccount("Name", "Address", 100);

            // should be valid
            bool success = account.SetAddress("New Address");
            Assert.IsTrue(success);
            Assert.AreEqual("New Address", account.GetAddress());

            // should be invalid
            success = account.SetAddress("");
            Assert.IsFalse(success);
            Assert.AreEqual("New Address", account.GetAddress());
        }

        [TestMethod]
        public void SetAndGetBalance()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            bool success = account.SetBalance(250);
            Assert.IsTrue(success);
            Assert.AreEqual(250, account.GetBalance());
        }

        [TestMethod]
        public void SetAndGetServiceFee()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            bool success = account.SetServiceFee(12.00m);
            Assert.IsTrue(success);
            Assert.AreEqual(12.00m, account.GetServiceFee());
        }

        [TestMethod]
        public void SetAndGetState()
        {
            var account = new SavingsAccount("Name", "Addr", 100);
            account.SetState(Account.AccountState.Frozen);

            Assert.AreEqual(Account.AccountState.Frozen, account.GetState());
        }


        /* ---------- BANKING METHODS ---------- */

        [TestMethod]
        public void DepositAmount()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            account.PayInFunds(100);

            Assert.AreEqual(200, account.GetBalance());
        }

        [TestMethod]
        public void DepositAmount_Negative()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            account.PayInFunds(-100);

            Assert.AreEqual(100, account.GetBalance());
        }

        [TestMethod]
        public void WithdrawAmount()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            account.WithdrawFunds(50);

            Assert.AreEqual(50, account.GetBalance());
        }

        [TestMethod]
        public void WithdrawAmount_TooMuch()
        {
            var account = new SavingsAccount("Name", "Addr", 100);

            bool result = account.WithdrawFunds(200);

            Assert.IsFalse(result);
            Assert.AreEqual(100, account.GetBalance());
        }
    }
}