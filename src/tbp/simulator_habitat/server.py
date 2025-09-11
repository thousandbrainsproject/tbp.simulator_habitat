from __future__ import annotations

import logging
import signal
import sys
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

import tbp.simulator.protocol.v1.protocol_pb2 as protocol_pb2
import tbp.simulator.protocol.v1.protocol_pb2_grpc as protocol_pb2_grpc
from tbp.simulator_habitat.agents import SingleSensorAgent
from tbp.simulator_habitat.simulator import HabitatSim

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class SimulatorServiceServicer(protocol_pb2_grpc.SimulatorServiceServicer):
    def __init__(self, habitat_sim: HabitatSim):
        logger.info("Initializing simulator service")
        self.habitat_sim = habitat_sim

    def RemoveAllObjects(self, request, context):  # noqa: N802
        logger.info("Removing all objects")
        self.habitat_sim.remove_all_objects()
        return protocol_pb2.RemoveAllObjectsResponse()

    def AddObject(self, request, context):  # noqa: N802
        logger.info("Adding object")
        logger.info(request)
        object_id, semantic_id = self.habitat_sim.add_object(
            request.name,
            request.position,
            request.rotation,
            request.scale,
            request.semantic_id,
            request.primary_target_object,
        )
        return protocol_pb2.AddObjectResponse(
            object_id=object_id,
            semantic_id=semantic_id,
        )

    def Step(self, request, context):  # noqa: N802
        logger.info("Stepping")
        return protocol_pb2.StepResponse()

    def Reset(self, request, context):  # noqa: N802
        logger.info("Resetting")
        return protocol_pb2.ResetResponse()

    def Close(self, request, context):  # noqa: N802
        logger.info("I'm afraid I can't do that, Dave.")
        return protocol_pb2.CloseResponse()


def serve(habitat_sim: HabitatSim):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protocol_pb2_grpc.add_SimulatorServiceServicer_to_server(
        SimulatorServiceServicer(habitat_sim), server
    )
    SERVICE_NAMES = (
        protocol_pb2.DESCRIPTOR.services_by_name["SimulatorService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


def signal_handler(habitat_sim: HabitatSim):
    def signal_handler_inner(signum, frame):
        logger.info("Closing habitat sim")
        habitat_sim.close()
        sys.exit(0)

    return signal_handler_inner


def create_habitat_sim() -> HabitatSim:
    logger.info("Creating habitat sim")
    agents = create_agents(num_agents=1, resolution=(5, 5))
    habitat_sim = HabitatSim(agents=agents)
    logger.info("Habitat sim created")
    return habitat_sim


def create_agents(
    num_agents,
    resolution=(64, 64),
    semantic=False,
    action_space_type="distant_agent",
    rotation_step=10.0,
    translation_step=0.25,
) -> list[SingleSensorAgent]:
    """Create agents with RGB, Depth and optional semantic sensors.

    Args:
        num_agents: Number of agents to create
        resolution: Sensor resolution
        semantic: Whether or not to add semantic sensor
        action_space_type: Whether to use the action-space of a surface agent,
            distant agent, or an agent operating with absolute, world-coordinate actions
            only
        rotation_step: Default action rotation step in degrees
        translation_step: Default action translation step in meters

    Returns:
        The created agents.
    """
    agents = []
    for i in range(num_agents):
        cam = SingleSensorAgent(
            agent_id=f"{i}",  # TODO: AgentID
            sensor_id="0",  # TODO: SensorID
            resolution=resolution,
            semantic=semantic,
            translation_step=translation_step,
            rotation_step=rotation_step,
            action_space_type=action_space_type,
        )
        agents.append(cam)
    return agents


if __name__ == "__main__":
    logger.info("Starting server")
    habitat_sim = create_habitat_sim()
    signal.signal(signal.SIGINT, signal_handler(habitat_sim))
    serve(habitat_sim)
