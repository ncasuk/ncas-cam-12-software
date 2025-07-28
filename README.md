# ncas-cam-12-software 

## Overview of the repo

This repo contains scripts that run on the the ncas-cam-12 camera system. This is an automated camera system that is designed to take photos at a given 
inteval to allow for the study of cloud systems. These scripts are all present in the /opt/scripts directory on the camera computer and are deployed as part of the ansible install routine. 

### Scripts overview 

`capture-photos.sh`

A script that simply captures images at a desired interval making use of GNU Gphoto2 

`capture-photos-with-ncas-image-standard-naming.sh`

A script to capture images and name them using the the ncas image standard 

`teamx_plose_template_photo.yaml`

An example template file to tag the image with extra metadata required for the [ncas image standard](https://datahelp.ncas.ac.uk/article/5170-quick-guide-b-ncas-image) 
