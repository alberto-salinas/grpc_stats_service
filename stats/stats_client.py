from __future__ import print_function
import logging

import grpc

import stats_pb2
import stats_pb2_grpc


def run():
	"""Simple client that sends requests to a GRPC stats service
	"""
    sampleData = [1,3,4]
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = stats_pb2_grpc.StatsStub(channel)

        response = stub.Average(stats_pb2.AverageRequest(data=sampleData))
        assert 2.6666667461395264 == response.result
        print("Stats average: " + str(response.result))

        response = stub.Median(stats_pb2.MedianRequest(data=sampleData))
        assert 3.0 == response.result
        print("Stats median: " + str(response.result)) 


if __name__ == '__main__':
    logging.basicConfig()
    run()
