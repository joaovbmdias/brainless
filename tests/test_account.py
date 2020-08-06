import unittest
# import constants
# from configuration import db
# from models.account import Account

# db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestAccount(unittest.TestCase):
    """
    Unit Testing Accounts
    """
    pass
    def test_test(self):
        self.assertEqual(1,1)
    # def test_1_1_create_account_oauth(self):
    #     """
    #     Test that it can create an account type OAUTH
    #     """
    #     account = Account(name="Test Account",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.OAUTH,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="teste@email.com",
    #                       client_secret="adtshwathwrjrjhrtj",
    #                       username=None,
    #                       password=None,
    #                       api_key=None,
    #                       sync_frequency=1)

    #     result = account.create()

    #     self.assertIsNotNone(account.id, "Account ID cannot be None")
    #     self.assertGreater(account.id, 0, "Account ID must be greater than 0")
    #     self.assertEqual(result, constants.SUCCESS)

    # def test_1_2_create_account_user_pass(self):
    #     """
    #     Test that it can create an account type USER_PASS
    #     """
    #     account = Account(name="Test Account 2",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.USER_PASS,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username="teste@email.com",
    #                       password="adtshwathwrjrjhrtj",
    #                       api_key=None,
    #                       sync_frequency=1)

    #     result = account.create()

    #     self.assertIsNotNone(account.id, "Account ID cannot be None")
    #     self.assertGreater(account.id, 0, "Account ID must be greater than 0")
    #     self.assertEqual(result, constants.SUCCESS)

    # def test_1_3_create_account_api_key(self):
    #     """
    #     Test that it can create an account type API_KEY
    #     """
    #     account = Account(name="Test Account 3",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.API_KEY,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username=None,
    #                       password=None,
    #                       api_key="adtshwathwrjrjhrtj",
    #                       sync_frequency=1,
    #                       id=3)

    #     result = account.create()

    #     self.assertIsNotNone(account.id, "Account ID cannot be None")
    #     self.assertGreater(account.id, 0, "Account ID must be greater than 0")
    #     self.assertEqual(result, constants.SUCCESS)

    # def test_2_1_create_same_account_by_name(self):
    #     """
    #     Test that it cannot create an already existing account
    #     Account with the same name for the same user
    #     """
    #     account = Account(name="Test Account",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.OAUTH,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="teste2@email.com",
    #                       client_secret="adtshwathwrjrjhrtj",
    #                       username=None,
    #                       password=None,
    #                       api_key=None,
    #                       sync_frequency=1)      
        
    #     result = account.create()

    #     self.assertIsNone(account.id, "Account ID must be None")
    #     self.assertEqual(result, constants.FAILURE)

    # def test_2_2_create_same_account_by_username(self):
    #     """
    #     Test that it cannot create an already existing account
    #     Account with the same provider and same username for the same user
    #     """
    #     account = Account(name="Test Account username",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.USER_PASS,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username="teste@email.com",
    #                       password="adtshwathwrjrjhrtj",
    #                       api_key=None,
    #                       sync_frequency=1)   
        
    #     result = account.create()

    #     self.assertIsNone(account.id, "Account ID must be None")
    #     self.assertEqual(result, constants.FAILURE)

    # def test_2_3_create_same_account_by_apikey(self):
    #     """
    #     Test that it cannot create an already existing account
    #     Account with the same provider and same api_key for the same user
    #     """
    #     account = Account(name="Test Account api key",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.API_KEY,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username=None,
    #                       password=None,
    #                       api_key="adtshwathwrjrjhrtj",
    #                       sync_frequency=1)    
        
    #     result = account.create()

    #     self.assertIsNone(account.id, "Account ID must be None")
    #     self.assertEqual(result, constants.FAILURE)

    # def test_2_4_create_same_account_by_client_id(self):
    #     """
    #     Test that it cannot create an already existing account
    #     Account with the same provider and same client_id for the same user
    #     """
    #     account = Account(name="Test Account oauth",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.OAUTH,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="teste@email.com",
    #                       client_secret="adtshwathwrjrjhrtj",
    #                       username=None,
    #                       password=None,
    #                       api_key=None,
    #                       sync_frequency=1)      
        
    #     result = account.create()

    #     self.assertIsNone(account.id, "Account ID must be None")
    #     self.assertEqual(result, constants.FAILURE)

    # def test_3_1_delete_existing_account(self):
    #     """
    #     Test that it can delete an existing account
    #     """   
    #     account = Account(name="Test Account 3",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.API_KEY,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username=None,
    #                       password=None,
    #                       api_key="adtshwathwrjrjhrtj",
    #                       sync_frequency=1)

    #     result = account.delete()

    #     self.assertEqual(result, constants.SUCCESS)

    # def test_3_2_delete_unexisting_account(self):
    #     """
    #     Test that it cannot delete an unexisting account
    #     """
    #     account = Account(name=None,
    #                       account_type=None,
    #                       authentication_type=None,
    #                       provider=None,
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username=None,
    #                       password=None,
    #                       api_key=None,
    #                       sync_frequency=None,
    #                       id=10000)
    #     result = account.delete()

    #     self.assertEqual(result, constants.FAILURE)

    # def test_4_1_read_one_existing_account(self):
    #     """
    #     Test that it can read an existing account
    #     """
    #     account = Account(name                = None,
    #                       account_type        = None,
    #                       authentication_type = None,
    #                       provider            = None,
    #                       user_id             = None,
    #                       client_id           = None,
    #                       client_secret       = None,
    #                       username            = None,
    #                       password            = None,
    #                       api_key             = None,
    #                       sync_frequency      = None,
    #                       id                  = 1)

    #     result = account.read()

    #     self.assertEqual(result, constants.SUCCESS)

    # def test_4_2_read_one_unexisting_account(self):
    #     """
    #     Test that it cannot read an unexisting account
    #     """
    #     account = Account(name                = None,
    #                       account_type        = None,
    #                       authentication_type = None,
    #                       provider            = None,
    #                       user_id             = None,
    #                       client_id           = None,
    #                       client_secret       = None,
    #                       username            = None,
    #                       password            = None,
    #                       api_key             = None,
    #                       sync_frequency      = None,
    #                       id                  = 100000)

    #     result = account.read()

    #     self.assertEqual(result, constants.FAILURE)

    # def test_5_1_update_existing_account(self):
    #     """
    #     Test that it can update an existing account
    #     """
    #     account = Account(name="Test Account Updated Again",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.OAUTH,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="teste@email.com",
    #                       client_secret="adtshwathwrjrjhrtj",
    #                       username=None,
    #                       password=None,
    #                       api_key=None,
    #                       sync_frequency=1,
    #                       id=1)

    #     result = account.update()

    #     self.assertEqual(result, constants.SUCCESS)

    # def test_5_2_update_unexisting_account(self):
    #     """
    #     Test that it cannot update an unexisting account
    #     """
    #     account = Account(name="Test Account Updated Again",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.OAUTH,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="teste@email.com",
    #                       client_secret="adtshwathwrjrjhrtj",
    #                       username=None,
    #                       password=None,
    #                       api_key=None,
    #                       sync_frequency=1,
    #                       id=100000)

    #     result = account.update()

    #     self.assertEqual(result, constants.FAILURE)

    # def test_6_1_check_account_oauth(self):
    #     """
    #     Test that it cannot create an account type OAUTH with username, password or api_key fields
    #     """
    #     account = Account(name="Test Account Check Constraint Oauth",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.OAUTH,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="check@email.com",
    #                       client_secret="asdfghjklçqwertyuiopzxcvbnm",
    #                       username="shouldntbehere",
    #                       password="shouldntbehere",
    #                       api_key="shouldntbehere",
    #                       sync_frequency=1,
    #                       id=1)
        
    #     result = account.create()

    #     self.assertEqual(result, constants.FAILURE)

    # def test_6_2_check_account_user_pass(self):
    #     """
    #     Test that it cannot create an account type USER_PASS with client_id, client_secret or api_key fields
    #     """
    #     account = Account(name="Test Account Check Constraint User Pass",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.USER_PASS,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="shouldntbehere",
    #                       client_secret="shouldntbehere",
    #                       username="check@email.com",
    #                       password="asdfghjklçqwertyuiopzxcvbnm",
    #                       api_key="shouldntbehere",
    #                       sync_frequency=1,
    #                       id=1)

    #     result = account.create()

    #     self.assertEqual(result, constants.FAILURE)

    # def test_6_3_check_account_api_key(self):
    #     """
    #     Test that it cannot create an account type API_KEY with username, password, client_id or client_secret fields
    #     """
    #     account = Account(name="Test Account Check Constraint Api Key",
    #                       account_type="CALENDAR",
    #                       authentication_type=constants.API_KEY,
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id="shouldntbehere",
    #                       client_secret="shouldntbehere",
    #                       username="shouldntbehere",
    #                       password="shouldntbehere",
    #                       api_key="asdfghjklçqwertyuiopzxcvbnm",
    #                       sync_frequency=1,
    #                       id=1)

    #     result = account.create()

    #     self.assertEqual(result, constants.FAILURE)

    # def test_6_4_check_account_auth_type(self):
    #     """
    #     Test that it cannot create an account with auth type not in API_KEY, USER_PASS or OAUTH
    #     """
    #     account = Account(name="Test Account Check Constraint AUTH",
    #                       account_type="CALENDAR",
    #                       authentication_type='OTHER_AUTH',
    #                       provider="APPLE",
    #                       user_id=1,
    #                       client_id=None,
    #                       client_secret=None,
    #                       username=None,
    #                       password=None,
    #                       api_key="asglkjnefçnserosengpaoerh",
    #                       sync_frequency=1,
    #                       id=1)

    #     result = account.create()

    #     self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    # db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
