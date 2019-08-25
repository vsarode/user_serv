#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=user_service.db.settings.local;
export PYHTONPATH=$pwd;
python user_service/conf/service_app.py
