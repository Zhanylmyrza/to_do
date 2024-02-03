from django.shortcuts import render
from serializer import TaskSerializer

class MyTasksView:
  serializer_class = TaskSerializer
    
  @api_view(['GET'])
  def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(products, many=True)
    return Response(serializer.data)
  
  
  @api_view(['GET'])
  def getTask(request, pk):
    task = Task.objects.get(_id=pk)
    serializer = TaskSerializer(product, many=False)
    
    return Response(serializer.data)
    