'''
Created on 8 juin 2016

@author: maelle
'''
import datetime
from django.utils import timezone
from .models import Question
from django.test import TestCase

class QuestionMethodTests(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        time = timezone.now()+ datetime.timedelta(days=30)
        self.future_question=Question(pub_date=time)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_was_published_with_future_question(self):
       
        self.assertEqual(self.future_question.was_published(), False,"Erreur : question with future pub_date")