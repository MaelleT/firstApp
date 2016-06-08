'''
Created on 8 juin 2016

@author: maelle
'''
import datetime
from django.utils import timezone
from .models import Question
from django.test import TestCase
from django.core.urlresolvers import reverse


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
        
        
        
        
def create_question(question_text,days):
    '''
    Creates a question with the given question_text and published givne number of days
    '''
    time=timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class TestQuestionViewNoQuestions(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        
    def tearDown(self):
        TestCase.tearDown(self)
    
    def testQuestionView_with_no_questions(self):
        '''
        If no questions exist, an appropriate message should be displayed
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
        
class TestQuestionViewPastQuestion(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        create_question(question_text="Past Question.", days=-30)
        
    def tearDown(self):
        TestCase.tearDown(self)
    
    def testQuestionView_with_past_question(self):
        '''
        Question with a pub_date in the past should be displayed on the index page
        '''
        response = self.client.get(reverse('polls:index'))
       
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question.>'])
        
class TestQuestionViewFutureQuestion(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        create_question(question_text="Future Question.", days=30)
        
    def tearDown(self):
        TestCase.tearDown(self)
    
    def testQuestionView_with_future_question(self):
        '''
        Question with a pub_date in the past should be displayed on the index page
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response,"No polls are available.",status_code=200)

        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    
class TestQuestionViewFutureAndPastQuestion(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        create_question(question_text="Future Question.", days=30)
        create_question(question_text="Past Question.", days=-30)

    def tearDown(self):
        TestCase.tearDown(self)
    
    def testQuestionView_with_future_and_past_question(self):
        '''
        Question with a pub_date in the past should be displayed on the index page
        '''
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(response.context['latest_question_list'],  ['<Question: Past Question.>'])

class TestQuestionViewWithTwoPastQuestion(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        create_question(question_text="Past Question 1.", days=-40)
        create_question(question_text="Past Question 2.", days=-30)

    def tearDown(self):
        TestCase.tearDown(self)
    
    def testQuestionView_with_two_past_question(self):
        '''
        Question with a pub_date in the past should be displayed on the index page
        '''
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(response.context['latest_question_list'],  ['<Question: Past Question 2.>','<Question: Past Question 1.>'])

        
        
        
            