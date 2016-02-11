## Django
****
`pip3 install django`

`django-admin startproject myproject`
 - Initialized django and scaffolds basic app

`python3 manage.py runserver 0.0.0.0:8000`
 - starts the server on any host at port 8000

`python3 manage.py migrate`
 - migrates the prebuilt auth data to our project

*make views.py*

`from django.http import HttpResponse`

```
def hello_world(request):
    return HttpResponse('Hello World')

```

To link the view, in urls.py

`from . import views`

```
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.hello_world)
]
```

### Creating Apps

`python3 manage.py startapp courses`
 - Makes an app named courses
 - In settings.py add courses to INSTALLED_APPS
 - change relevant time zone too

In models.py in courses, we make our first model:

```
class Course(models.Model):
    created_at = models.DateTimeField(`auto_now_add=True`)
    title = models.CharField(max_length=255)
    description = models.TextField()


```

`python3 manage.py makemigrations courses`
 - sets up the new data to be migrated

`python3 manage.py migrate courses`
 - adds the new model data to our app, i.e. migrates


## Django shell

`python3 manage.py shell`
`from courses.models import Course`
 - starts the shell and imports our model

`Course.objects.all()`
 - gets all items of the Course Model

```
c = Course()
c.title = "Python Basics"
c.description = "Learn the basics of Python"
c.save()
```
 - Creates a new course, add attributes, and uses .save() to save it

`Course(title="Course Name", description="Course Description").save()`
`Course.objects.create(title="Course Name", description="Course Description")`
 - Both of these also make new Courses and save them




### Filters
****

`{{ course.step_set | join:", " }}`
 - joins together like an array

`{{ course.step_set | length }}`
 - gives the length, .count is better

`{{ course.step_set | pluralize }}`
 - returns an s if the count of the thing is greater than 1

add `'django.contrib.humanize',` to settings under INSTALLED_APPS
`{% load humanize %}`
`{{ course.step_set.count | apnumber }}`
 - returns number words for 1-9, then digits after that

`{{ course.step_set | unordered_list }}`
 - prints as an unordered list

`{{ course.description | truncatewords:5 }}`
 - cuts string off at 5 words, adds ...

`{{ course.created_at | date:"F j, Y"}}`
 - Returns February 5, 2016. "m/d/y" returns 02/05/16

`{{ email|urlize }}`
 - returns an anchor tag with the email as the link and the text, mailto if email