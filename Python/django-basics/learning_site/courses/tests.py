from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Course, Step
from . import views


class CourseModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in python")

    def test_course_creation(self):
        now = timezone.now()
        self.assertLess(self.course.created_at, now)

    def test_course_dunder_str(self):
        self.assertEqual(str(self.course), "Python Regular Expressions")


class StepModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to test in python.")
        self.step = Step.objects.create(
            title="Unit Test",
            description="Learn to use the unittest library",
            course=self.course)

    def test_step_creation(self):
        self.assertEqual(self.step.order, 0)
        self.assertEqual(self.step.content, "")

    def test_step_link(self):
        self.assertEqual(self.step.course, self.course)

    def test_step_dunder_str(self):
        self.assertEqual(str(self.step), "Unit Test")


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in python.")
        self.course2 = Course.objects.create(
            title="New Python Course",
            description="In development.")
        self.step = Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your doc strings.",
            course=self.course)
        self.step2 = Step.objects.create(
            title="More Doctests to come",
            description="Learn to write awesomer tests in your doc strings.",
            course=self.course2)

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={
            'pk':self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])
        self.assertNotEqual(self.course2, resp.context['course'])
        self.assertIn(self.step, resp.context['course'].step_set.all())
        self.assertNotIn(self.step2, resp.context['course'].step_set.all())
        self.assertTemplateUsed(resp, 'courses/course_detail.html')
        self.assertContains(resp, self.course.title)

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={
            'course_pk': self.step.course.pk, 'step_pk': self.step.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])
        self.assertNotEqual(self.step2, resp.context['step'])
        self.assertTemplateUsed(resp, 'courses/step_detail.html')
        self.assertContains(resp, self.step.title)
