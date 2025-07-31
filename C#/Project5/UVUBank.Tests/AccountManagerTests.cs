using Microsoft.VisualStudio.TestTools.UnitTesting;
using UVUBank;

namespace UVUBank.Tests
{
    [TestClass]
    public class AccountManagerTests
    {
        [TestMethod]
        public void StoreAccount_Valid()
        {
            var manager = new AccountManager();
            var account = new SavingsAccount("123", "Test User", 100);

            var result = manager.StoreAccount(account);

            Assert.IsTrue(result); // should return true
        }

        [TestMethod]
        public void StoreAccount_Null()
        {
            var manager = new AccountManager();

            var result = manager.StoreAccount(null);

            Assert.IsFalse(result); // should return false
        }

        [TestMethod]
        public void GetAccount_Existing()
        {
            var manager = new AccountManager();
            var account = new SavingsAccount("123", "Test User", 100);
            manager.StoreAccount(account);

            string accountNum = account.GetAccountNumber();
            Console.WriteLine("Account Number: " + accountNum);
            var found = manager.GetAccount(accountNum);
            Console.WriteLine(found);

            Assert.IsNotNull(found);                               // should exist
            Assert.AreEqual(accountNum, found.GetAccountNumber()); // and match
        }

        [TestMethod]
        public void GetAccount_Nonexisting()
        {
            var manager = new AccountManager();

            var found = manager.GetAccount("NA");

            Assert.IsNull(found);
        }
    }
}