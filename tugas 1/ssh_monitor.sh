#!/bin/bash

while true; do
   if systemctl is-active --quiet ssh; then
       echo "$(date): SSH service is running"
   else
       echo "$(date): SSH service is DOWN - Starting SSH service"
       systemctl start ssh
   fi
   sleep 10
done

