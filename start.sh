#!/usr/bin/env bash
export PYTHONPATH=$pwd;
export DJANGO_SETTINGS_MODULE=user_service.db.settings.local;
python user_service/conf/service_app.py
