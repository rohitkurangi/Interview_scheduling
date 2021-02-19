from django.db import models


# Create your models here.
class SchedulingMaster(models.Model):
    candidate_id = models.CharField(max_length=100, null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    job_code = models.CharField(max_length=100, null=True, blank=True)
    apply_position = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    interview_date = models.DateTimeField(null=True)
    time_slot = models.CharField(max_length=50,null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=True)
    def __str__(self):
        return "{0}".format(self.candidate_id)


class InterviewrMaster(models.Model):
    interviwer_id = models.CharField(max_length=100, null=True)
    interviwer_name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    available_date = models.DateTimeField(null=True)
    time_slot = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return "{0}".format(self.interviwer_id)




