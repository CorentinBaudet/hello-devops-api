#!/bin/bash

helm uninstall hello-devops-api
git pull
helm install hello-devops-api .