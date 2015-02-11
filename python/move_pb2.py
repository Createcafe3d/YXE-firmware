# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: move.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='move.proto',
  package='',
  serialized_pb='\n\nmove.proto\"<\n\x04Move\x12\n\n\x02id\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x12\x12\n\nlaserPower\x18\x04 \x02(\x05\"\x11\n\x03\x41\x63k\x12\n\n\x02id\x18\x01 \x02(\x05\"\"\n\x04Nack\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06reason\x18\x02 \x02(\x05\"&\n\x07Measure\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x63hannel\x18\x02 \x02(\x05')




_MOVE = _descriptor.Descriptor(
  name='Move',
  full_name='Move',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Move.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='Move.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Move.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='laserPower', full_name='Move.laserPower', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=14,
  serialized_end=74,
)


_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Ack.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=76,
  serialized_end=93,
)


_NACK = _descriptor.Descriptor(
  name='Nack',
  full_name='Nack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Nack.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Nack.reason', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=95,
  serialized_end=129,
)


_MEASURE = _descriptor.Descriptor(
  name='Measure',
  full_name='Measure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Measure.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='Measure.channel', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=131,
  serialized_end=169,
)

DESCRIPTOR.message_types_by_name['Move'] = _MOVE
DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['Nack'] = _NACK
DESCRIPTOR.message_types_by_name['Measure'] = _MEASURE

class Move(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MOVE

  # @@protoc_insertion_point(class_scope:Move)

class Ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACK

  # @@protoc_insertion_point(class_scope:Ack)

class Nack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NACK

  # @@protoc_insertion_point(class_scope:Nack)

class Measure(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MEASURE

  # @@protoc_insertion_point(class_scope:Measure)


# @@protoc_insertion_point(module_scope)
