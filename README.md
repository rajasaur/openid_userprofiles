This is an example of using the following django applications:

* django-openid-auth ( https://launchpad.net/django-openid-auth)
* python-openid (used internally by django-openid-auth) 
* django-profiles for User profile management. (https://bitbucket.org/ubernostrum/django-profiles/)

The django-openid-auth is used along with openid-selector (http://code.google.com/p/openid-selector/) to display a nice UI for the user to select a OpenID Provider.

### Changes made ###
1. Modified django-openid-auth's templates to include openid-selector so you get a nice ui that has the icons for various openid providers.
2. Manipulated django-profiles so that once a openid is done for a user, you have the ability to add/edit profiles. The application will allow you to create a UserProfile if one is not found and edit it if its found. The UserProfile in this example contains 2 fields (favourite_pet and favourite_number).

### Trying out the example ###

1. git clone git://github.com/rajasaur/openid_userprofiles.git
2. This is much easier done if you are using pip as Ive packaged the above dependencies using pip. If you are using pip, just do a
    pip install -f requirements.txt
3. python manage.py syncdb # to build the built-in sqlite schema
4. python manage.py runserver
5. Enjoy!

### Application Screens ###
Try logging into http://localhost:8000. This should take you to a openid selector screen where you can select a openid. Once you are authenticated, you will be redirected to a front page where you can create/edit your profile. Completing the form (which has a validation to accept 4 or greater digits for favourite_number) should take you to a profile detail page where some details are displayed.

### Credits ###

Credits go to the authors of the following packages

* Django
* django-openid-auth
* python-openid
* django-profiles
* openid-selector
