# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"/\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"@\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"&\n\x0fGetUserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User2=\n\x0bUserService\x12.\n\x07GetUser\x12\x0f.GetUserRequest\x1a\x10.GetUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=14
  _globals['_USER']._serialized_end=61
  _globals['_POST']._serialized_start=63
  _globals['_POST']._serialized_end=127
  _globals['_GETUSERREQUEST']._serialized_start=129
  _globals['_GETUSERREQUEST']._serialized_end=162
  _globals['_GETUSERRESPONSE']._serialized_start=164
  _globals['_GETUSERRESPONSE']._serialized_end=202
  _globals['_USERSERVICE']._serialized_start=204
  _globals['_USERSERVICE']._serialized_end=265
# @@protoc_insertion_point(module_scope)
