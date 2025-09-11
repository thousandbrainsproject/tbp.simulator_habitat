import logging
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

import tbp.simulator.protocol.v1.protocol_pb2 as protocol_pb2
import tbp.simulator.protocol.v1.protocol_pb2_grpc as protocol_pb2_grpc


class SimulatorServiceServicer(protocol_pb2_grpc.SimulatorServiceServicer):
    def RemoveAllObjects(self, request, context):  # noqa: N802
        return protocol_pb2.RemoveAllObjectsResponse()

    def AddObject(self, request, context):  # noqa: N802
        return protocol_pb2.AddObjectResponse(
            object_id=1,
            semantic_id=1,
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protocol_pb2_grpc.add_SimulatorServiceServicer_to_server(
        SimulatorServiceServicer(), server
    )
    SERVICE_NAMES = (
        protocol_pb2.DESCRIPTOR.services_by_name["SimulatorService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting server")
    serve()
