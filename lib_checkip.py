#!/usr/bin/env python
# coding:UTF-8
import commands
import re
import netifaces

#print lib_checkip.check_v4_global()
#print lib_checkip.check_v6_global()
#print lib_checkip.check_v6_if("eth0")

def get_v4_global(op):
	if op == 0:
		cmd = "dig +short myip.opendns.com @resolver1.opendns.com"
		return commands.getoutput(cmd).strip()
	elif op == 1:
		cmd = "dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F'\"' '{ print $2}'"
		return commands.getoutput(cmd).strip()
	elif op == 2:
		cmd = "curl -s -4 checkip.dyndns.com | perl -ne '/IP Address: ([0-9.]+)/ && print $1'"
		return commands.getoutput(cmd).strip()
	elif op == 3:
		cmd = "curl -s -4 monip.org | perl -ne '/IP : ([0-9.]+)/ && print $1'"
		return commands.getoutput(cmd).strip()
	elif op == 4:
		cmd = "curl -s -4 ipcheck.ieserver.net"
		return commands.getoutput(cmd).strip()
	elif op == 5:
		cmd = "curl -s -4 ipecho.net/plain"
		return commands.getoutput(cmd).strip()
	elif op == 6:
		cmd = "curl -s -4 ifconfig.me"
		return commands.getoutput(cmd).strip()
	elif op == 7:
		cmd = "curl -s -4 eth0.me"
		return commands.getoutput(cmd).strip()
	elif op == 8:
		cmd = "curl -s -4 ifconfig.co" # v6 support
		return commands.getoutput(cmd).strip()
	elif op == 9:
		cmd = "curl -s -4 l2.io/ip" # v6 support
		return commands.getoutput(cmd).strip()
	elif op == 10:
		cmd = "curl -s -4 ip.appspot.com" # v6 support
		return commands.getoutput(cmd).strip()
	elif op == 11:
		cmd = "curl -s -4 icanhazip.com" # v6 support
		return commands.getoutput(cmd).strip()


def get_v6_global(op):
	if op == 0:
		cmd = "curl -s -6 ifconfig.co" # v6 support
		return commands.getoutput(cmd).strip()
	elif op == 1:
		cmd = "curl -s -6 l2.io/ip" # v6 support
		return commands.getoutput(cmd).strip()
	elif op == 2:
		cmd = "curl -s -6 ip.appspot.com" # v6 support
		return commands.getoutput(cmd).strip()
	elif op == 3:
		cmd = "curl -s -6 icanhazip.com" # v6 support
		return commands.getoutput(cmd).strip()


def check_v4_global():
	for i in range(0, 11):
		ip = get_v4_global(i)
		if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
			return ip
	return ""


def check_v6_global():
	for i in range(0, 3):
		ip = get_v6_global(i)
		if re.match(r"((([0-9a-f]{1,4}:){7}([0-9a-f]{1,4}|:))|(([0-9a-f]{1,4}:){6}(:[0-9a-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9a-f]{1,4}:){5}(((:[0-9a-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9a-f]{1,4}:){4}(((:[0-9a-f]{1,4}){1,3})|((:[0-9a-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9a-f]{1,4}:){3}(((:[0-9a-f]{1,4}){1,4})|((:[0-9a-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9a-f]{1,4}:){2}(((:[0-9a-f]{1,4}){1,5})|((:[0-9a-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9a-f]{1,4}:){1}(((:[0-9a-f]{1,4}){1,6})|((:[0-9a-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9a-f]{1,4}){1,7})|((:[0-9a-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$", ip):
			return ip
	return ""


def check_v6_if(nic):
	if nic == "":
		nic = "eth0"
	ip = netifaces.ifaddresses(nic)[netifaces.AF_INET6][0]['addr']
	if re.match(r"((([0-9a-f]{1,4}:){7}([0-9a-f]{1,4}|:))|(([0-9a-f]{1,4}:){6}(:[0-9a-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9a-f]{1,4}:){5}(((:[0-9a-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9a-f]{1,4}:){4}(((:[0-9a-f]{1,4}){1,3})|((:[0-9a-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9a-f]{1,4}:){3}(((:[0-9a-f]{1,4}){1,4})|((:[0-9a-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9a-f]{1,4}:){2}(((:[0-9a-f]{1,4}){1,5})|((:[0-9a-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9a-f]{1,4}:){1}(((:[0-9a-f]{1,4}){1,6})|((:[0-9a-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9a-f]{1,4}){1,7})|((:[0-9a-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$", ip):
		return ip
	return ""


