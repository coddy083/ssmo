from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from holiday.models import HolliyDay
from holiday.serializers import HolidaySerializer

class HolidayView(APIView):
    def get(self, request):
        holiday = HolliyDay.objects.all()
        serializer = HolidaySerializer(holiday, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            holiday = HolliyDay.objects.get(date=request.data['date'])
            holiday.hours = request.data['hours']
            holiday.save()
            serializer = HolidaySerializer(holiday)
            return Response(serializer.data)
        except HolliyDay.DoesNotExist:
            serializer = HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        

        