#to create a specific image
#execute from ubuntu image
FROM ubuntu 
FROM python
#explain root directory
WORKDIR /project
#add a file to the image
ADD README.md .
#run a command line
RUN pip install -r README.md

#give action to execute when prog is starting
ENTRYPOINT ["uvicorn"]

