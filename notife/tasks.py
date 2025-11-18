from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Todo
from celery import current_app

@shared_task(bind=True)
def send_todo_reminder(self, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        send_mail(
            subject=f'Reminder: {todo.title}',
            message=f'Your todo: {todo.title}\nDetails: {todo.info}',
            from_email=None,  # از DEFAULT_FROM_EMAIL استفاده می‌کند
            recipient_list=[todo.owner.email],
        )
    except Todo.DoesNotExist:
        pass
