#Interview_scheduling

### create python3 virtual env
1) python3 -m venv env
   
###install packages in virtual env.
2)  pip3 install -r requirement.txt 
  
###activete virtual env.

3)source /home/venu/bin/activate

###enter the project using cd command  
4) cd Interview_scheduling

### run the python project
python manage.py runserver 0:8000

we create two api,s for 
1)register the candidate and interviver
2)get time sloat for hr-manager 


1)register candidate and interviwer
```json
localhost:8000/api/register_interview_shceduling
```

Request body  for candidate
```json
{
"fullname":"rohit mehta",
"job_code":"T0050",
"apply_position":"python developer",
"interview_date":"2021-02-19",
"time_slot":"12-2",
"relavent_to":"candidate"
}
```
Response body
```json
{
    "data": {
        "Candidate_unique_id": "can_b'UiBYn10jqOzvzQ6yKcRLrw=='"
    },
    "message": "candidate register successfully",
    "status": true
}
```

Request body for Interviver
```json
{
"fullname":"rohit mehta",
"interview_date":"2021-02-19",
"time_slot":"12-4",
"relavent_to":"interviewer",
"position":"sr.python developer"
}
```

Response body 
```json
{
    "data": {
        "Interviwer_unique_id": "Inter_b'wWYmgghUAsqvCmNqxbvxLQ=='"
    },
    "message": "interviewr register successfully",
    "status": true
}
```


# Time Slot Matching Api
### this api for scheduling the interview time for available candidate in single day
```json
localhost:8000/api/time_slot_matching/
```

Request body
```json
{
"interviewr_id":"Inter_b'X4E4CtV2UuA3wqhN3mMX+w=='"

}
```

Response Body
```json
{
    "data": [
        {
            "time_slot": "09:11 - 10:11",
            "candidate_name": "rakesh mane",
            "candidate_id": "can_b'hyvZ2JpZos6tyZtc4emeBA=='"
        },
        {
            "time_slot": "10:11 - 11:11",
            "candidate_name": "milan powar",
            "candidate_id": "can_b'qsCHh1ug/lZGDGLqJfyGZg=='"
        },
        {
            "time_slot": "11:11 - 12:11",
            "candidate_name": "moahn mehara",
            "candidate_id": "can_b'vQ5XdN02oAc2euCJZkr6aw=='"
        }
    ],
    "message": "sloat is ready",
    "status": true
}
```