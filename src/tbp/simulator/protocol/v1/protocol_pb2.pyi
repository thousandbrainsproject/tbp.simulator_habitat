from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveAllObjectsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveAllObjectsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VectorXYZ(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class QuaternionWXYZ(_message.Message):
    __slots__ = ("w", "x", "y", "z")
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(self, w: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class AddObjectRequest(_message.Message):
    __slots__ = ("name", "position", "rotation", "scale", "semantic_id", "primary_target_object")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TARGET_OBJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    position: VectorXYZ
    rotation: QuaternionWXYZ
    scale: VectorXYZ
    semantic_id: int
    primary_target_object: int
    def __init__(self, name: _Optional[str] = ..., position: _Optional[_Union[VectorXYZ, _Mapping]] = ..., rotation: _Optional[_Union[QuaternionWXYZ, _Mapping]] = ..., scale: _Optional[_Union[VectorXYZ, _Mapping]] = ..., semantic_id: _Optional[int] = ..., primary_target_object: _Optional[int] = ...) -> None: ...

class AddObjectResponse(_message.Message):
    __slots__ = ("object_id", "semantic_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    semantic_id: int
    def __init__(self, object_id: _Optional[int] = ..., semantic_id: _Optional[int] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class StepRequest(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: Action
    def __init__(self, action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class SensorObservations(_message.Message):
    __slots__ = ("raw", "rgba", "depth", "semantic", "semantic_3d", "sensor_frame_data", "world_camera", "pixel_loc")
    RAW_FIELD_NUMBER: _ClassVar[int]
    RGBA_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_3D_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    WORLD_CAMERA_FIELD_NUMBER: _ClassVar[int]
    PIXEL_LOC_FIELD_NUMBER: _ClassVar[int]
    raw: bytes
    rgba: bytes
    depth: bytes
    semantic: bytes
    semantic_3d: bytes
    sensor_frame_data: bytes
    world_camera: bytes
    pixel_loc: bytes
    def __init__(self, raw: _Optional[bytes] = ..., rgba: _Optional[bytes] = ..., depth: _Optional[bytes] = ..., semantic: _Optional[bytes] = ..., semantic_3d: _Optional[bytes] = ..., sensor_frame_data: _Optional[bytes] = ..., world_camera: _Optional[bytes] = ..., pixel_loc: _Optional[bytes] = ...) -> None: ...

class AgentObservations(_message.Message):
    __slots__ = ("entries",)
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SensorObservations
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SensorObservations, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.MessageMap[int, SensorObservations]
    def __init__(self, entries: _Optional[_Mapping[int, SensorObservations]] = ...) -> None: ...

class Observations(_message.Message):
    __slots__ = ("entries",)
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AgentObservations
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AgentObservations, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.MessageMap[int, AgentObservations]
    def __init__(self, entries: _Optional[_Mapping[int, AgentObservations]] = ...) -> None: ...

class SensorState(_message.Message):
    __slots__ = ("position", "rotation")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    position: VectorXYZ
    rotation: QuaternionWXYZ
    def __init__(self, position: _Optional[_Union[VectorXYZ, _Mapping]] = ..., rotation: _Optional[_Union[QuaternionWXYZ, _Mapping]] = ...) -> None: ...

class AgentState(_message.Message):
    __slots__ = ("sensors", "position", "rotation", "motor_only_step")
    class SensorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SensorState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SensorState, _Mapping]] = ...) -> None: ...
    SENSORS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    MOTOR_ONLY_STEP_FIELD_NUMBER: _ClassVar[int]
    sensors: _containers.MessageMap[int, SensorState]
    position: VectorXYZ
    rotation: QuaternionWXYZ
    motor_only_step: bool
    def __init__(self, sensors: _Optional[_Mapping[int, SensorState]] = ..., position: _Optional[_Union[VectorXYZ, _Mapping]] = ..., rotation: _Optional[_Union[QuaternionWXYZ, _Mapping]] = ..., motor_only_step: bool = ...) -> None: ...

class ProprioceptiveState(_message.Message):
    __slots__ = ("entries",)
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AgentState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AgentState, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.MessageMap[int, AgentState]
    def __init__(self, entries: _Optional[_Mapping[int, AgentState]] = ...) -> None: ...

class StepResponse(_message.Message):
    __slots__ = ("observations", "proprioceptive_state")
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    PROPRIOCEPTIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    observations: Observations
    proprioceptive_state: ProprioceptiveState
    def __init__(self, observations: _Optional[_Union[Observations, _Mapping]] = ..., proprioceptive_state: _Optional[_Union[ProprioceptiveState, _Mapping]] = ...) -> None: ...

class ResetRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetResponse(_message.Message):
    __slots__ = ("observations", "proprioceptive_state")
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    PROPRIOCEPTIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    observations: Observations
    proprioceptive_state: ProprioceptiveState
    def __init__(self, observations: _Optional[_Union[Observations, _Mapping]] = ..., proprioceptive_state: _Optional[_Union[ProprioceptiveState, _Mapping]] = ...) -> None: ...

class CloseRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
