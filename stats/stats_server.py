from concurrent import futures
import logging
import statistics

import grpc

import stats_pb2
import stats_pb2_grpc


class Stats(stats_pb2_grpc.StatsServicer):

    def Average(self, request, context):
        result = sum(request.data) / len(request.data)
        return stats_pb2.SingleResult(result=result)

    def Median(self, request, context):
    	return stats_pb2.SingleResult(result=statistics.median(request.data))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServicer_to_server(Stats(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
