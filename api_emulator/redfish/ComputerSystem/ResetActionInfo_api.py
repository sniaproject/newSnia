# Copyright Notice:
# Copyright 2016 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# Singleton API: GET

import g

import sys, traceback
from flask import Flask, request, make_response, render_template
from flask_restful import reqparse, Api, Resource

from .ResetActionInfo_template import get_ResetActionInfo_instance

members = {}

INTERNAL_ERROR = 500


class ResetActionInfo_API(Resource):
    # kwargs is use to pass in the wildcards values to replace when the instance is created.
    def __init__(self, **kwargs):
        wildcards=kwargs.get('resource_class_kwargs',{})
        if not wildcards:
            return
        # sw_id = kwargs['{sw_id}']
        try:
            config = get_ResetActionInfo_instance(wildcards)
            members[wildcards['sys_id']] = config
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR

    # HTTP GET
    def get(self,ident):
        try:
            resp = 404
            if ident in members:
                resp = members[ident], 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP PATCH

    # HTTP PUT
    def put(self):
        return 'PUT is not a valid command', 202

    # HTTP DELETE
    def delete(self):
        return 'DELETE is not a valid command', 202
