from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        """Ensure we can create a Task and it saves correctly"""
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)  # default should be False


class TaskViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Initial Task")

    def test_index_view_status_code(self):
        """Check if index page loads successfully"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Task")

    def test_add_task(self):
        """Check if new task can be added via POST"""
        response = self.client.post(reverse("add_task"), {"title": "New Task"})
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    def test_delete_task(self):
        """Check if a task can be deleted"""
        task_id = self.task.id
        response = self.client.get(reverse("delete_task", args=[task_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task_id).exists())

