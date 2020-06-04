import providers.apple as apple
import providers.google as google
import providers.doist as doist
import constants as const

def get_apple_data(authentication_data):
    return apple.get_data(authentication_data['username'], authentication_data['password'], authentication_data['account_type'])

def get_google_data(authentication_data):
    pass

def get_doist_data(authentication_data):
    return doist.get_data(authentication_data['api_token'])

providers_mapping = {const.APPLE: get_apple_data,
                     const.GOOGLE: get_google_data,
                     const.DOIST: get_doist_data
                     }

def get_data(authentication_data):
    return providers_mapping[authentication_data['provider']](authentication_data)