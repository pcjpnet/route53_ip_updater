#!/usr/bin/env python
# coding:UTF-8
import boto.route53

#print lib_route53.read_route53(key, sec, zone, name, typ)
#print lib_route53.write_route53(key, sec, zone, name, typ, ttl, "pjsv.net")

def read_route53(key, sec, zone, name, typ):
	if key == "" or sec == "" or zone == "" or name == "" or typ == "":
		return
	r53 = boto.route53.connect_to_region("universal",
		aws_access_key_id = key,
		aws_secret_access_key = sec)
	return r53.get_all_rrsets(zone, typ, name, maxitems=1)[0].resource_records[0]


def write_route53(key, sec, zone, name, typ, ttl, val):
	if key == "" or sec == "" or zone == "" or name == "" or typ == "" or val == "":
		return
	if typ == "":
		typ = "A"
	if ttl == "":
		ttl = "600"
	r53 = boto.route53.connect_to_region("universal",
		aws_access_key_id = key,
		aws_secret_access_key = sec)
	r53rr = boto.route53.record.ResourceRecordSets(r53, zone)
	r53rr.add_change("UPSERT", name, typ, ttl).add_value(val)
	r53rr.commit()
	

