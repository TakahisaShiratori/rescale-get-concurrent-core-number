import json
import os
import requests

target_software = os.environ["TARGET_SOFTWARE"]
active = "1"

# Get active jobs as a list

jobs = []
url = "https://{platform}/api/v2/jobs/?t={status}".format(platform=os.environ["RESCALE_PLATFORM"], status=active)

while True:

  raw_reply = requests.get(
    url,
    headers={"Authorization": "Token {apikey}".format(apikey=os.environ["RESCALE_API_KEY"])}
  )
  reply = json.loads(raw_reply.text)

  for job in reply["results"]:
    jobs.append(job)

  if reply["next"] == None:
    break

  url = "{next}&t={status}".format(next=reply["next"], status=active)

print("The number of active jobs: {number}".format(number=str(len(jobs))))

# Sum core numbers for the target software jobs

target_jobs = 0
core_number = 0

for job in jobs:

  url = "https://{platform}/api/v2/jobs/{jobid}".format(platform=os.environ["RESCALE_PLATFORM"], jobid=job["id"])

  if job["analysisNames"][0] == target_software:
    target_jobs += 1

    raw_reply = requests.get(
      url,
      headers={"Authorization": "Token {apikey}".format(apikey=os.environ["RESCALE_API_KEY"])}
    )
    reply = json.loads(raw_reply.text)

    core_number += reply["jobanalyses"][0]["hardware"]["coresPerSlot"]

print("The number of {software} jobs: {number}".format(software=target_software, number=str(target_jobs)))
print("The number of concurrent cores used for {software}: {number}".format(software=target_software, number=str(core_number)))

