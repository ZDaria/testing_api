import grpc
import pytest
from my_proto import my_service_pb2, my_service_pb2_grpc

@pytest.fixture
def grpc_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = my_service_pb2_grpc.MyServiceStub(channel)
    return stub

def test_my_grpc_method(grpc_client):
    request = my_service_pb2.MyRequest(param="test")
    response = grpc_client.MyMethod(request)
    assert response.result == "expected"