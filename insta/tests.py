from django.test import TestCase
from .models import Image,Followers,Following,Profile,User

class InstaTestClass(TestCase):
    def setUp(self):
        self.user = User(id =1, username = "Umar", email = "b@gmail.com", password = "p123")
        self.user.save()
        self.image = Image(comments = "wow",image_caption = "Hey nice",user = self.user, location = "msa",image = "images/pip.jpg")
        self.image.save()
        self.profile = Profile(id=1,first_name = "Umar", last_name = "Ngare", name = self.user, bio = "life is good", profile_pic = "image/one.jpg")
        self.profile.save()
    
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.user,User))
    
    def test_save_class(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    def test_delete_method(self):
        '''
        tests to check the deleting functionality
        '''
        # profile
        self.profile.save_profile()
        info = Profile.objects.all()
        Profile.delete_profile(info)
        prof = Profile.objects.all()
        self.assertTrue(len(prof) == 0)

        # image
        self.image.save_image()
        images = Image.objects.all()
        Image.delete_image(images)
        ima = Image.objects.all()
        self.assertTrue(len(ima)== 0)

    def test_get_methods(self):
        '''
        tests to check if get methods work.
        '''
        self.image.save_image()
        all_images = Image.get_images()
        self.assertTrue(len(all_images) > 0)

        # test for profile get method

        self.profile.save_profile()
        all_profile = Profile.get_profiles()
        self.assertTrue(len(all_profile) > 0)
    
    def test_by_id_methods(self):
        '''
        test to check proper functionality of the get by id functions.
        '''
        self.image.save_image()
        found_image = Image.get_image_by_id(1)
        self.assertEqual(found_image.id,1)

        # profile test
        self.profile.save_profile()
        found_profile = Profile.get_profile_by_id(1)
        self.assertEqual(found_profile.id,1)
    
    def test_search_by_username(self):
        self.profile.save_profile()
        sought_profile = Profile.search_profile("Umar")
        self.assertEqual(sought_profile.name.username,"Umar")