from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def showme(req):
    user = req.user
    action = 'edit'
    try:
        user.get_profile()
    except:
        action = 'create'
    return HttpResponse("User id is %s and name is %s. click <a href='/profiles/edit/'>Here</a> to %s profile" %(user.id, user.username, action))

