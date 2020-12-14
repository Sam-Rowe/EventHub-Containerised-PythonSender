FROM python:3.9
RUN pip install azure-eventhub
RUN pip install azure-eventhub-checkpointstoreblob-aio
RUN pip install Faker
COPY send.py /root/send.py
ENV EVENT_HUB_CONN_STR=Endpoint=sb://YOUREVENTHUB.servicebus.windows.net/;SharedAccessKeyName=KEYNAME;SharedAccessKey=KEYGOESHERE;EntityPath=HUBNAME
ENV EVENT_HUB_NAME=YOURHUBNAME
ENTRYPOINT ["python","/root/send.py"]