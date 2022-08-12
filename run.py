import os, sys
try:
    __import__("IGPRO").menu_apikey()
except Exception as e:
    exit(str(e))