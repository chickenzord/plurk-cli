import plurkenv

plurk = plurkenv.init()

def _call(path, key = None,  params = {}):
  response = plurk.callAPI(path, params)
  if response is None:
    raise Exception("Request failed")
  elif key is None:
    return response
  elif key in response:
    return response[key]
  else:
    raise Exception("%s key not found" % key)

def whois(user_id = None):
  if user_id:
    return _call('/APP/Profile/getPublicProfile', 'user_info', { 'user_id': user_id})
  else:
    return _call('/APP/Profile/getOwnProfile', 'user_info')

def update_profile(display_name = None, full_name = None):
  params = dict()
  if display_name: params['display_name'] = display_name
  if full_name: params['full_name'] = full_name

  json = _call('/APP/Users/update', 'user', params)
  return {
    'display_name': json['display_name'],
    'full_name': json['full_name']
  }
