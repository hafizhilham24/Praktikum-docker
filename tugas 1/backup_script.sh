#!/bin/bash

while true; do
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BACKUP_FILE="backup_music_$TIMESTAMP.tar.gz"
    
    # Backup direktori Music ke direktori backup
    tar -czf backup/$BACKUP_FILE Music/
    echo "$(date): Music backup created: $BACKUP_FILE"
    
    # Hapus backup yang lebih dari 10 file
    cd backup
    ls -t backup_music_*.tar.gz 2>/dev/null | tail -n +11 | xargs -r rm
    cd ..
    echo "$(date): Old music backups cleaned"
    
    sleep 15
done
