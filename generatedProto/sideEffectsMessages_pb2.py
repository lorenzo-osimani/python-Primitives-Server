# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sideEffectsMessages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basicMessages_pb2 as basicMessages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19sideEffectsMessages.proto\x12\nprimitives\x1a\x13\x62\x61sicMessages.proto\"\xc0\x02\n\rSideEffectMsg\x12\x30\n\x07\x63lauses\x18\x01 \x01(\x0b\x32\x1d.primitives.SetClausesOfKBMsgH\x00\x12*\n\x05\x66lags\x18\x02 \x01(\x0b\x32\x19.primitives.AlterFlagsMsgH\x00\x12.\n\x07runtime\x18\x03 \x01(\x0b\x32\x1b.primitives.AlterRuntimeMsgH\x00\x12\x32\n\toperators\x18\x04 \x01(\x0b\x32\x1d.primitives.AlterOperatorsMsgH\x00\x12\x30\n\x08\x63hannels\x18\x05 \x01(\x0b\x32\x1c.primitives.AlterChannelsMsgH\x00\x12\x34\n\ncustomData\x18\x06 \x01(\x0b\x32\x1e.primitives.AlterCustomDataMsgH\x00\x42\x05\n\x03msg\"\x99\x02\n\x11SetClausesOfKBMsg\x12\x34\n\x06kbType\x18\x01 \x01(\x0e\x32$.primitives.SetClausesOfKBMsg.KbType\x12;\n\roperationType\x18\x02 \x01(\x0e\x32$.primitives.SetClausesOfKBMsg.OpType\x12\x12\n\x05onTop\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12&\n\x07\x63lauses\x18\x04 \x03(\x0b\x32\x15.primitives.StructMsg\"!\n\x06KbType\x12\n\n\x06STATIC\x10\x00\x12\x0b\n\x07\x44YNAMIC\x10\x01\"(\n\x06OpType\x12\t\n\x05RESET\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x42\x08\n\x06_onTop\"\xed\x01\n\rAlterFlagsMsg\x12\x37\n\roperationType\x18\x01 \x01(\x0e\x32 .primitives.AlterFlagsMsg.OpType\x12\x33\n\x05\x66lags\x18\x02 \x03(\x0b\x32$.primitives.AlterFlagsMsg.FlagsEntry\x1a\x45\n\nFlagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.primitives.ArgumentMsg:\x02\x38\x01\"\'\n\x06OpType\x12\x07\n\x03SET\x10\x00\x12\t\n\x05RESET\x10\x01\x12\t\n\x05\x43LEAR\x10\x02\"\x96\x01\n\x0f\x41lterRuntimeMsg\x12\x39\n\roperationType\x18\x01 \x01(\x0e\x32\".primitives.AlterRuntimeMsg.OpType\x12\x11\n\tlibraries\x18\x02 \x03(\t\"5\n\x06OpType\x12\x08\n\x04LOAD\x10\x00\x12\n\n\x06UNLOAD\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\t\n\x05RESET\x10\x03\"\xa6\x01\n\x11\x41lterOperatorsMsg\x12;\n\roperationType\x18\x01 \x01(\x0e\x32$.primitives.AlterOperatorsMsg.OpType\x12*\n\toperators\x18\x02 \x03(\x0b\x32\x17.primitives.OperatorMsg\"(\n\x06OpType\x12\x07\n\x03SET\x10\x00\x12\t\n\x05RESET\x10\x01\x12\n\n\x06REMOVE\x10\x02\"\xf5\x06\n\x10\x41lterChannelsMsg\x12=\n\x06modify\x18\x02 \x01(\x0b\x32+.primitives.AlterChannelsMsg.ModifyChannelsH\x00\x12;\n\x05\x63lose\x18\x03 \x01(\x0b\x32*.primitives.AlterChannelsMsg.CloseChannelsH\x00\x12\x34\n\x05write\x18\x04 \x01(\x0b\x32#.primitives.WriteOnOutputChannelMsgH\x00\x1a\xb0\x02\n\x0eModifyChannels\x12K\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x39.primitives.AlterChannelsMsg.ModifyChannels.ChannelsEntry\x12\x42\n\x06opType\x18\x02 \x01(\x0e\x32\x32.primitives.AlterChannelsMsg.ModifyChannels.OpType\x12=\n\x0b\x63hannelType\x18\x03 \x01(\x0e\x32(.primitives.AlterChannelsMsg.ChannelType\x1a/\n\rChannelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1d\n\x06OpType\x12\x08\n\x04OPEN\x10\x00\x12\t\n\x05RESET\x10\x01\x1a`\n\rCloseChannels\x12\x10\n\x08\x63hannels\x18\x01 \x03(\t\x12=\n\x0b\x63hannelType\x18\x02 \x01(\x0e\x32(.primitives.AlterChannelsMsg.ChannelType\x1a\xe6\x01\n\x0eWriteOnOutputs\x12K\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x39.primitives.AlterChannelsMsg.WriteOnOutputs.ChannelsEntry\x1a\x1e\n\nContentMsg\x12\x10\n\x08messages\x18\x01 \x03(\t\x1ag\n\rChannelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.primitives.AlterChannelsMsg.WriteOnOutputs.ContentMsg:\x02\x38\x01\"$\n\x0b\x43hannelType\x12\t\n\x05INPUT\x10\x00\x12\n\n\x06OUTPUT\x10\x01\x42\x0b\n\toperation\"\xda\x01\n\x17WriteOnOutputChannelMsg\x12\x43\n\x08messages\x18\x03 \x03(\x0b\x32\x31.primitives.WriteOnOutputChannelMsg.MessagesEntry\x1a\x1b\n\x08Messages\x12\x0f\n\x07message\x18\x01 \x03(\t\x1a]\n\rMessagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.primitives.WriteOnOutputChannelMsg.Messages:\x02\x38\x01\"\xf0\x01\n\x12\x41lterCustomDataMsg\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.primitives.AlterCustomDataMsg.OpType\x12\x36\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32(.primitives.AlterCustomDataMsg.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"@\n\x06OpType\x12\x12\n\x0eSET_PERSISTENT\x10\x00\x12\x0f\n\x0bSET_DURABLE\x10\x01\x12\x11\n\rSET_EPHEMERAL\x10\x02\"\xc1\x01\n\x14UpdateFromSessionMsg\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.primitives.UpdateFromSessionMsg.UpdateType\"n\n\nUpdateType\x12\r\n\tSTATIC_KB\x10\x00\x12\x0e\n\nDYNAMIC_KB\x10\x01\x12\t\n\x05\x46LAGS\x10\x02\x12\r\n\tOPERATORS\x10\x03\x12\x12\n\x0eINPUT_CHANNELS\x10\x04\x12\x13\n\x0fOUTPUT_CHANNELS\x10\x05\x42<\n(it.unibo.tuprolog.primitives.sideEffectsB\x0eSideEffectsMsgP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sideEffectsMessages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(it.unibo.tuprolog.primitives.sideEffectsB\016SideEffectsMsgP\001'
  _ALTERFLAGSMSG_FLAGSENTRY._options = None
  _ALTERFLAGSMSG_FLAGSENTRY._serialized_options = b'8\001'
  _ALTERCHANNELSMSG_MODIFYCHANNELS_CHANNELSENTRY._options = None
  _ALTERCHANNELSMSG_MODIFYCHANNELS_CHANNELSENTRY._serialized_options = b'8\001'
  _ALTERCHANNELSMSG_WRITEONOUTPUTS_CHANNELSENTRY._options = None
  _ALTERCHANNELSMSG_WRITEONOUTPUTS_CHANNELSENTRY._serialized_options = b'8\001'
  _WRITEONOUTPUTCHANNELMSG_MESSAGESENTRY._options = None
  _WRITEONOUTPUTCHANNELMSG_MESSAGESENTRY._serialized_options = b'8\001'
  _ALTERCUSTOMDATAMSG_DATAENTRY._options = None
  _ALTERCUSTOMDATAMSG_DATAENTRY._serialized_options = b'8\001'
  _SIDEEFFECTMSG._serialized_start=63
  _SIDEEFFECTMSG._serialized_end=383
  _SETCLAUSESOFKBMSG._serialized_start=386
  _SETCLAUSESOFKBMSG._serialized_end=667
  _SETCLAUSESOFKBMSG_KBTYPE._serialized_start=582
  _SETCLAUSESOFKBMSG_KBTYPE._serialized_end=615
  _SETCLAUSESOFKBMSG_OPTYPE._serialized_start=617
  _SETCLAUSESOFKBMSG_OPTYPE._serialized_end=657
  _ALTERFLAGSMSG._serialized_start=670
  _ALTERFLAGSMSG._serialized_end=907
  _ALTERFLAGSMSG_FLAGSENTRY._serialized_start=797
  _ALTERFLAGSMSG_FLAGSENTRY._serialized_end=866
  _ALTERFLAGSMSG_OPTYPE._serialized_start=868
  _ALTERFLAGSMSG_OPTYPE._serialized_end=907
  _ALTERRUNTIMEMSG._serialized_start=910
  _ALTERRUNTIMEMSG._serialized_end=1060
  _ALTERRUNTIMEMSG_OPTYPE._serialized_start=1007
  _ALTERRUNTIMEMSG_OPTYPE._serialized_end=1060
  _ALTEROPERATORSMSG._serialized_start=1063
  _ALTEROPERATORSMSG._serialized_end=1229
  _ALTEROPERATORSMSG_OPTYPE._serialized_start=1189
  _ALTEROPERATORSMSG_OPTYPE._serialized_end=1229
  _ALTERCHANNELSMSG._serialized_start=1232
  _ALTERCHANNELSMSG._serialized_end=2117
  _ALTERCHANNELSMSG_MODIFYCHANNELS._serialized_start=1431
  _ALTERCHANNELSMSG_MODIFYCHANNELS._serialized_end=1735
  _ALTERCHANNELSMSG_MODIFYCHANNELS_CHANNELSENTRY._serialized_start=1657
  _ALTERCHANNELSMSG_MODIFYCHANNELS_CHANNELSENTRY._serialized_end=1704
  _ALTERCHANNELSMSG_MODIFYCHANNELS_OPTYPE._serialized_start=1706
  _ALTERCHANNELSMSG_MODIFYCHANNELS_OPTYPE._serialized_end=1735
  _ALTERCHANNELSMSG_CLOSECHANNELS._serialized_start=1737
  _ALTERCHANNELSMSG_CLOSECHANNELS._serialized_end=1833
  _ALTERCHANNELSMSG_WRITEONOUTPUTS._serialized_start=1836
  _ALTERCHANNELSMSG_WRITEONOUTPUTS._serialized_end=2066
  _ALTERCHANNELSMSG_WRITEONOUTPUTS_CONTENTMSG._serialized_start=1931
  _ALTERCHANNELSMSG_WRITEONOUTPUTS_CONTENTMSG._serialized_end=1961
  _ALTERCHANNELSMSG_WRITEONOUTPUTS_CHANNELSENTRY._serialized_start=1963
  _ALTERCHANNELSMSG_WRITEONOUTPUTS_CHANNELSENTRY._serialized_end=2066
  _ALTERCHANNELSMSG_CHANNELTYPE._serialized_start=2068
  _ALTERCHANNELSMSG_CHANNELTYPE._serialized_end=2104
  _WRITEONOUTPUTCHANNELMSG._serialized_start=2120
  _WRITEONOUTPUTCHANNELMSG._serialized_end=2338
  _WRITEONOUTPUTCHANNELMSG_MESSAGES._serialized_start=2216
  _WRITEONOUTPUTCHANNELMSG_MESSAGES._serialized_end=2243
  _WRITEONOUTPUTCHANNELMSG_MESSAGESENTRY._serialized_start=2245
  _WRITEONOUTPUTCHANNELMSG_MESSAGESENTRY._serialized_end=2338
  _ALTERCUSTOMDATAMSG._serialized_start=2341
  _ALTERCUSTOMDATAMSG._serialized_end=2581
  _ALTERCUSTOMDATAMSG_DATAENTRY._serialized_start=2472
  _ALTERCUSTOMDATAMSG_DATAENTRY._serialized_end=2515
  _ALTERCUSTOMDATAMSG_OPTYPE._serialized_start=2517
  _ALTERCUSTOMDATAMSG_OPTYPE._serialized_end=2581
  _UPDATEFROMSESSIONMSG._serialized_start=2584
  _UPDATEFROMSESSIONMSG._serialized_end=2777
  _UPDATEFROMSESSIONMSG_UPDATETYPE._serialized_start=2667
  _UPDATEFROMSESSIONMSG_UPDATETYPE._serialized_end=2777
# @@protoc_insertion_point(module_scope)
