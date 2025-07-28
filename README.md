# ncas-cam-12-software 

## Overview of the repo

This repository contains scripts for the ncas-cam-12 automated camera system. The system is designed to capture images at regular intervals to support the study of cloud formations. All scripts are located in the /opt/scripts directory on the camera's onboard computer and are deployed as part of the Ansible installation process.

### Scripts overview 

`capture-photos.sh`

A script that simply captures images at a desired interval making use of GNU Gphoto2 

`capture-photos-with-ncas-image-standard-naming.sh`

A script to capture images and name them using the the ncas image standard 

`teamx_plose_template_photo.yaml`

An example template file to tag the image with extra metadata required for the [ncas image standard](https://datahelp.ncas.ac.uk/article/5170-quick-guide-b-ncas-image) 
