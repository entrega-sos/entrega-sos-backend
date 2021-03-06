#!/bin/bash

while true; do
    python manage.py db migrate
    python manage.py db upgrade

    if [[ "$?" == "0" ]]; then
        break
    fi

    echo "Initialization failed, retrying in 5 seconds..."
    sleep 5
done

exec gunicorn --workers=4 --bind 0.0.0.0:80 wsgi:app --reload --access-logfile - --error-logfile - --timeout 120 --keep-alive 30