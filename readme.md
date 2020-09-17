# Example of simple flask on Docker

This is a very very simple flask application and a docker file with instructions for running flask on docker.   This is not a tutorial for docker or flask or python or anything else.  It's just an working example to learn from or to start from.  

These instructions are command line based and only tested on MacOS. 

## testing without Docker

### get some Python
If you already have python installed you can skip this step
 
you need to be able to run the flask app on your own computer to ensure it runs.   You may use any python you like, but Anaconda seems easy. 

1. install miniconda version 3.   The full Anaconda  has hundreds of package and we just need  few
1. create a new environment.  
     If you are using Conda, then use conda environments.   environments must be named, and I usually use the same name as my app.  Substitute your app name for the 'simpleflask' name  I'm using here


```
conda create -n  simpleflask pip   # installs pip for this env, say 'y' when it asks
conda activate simpleflask
pip install -r requirements.txt
```


### test flask

if you have Python + flask installed, then in this folder test that flask will run this application

```
FLASK_APP=app.py flask run
```

open http://127.0.0.1:5000/  which should just be one page, with a message 'hello from flask' and a nice movie of a mountain (unless the nice people who are hosting that movie have moved it since we cretaed this repository ) 

Good?  Close this app (in Mac/Linux hit ctrl+c in the termianl window to stop the dev server) Then next step.  Not good?  check your python install, or other steps to get flask running.   You could try using docker anyway (as that has a python setup already)


## Dockerize

### get some Docker

I recommend docker destop which unless versions in 2019 or earlier, really didn't work well on Mac or Windows and used to require virtual box.   

After installing docker desktop, Docker needs to be running in the background, which is will be if you've install it correctly.   

### Build a docker image

If docker is installed and running then you can use the following command to build.  I use the image name based on the application name.  Substitute your app name for the 'simpleflask' name  I'm using here

```
docker build --tag simpleflask:latest .
```


This docker file is based on a smaller version of Docker-supplied python built on debiean but works fine for us.  The full version of python is huge. 

Another important difference in the Dockerfile that you don't need when testing on your computer, is the "host" flag which must be set to "0.0.0.0" so that flask will listen to all ports and not just 'localhost' 

A quick note about Docker 'tags' and the 'latest' tags.    Many docker repositories using the tag 'latest' and there is nothing special or magic about that.  Those devs have to create that manually.         Since 'latest' is a prevelant convention I just use it for every build and do not use any version number tags.   For this tiny example, I'm not using versioning because ... why?  No one will every want an earlier version of this (because it is probablhy broken). 

### Run the image (which creates a container)

```
docker run -d --name simpleflask -p 5000:5000 simpleflask:latest
```

Again, change `simpleflask` with your app name. 


The command will run and seem to exit with no output if it ran correctly.   Is it running?  Use `docker ps` to see if it's there. 


Now open it up on your laptops browser  http://127.0.0.1:5000  

it is running ?  

### clean up

Stop the server with `docker stop simpleflask`

You can remove the container if you need to modify anything and re-build with 

```
docker container rm simpleflask
docker rmi simpleflask:latest

```

## Next, To Do

  * For production you'll want to use a webserver not the flask dev server.  Gunicorn is a good idea.    You'll need to add that to the requirements.txt and modify the ENTRYPOINT.  Gunicorn runs on port 8000

  * try changing the port to 80 if your rlaptop allows it (may need sudo or to run as administrator)

  * install support libraries.   This version of python runs on the Debian OS (which is what Ubuntu is based on).  To install libraries in the Docker image add something like the following to your Dockerfile (this example installs Pandoc for converting doc formats)
 
```
    RUN apt-get update \
        && apt-get install -y  libxext6 libsm6 libxrender1 curl libglib2.0-0 dialog pandoc \
        && apt-get clean
```
