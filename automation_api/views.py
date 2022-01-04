from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_202_ACCEPTED
from rest_framework.views import APIView
from .tasks import create_task
from celery.result import AsyncResult


class CreateTaskView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        automation_id = request.data.get('automation_id')
        automation_arguments = request.data.get('arguments')
        task = create_task.delay(automation_id, **automation_arguments)
        response = {
            'task_id': task.id
        }
        return Response(response, HTTP_202_ACCEPTED)


class GetTaskView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        result = {
            'task_id': task_id,
            'task_status': task_result.status,
            'task_result': task_result.result
        }
        return Response(result, HTTP_200_OK)
