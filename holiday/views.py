from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from holiday.models import HolliyDay
from holiday.serializers import HolidaySerializer
from django.db.models import Q

class HolidayView(APIView):
    def get(self, request):
        holiday = HolliyDay.objects.filter(user=request.user)
        serializer = HolidaySerializer(holiday, many=True)
        return Response(serializer.data)

    def post(self, request):
        holiday = Q(user=request.user) & Q(date=request.data['date'])            
        if len(HolliyDay.objects.filter(holiday)) != 0:
            holiday = HolliyDay.objects.filter(holiday)
            holiday = holiday.last()
            holiday.hours = request.data['hours']
            holiday.save()
            serializer = HolidaySerializer(holiday)
            return Response(serializer.data, status=status.HTTP_200_OK)
        request.data['user'] = request.user.id
        serializer = HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        holiday = Q(user=request.user) & Q(date=request.data['date'])            
        holiday = HolliyDay.objects.filter(holiday)
        holiday = holiday.last()
        serializer = HolidaySerializer(holiday, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        holiday = HolliyDay.objects.filter(user=request.user)
        holiday.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

        