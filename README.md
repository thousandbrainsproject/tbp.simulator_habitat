# tbp.simulator_habitat

## Generate proto files

python -m grpc_tools.protoc -IPATH/TO/TBP/MONTY/proto --python_out=src --pyi_out=src --grpc_python_out=src PATH/TO/TBP/MONTY/proto/tbp/simulator/protocol/v1/protocol.proto

python -m grpc_tools.protoc -I/Users/tslominski/tbp/prototype.simulator/proto --python_out=src --pyi_out=src --grpc_python_out=src /Users/tslominski/tbp/prototype.simulator/proto/tbp/simulator/protocol/v1/protocol.proto
