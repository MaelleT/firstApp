'''
Created on 8 juin 2016

@author: maelle
'''
import datetime
from django.utils import timezone
from .models import Question
from django.test import TestCase

class TestQuestionMethodFutur(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        time = timezone.now()+ datetime.timedelta(days=30)
        self.future_question=Question(pub_date=time)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_was_published_with_future_question(self):
       
        self.assertEqual(self.future_question.was_published(), False,"Erreur : question with future pub_date")
        
class TestQuestionMethodOld(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        time = timezone.now()- datetime.timedelta(days=30)
        self.old_question=Question(pub_date=time)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_was_published_with_old_question(self):
       
        self.assertEqual(self.old_question.was_published(), False,"Erreur : question with old pub_date")
        
class TestQuestionMethodRecent(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        time = timezone.now()- datetime.timedelta(hours=1)
        self.recent_question=Question(pub_date=time)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_was_published_with_recent_question(self):
       
        self.assertEqual(self.recent_question.was_published(), True,"Erreur : question with recent pub_date")
        
        