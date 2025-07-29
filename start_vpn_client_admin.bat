@echo off
cd /d "C:\Users\packh\Desktop\hacker\vpn"
powershell -Command "Start-Process python -ArgumentList 'vpn_client_gui.py' -Verb RunAs"
