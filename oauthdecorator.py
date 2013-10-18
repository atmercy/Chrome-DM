#
# Setup OAuth2Decorator Class
#


def CreateDecorator(environment):
   'Creates the proper OAuth2Decorator for use with AppEngine'

   if environment = 'local':    #running locally to save on API calls
      return OAuth2Decorator(
         client_id='YOUR_CLIENT_ID_HERE',
         client_secret='YOU_CLIENT_SECRET_HERE',
         scope='https://www.googleapis.com/auth/admin.directory.device.chromeos')
   
   else:
      return OAuth2Decorator(
         client_id='YOUR_CLIENT_ID_HERE,
         client_secret='YOU_CLIENT_SECRET_HERE',
         scope='https://www.googleapis.com/auth/admin.directory.device.chromeos')
