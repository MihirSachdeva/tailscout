from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers import JobSerializer
from ...models import Job
import os

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def create(self, request):
        bacteria = self.request.data.get("bacteria")
        email_id = self.request.data.get("email_id")
        new_job = Job.objects.create(
            bacteria=bacteria,
            email_id=email_id
        )
        new_job.save()
        new_job_id = new_job.id
        new_job_bacteria = new_job.bacteria
        new_job_email_id = new_job.email_id

        os.system(f"python /home/mihir/Desktop/tailscout/tailscout/tailscout_app/genee.py --bacteria {new_job_bacteria} --filename {new_job_id}")
        # new_job_id.fasta created
        new_job.status = "S1"
        print("Step 1 done.")
        new_job.save()


        # os.system => clustalo, give new_job_id.fasta and new_job.email_id
        # new_job_id_ABC.fasta created
        # new_job.status = "S2"
        # new_job.save()


        # os.system => jpred, give new_job_id_ABC.fasta and new_job.email_id4
        # new_job.status = "S3"
        # new_job.save()

        return Response(
                {'message': 'Data entered!'},
                status=status.HTTP_200_OK
        )
