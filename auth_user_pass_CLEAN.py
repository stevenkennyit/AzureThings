import adal

class Authentication():
	def __init__(self, username='USER@EMAIL.COM', password='passwordhere', tenant='tenantid-here', client_id='1b730954-1685-4b74-9bfd-dac224a7b894'):
			self.username = username
			self.password = password
			self.tenant = tenant
			self.client_id = client_id
			self.resource_uri = 'https://graph.windows.net/'
			self.tokendata = {}
			self.refresh_token = None
			self.access_token = None
			self.proxies = None
			self.verify = True
			self.outfile = None
			self.debug = False


	def get_authority_url(self):
			"""
			Returns the authority URL for the tenant specified, or the
			common one if no tenant was specified
			"""
			if self.tenant is not None:
					return 'https://login.microsoftonline.com/{}'.format(self.tenant)
			return 'https://login.microsoftonline.com/common'


	def authenticate_username_password(self):
			"""
			Authenticate using user w/ username + password.
			This doesn't work for users or tenants that have multi-factor authentication required.
			"""
			authority_uri = self.get_authority_url()
			context = adal.AuthenticationContext(authority_uri, api_version=None, proxies=self.proxies, verify_ssl=False)
			self.tokendata = context.acquire_token_with_username_password(self.resource_uri, self.username, self.password, self.client_id)

			return self.tokendata
 

def main():
    auth = Authentication()
    auth.authenticate_username_password()
        
if __name__ == '__main__':
    main()
