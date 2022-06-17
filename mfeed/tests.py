from django.test import TestCase
from .models import Profile,Survey,Reports,User
# Create your tests here.
class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User(username='Benjamin')
        self.user.save()
        self.survey=Survey(Survey= self.user,name='moringa alumni ',organisation='Moringa',resp="20",quantity=50000.00, date="2022-06-16",action="done")
        self.survey.save_survey()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
    
    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >0)
    
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)