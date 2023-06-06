from python_Primitives_Server import DistributedElements
from generatedProto import primitiveService_pb2 as primitiveMsg
from generatedProto import basicMessages_pb2 as basicMsg
from typing import Generator
from python_Primitives_Server import Utils

class __FilterKBPrimitive(DistributedElements.DistributedPrimitive):
    
    def solve(self, request: DistributedElements.DistributedRequest) -> Generator[DistributedElements.DistributedResponse, None, None]:
        arg0 = request.arguments[0]
        arg1 = request.arguments[1]
        if(arg1.HasField("var")):
            for i in request.inspectKb(
                primitiveMsg.InspectKbMsg.STATIC,
                [(primitiveMsg.InspectKbMsg.STARTS_WITH, str(Utils.parseArgumentMsg(arg0)))]):
                
                if(i == None):
                    yield request.replyFail()
                else:
                    substitutions = {}
                    substitutions[arg1.var] = basicMsg.ArgumentMsg(struct=i)
                    yield request.replySuccess(
                        substitutions=substitutions
                    )
        else:
            yield request.replyFail()
            
filterKBPrimitive = DistributedElements.DistributedPrimitiveWrapper("filterKB", 2, __FilterKBPrimitive())