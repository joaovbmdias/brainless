import providers.apple as apple
import providers.google as google
import providers.doist as doist
import constants as const

def get_apple_data(client_id, client_secret, account_type):
    return apple.get_data(client_id, client_secret, account_type)

def get_google_data(client_id, client_secret, account_type):
    pass

def get_doist_data(client_id, client_secret, account_type):
    pass

providers_mapping = {const.CONST_APPLE: get_apple_data,
                     const.CONST_GOOGLE: get_google_data,
                     const.CONST_GOOGLE: get_doist_data
                     }

def get_data(provider, client_id, client_secret, account_type):
    return providers_mapping[provider](client_id, client_secret, account_type)