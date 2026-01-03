from django.test import TestCase
from .models import Blog 
# Create your tests here.
class blogtest(TestCase) : 
    @classmethod 
    def setUpTestData(cls) :  # yo function name chai yei nai huna parxah django leh call garna lae
        Blog.objects.create(title="hello",description="this is test case.",body="this is body of blog test.")  

    def test_title(self) : 
        blog = Blog.objects.get(id=1) 
        expected_title = f'{blog.title}'
        self.assertEqual(expected_title , "hello") 

