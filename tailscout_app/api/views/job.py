from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers import JobSerializer
from ...models import Job
import os
import shutil

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

        # Directory
        directory = str(new_job_id)

        # Parent Directory path
        parent_dir = "/home/pradum/PycharmProjects/djangoProject/tailscout-master/tailscout_app/"

        # Path
        path = os.path.join(parent_dir, directory)
        print(os.getcwd())
        try:
            os.makedirs(path, exist_ok=True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)

        print(os.getcwd())
        os.chdir("/home/pradum/PycharmProjects/djangoProject/tailscout-master/tailscout_app/")

        print(os.getcwd())

        files = ['genee.py', 'clustalo.py', 'phage_details.csv', 'jpred.pl','sequence_phages.fasta']
        for f in files:
            shutil.copy(f, f"{new_job_id}")
        print(os.getcwd())

        dname = os.path.dirname(__file__)
        fname1 = os.path.join(dname, f'../../{new_job_id}/genee.py')
        fname2 = os.path.join(dname, f'../../{new_job_id}/clustalo.py')
        fname3 = os.path.join(dname, f'../../{new_job_id}/jpred.pl')

        os.system(f"python {fname1} --bacteria {new_job_bacteria} --filename {new_job_id}")
        # new_job_id.fasta created
        new_job.status = "S1"
        print("Step 1 done.")
        new_job.save()

        files = [f'{new_job_id}.fasta']
        for f in files:
            shutil.copy(f, f"{new_job_id}")

        os.system(f"python {fname2} --email {new_job_email_id} --sequence {new_job_id}")
        # new_job_id_ABC.fasta created
        new_job.status = "S2"
        print("Step 2 done!")
        new_job.save()

        if bacteria == "acinetobacter":
            file = open(f"{new_job_id}a.fasta", "w+")
            L = [">MTTNTPKYGGLLTDIGAAALATASAAGKKWQPTHMLIGDAGGAPGDTPDPLPSAA" + "\n" + "QKSLINQRHRAQLNRLFVSDKNANTLVAEVVLPVEVGGFWIREIGLQDADGKFVAVSNCP" + "\n" + "PSYKAAMESGSARTQTIRVNIALSGLENVQLLIDNGIIYATQDWVKEKVAADFKGRKILAGNGLLG" + "\n" + "GGDLSADRSIGLAPSGVTAGSYRSVTVNANGVVTQGSNPTTLAGYAIGDAYTKADTDGKLAQKANKATTL" + "\n" +  "AGYGITDALRVDGNAVSSSRLAAPRSLAASGDASWSVTFDGSANVSAPLSLSATGVAAGSYPKVTVDTKGRVTA" + "\n" + "GMALAATDIPGLDASKLVSGVLAEQRLPVFARGLATAVSNSSDPNTATVPLMLTNHANGPVAGRYFYIQS" + "\n" + "MFYPDQNGNASQIATSYNATSEMYVRVSYAANPSIREWLPWQRCDIGGSFTKEADGELPGGVNLDSMVTSG" + "\n" + "WWSQSFTAQAASGANYPIVRAGLLHVYAASSNFIYQTYQAYDGESFYFRCRHSNTWFPWRRMWHGGDFNPSDYL" + "\n" + "LKSGFYWNALPGKPATFIPTATSTTAGITKVLNVLNSNDVGSALSAAQGKVLNDKFNFQNSKNQSGYVRLGDSGLIIQ" + "\n" + "WGVFTSTKTQSNLIFPLAFPNALLSITGNLNSNTPDVIGIDFDLSTATKTSIKTGAAQVGASWLSGKKISWIAIGY" ]
            file.writelines(L)
            file.close()

        files = [f'{new_job_id}a.fasta']
        for f in files:
            shutil.copy(f, f"{new_job_id}")

        os.system(f"perl {fname3} submit file={new_job_id}a.fasta mode=batch format=fasta email={new_job_email_id} ")
        new_job.status = "S3"
        print("Step 3 done!")
        new_job.save()

        return Response(
                {'message': 'Data entered!'},
                status=status.HTTP_200_OK
        )
