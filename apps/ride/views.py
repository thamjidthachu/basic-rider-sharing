from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ride
from .serializer import RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['put'])
    def start_ride(self, request, pk=None):
        ride = self.get_object()
        if ride.status == 'requested':
            ride.status = 'started'
            ride.save()
            return Response({'message': 'Ride started successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ride cannot be started. Current status: {}'.format(ride.status)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def complete_ride(self, request, pk=None):
        ride = self.get_object()
        if ride.status == 'started':
            ride.status = 'completed'
            ride.save()
            return Response({'message': 'Ride completed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ride cannot be completed. Current status: {}'.format(ride.status)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def cancel_ride(self, request, pk=None):
        ride = self.get_object()
        if ride.status in ['requested', 'accepted']:
            ride.status = 'cancelled'
            ride.save()
            return Response({'message': 'Ride cancelled successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ride cannot be cancelled. Current status: {}'.format(ride.status)},
                            status=status.HTTP_400_BAD_REQUEST)
