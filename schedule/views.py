from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from schedule.core.utility import error_response, encrypt_data, decrypted_data, ok_response
from schedule.models import SchedulingMaster, InterviewrMaster
import datetime


@api_view(['POST'])
def scheduling(request):
    json_data = request.data
    job_code=json_data.get("job_code")
    apply_position=json_data.get("apply_position")
    description=json_data.get("description")
    position=json_data.get("position")

    # common fields
    fullname=json_data.get("fullname")
    relavent_to=json_data.get("relavent_to")
    time_slot=json_data.get("time_slot")
    interview_date=json_data.get("interview_date")


    if relavent_to not in ["candidate","interviewer"]:
        return error_response(code=406,message="invalid relevent")
    try:
        date_time_obj = datetime.strptime(interview_date, '%Y-%m-%d')
    except Exception as e:
        print(e)
        return error_response(code=406,message="date must be proper format")

    if relavent_to == "candidate":
        interview_sch={"fullname":fullname,"job_code":job_code,"apply_position":apply_position,"description":description,
                        "interview_date":date_time_obj,"time_slot":time_slot}
        obj_candidate=SchedulingMaster.objects.create(**interview_sch)
        concat_id = "can_"+ str(obj_candidate.id) + interview_date
        unique_id=encrypt_data(concat_id)
        obj_candidate.candidate_id = unique_id
        obj_candidate.save()
        return  ok_response(message="candidate register successfully")
    elif relavent_to == "interviewer":
        interview_sch = {"interviwer_name": fullname,
                         "available_date": date_time_obj, "time_slot": time_slot, "position": position}
        obj_interviewr = InterviewrMaster.objects.create(**interview_sch)
        concat_id = "inter_" + str(obj_interviewr.id) + interview_date
        unique_id=encrypt_data(concat_id)
        obj_interviewr.interviwer_id = unique_id
        obj_interviewr.save()
        return ok_response(message="interviewr register successfully")

    else:
        return error_response(code=406,message="relavent is missmatch")


@api_view(['POST'])
def time_slot_matching(request):
    json_data = request.data
    candidate_id = json_data.get("candidate_id")
    interviewr_id = json_data.get("interviewr_id")
    if candidate_id == None:
        is_interviewr = True
        mydict={"interviwer_id":interviewr_id}
        commanmodel=InterviewrMaster
    else:
        mydict={"candidate_id":candidate_id}
        is_interviewr = False
        commanmodel= SchedulingMaster

    try:
        checkslot=commanmodel.objects.get(**mydict)
    except:
        return error_response(code=406,message="wrong id")


    if is_interviewr:
        actual_datw=str(checkslot.available_date.date())
        check_scheduling=SchedulingMaster.objects.filter(interview_date__range=[actual_datw,actual_datw])
        if not check_scheduling.exists():
            return error_response(message="no interview scheduled")
        set_hours_start = datetime.now()
        val1 = set_hours_start.replace(hour=9,tzinfo=None)
        val2 = set_hours_start.replace(hour=18,tzinfo=None)
        hours = (val1, val2)
        userslotlist=[]
        for data in check_scheduling:
            userslotdict=()
            time = data.time_slot
            start_time=time[:1]
            end_time=time[-1]
            start_date_time=data.interview_date.replace(hour=int(start_time),tzinfo=None)
            end_date_time=data.interview_date.replace(hour=int(end_time),tzinfo=None)
            userslotdict=(start_date_time,end_date_time)
            userslotlist.append(userslotdict)
        print(userslotlist)
        logging.info(userslotlist, "djddjndjn")
        val=get_slots(hours, userslotlist, check_scheduling,duration=timedelta(hours=1))
        return ok_response(data=val,message="sloat is ready")

from datetime import datetime, timedelta
import logging
def get_slots(hours, appointments,check_scheduling, duration=timedelta(hours=1)):
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    for start, end in ((slots[i][0], slots[i + 1][1]) for i in range(len(slots) - 1)):
        logging.info(start,end,"djddjndjn")
        assert start <= end, "Cannot attend all appointments"
        demolist=[]
        while start + duration <= end:
            mydict=dict()
            mydict={"time_slot":"{:%H:%M} - {:%H:%M}".format(start, start + duration),"candidate_name":None,"candidate_id":None}
            start += duration
            demolist.append(mydict)
        print(demolist)
        for can_name,time_slot in zip(check_scheduling,demolist):
            time_slot["candidate_id"] = can_name.candidate_id
            time_slot["candidate_name"] =can_name.fullname

        return demolist
