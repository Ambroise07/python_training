#coding:utf-8
#-------------------------------------------------------------------------------------------------------------#
#--------------------------------------------Facebook Bot-----------------------------------------------------#
import sys, os, time, requests, json

if sys.platform in ["linux", "linux2"] :
    clear = "clear"
    R = "\033[31;1m"
    V = "\033[32;1m"
    B = "\033[0m"
    C = "\033[36;1m"
    J = '\033[93m'
    M = '\033[94m'
else :
    R = ""
    V = ""
    B = ""
    C = ""
    J = ""
    M = ""
    clear = "cls"
class FacebookBot():
    def __init__(self):
        pass

