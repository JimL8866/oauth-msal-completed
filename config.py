class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "HkR8Q~XRPr_IdENU_ia-tFaBCWZ2yObOOPsr~bK-" 

    #AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    AUTHORITY = "https://login.microsoftonline.com/d5fc14ea-8b7a-414d-89be-b7bf0dcd41a8"  #Tenant ID

    # TODO: Enter your application client ID here
    CLIENT_ID = "5b6678e0-298d-44e5-a3be-19998afbce5f"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD
        
    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session