"""Tests for the API app."""

from http import HTTPStatus

from django.test import Client, TestCase

from .models import Task


class TaskAPITestCase(TestCase):
    """Tests for Task API endpoints."""

    def setUp(self):
        """Create a test client."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Check that the task list endpoint is available."""
        response = self.guest_client.get("/api/tasks/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Check that a task can be created via the API."""
        data = {"title": "Test", "description": "Test"}
        response = self.guest_client.post("/api/tasks/", data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(Task.objects.filter(title="Test").exists())
