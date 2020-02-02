# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hypernetwork_pb2 as hypernetwork__pb2


class HTStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetHypersimplex = channel.unary_unary(
        '/HT/GetHypersimplex',
        request_serializer=hypernetwork__pb2.VertexMessage.SerializeToString,
        response_deserializer=hypernetwork__pb2.HypersimplexMessage.FromString,
        )
    self.AddHypersimplex = channel.unary_unary(
        '/HT/AddHypersimplex',
        request_serializer=hypernetwork__pb2.HypersimplexMessage.SerializeToString,
        response_deserializer=hypernetwork__pb2.VertexMessage.FromString,
        )
    self.DeleteHypersimplex = channel.unary_unary(
        '/HT/DeleteHypersimplex',
        request_serializer=hypernetwork__pb2.HypersimplexMessage.SerializeToString,
        response_deserializer=hypernetwork__pb2.VertexMessage.FromString,
        )
    self.GetHypernetwork = channel.unary_unary(
        '/HT/GetHypernetwork',
        request_serializer=hypernetwork__pb2.DeleteHsMessage.SerializeToString,
        response_deserializer=hypernetwork__pb2.EmptyMessage.FromString,
        )


class HTServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetHypersimplex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHypersimplex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHypersimplex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHypernetwork(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HTServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetHypersimplex': grpc.unary_unary_rpc_method_handler(
          servicer.GetHypersimplex,
          request_deserializer=hypernetwork__pb2.VertexMessage.FromString,
          response_serializer=hypernetwork__pb2.HypersimplexMessage.SerializeToString,
      ),
      'AddHypersimplex': grpc.unary_unary_rpc_method_handler(
          servicer.AddHypersimplex,
          request_deserializer=hypernetwork__pb2.HypersimplexMessage.FromString,
          response_serializer=hypernetwork__pb2.VertexMessage.SerializeToString,
      ),
      'DeleteHypersimplex': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHypersimplex,
          request_deserializer=hypernetwork__pb2.HypersimplexMessage.FromString,
          response_serializer=hypernetwork__pb2.VertexMessage.SerializeToString,
      ),
      'GetHypernetwork': grpc.unary_unary_rpc_method_handler(
          servicer.GetHypernetwork,
          request_deserializer=hypernetwork__pb2.DeleteHsMessage.FromString,
          response_serializer=hypernetwork__pb2.EmptyMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'HT', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
