from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
    aws_apigateway as apigw,
)
from constructs import Construct

from .hitcounter import HitCounter 

class HitCounterApp02Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
                self, 'HelloHandler',
                runtime=_lambda.Runtime.PYTHON_3_7,
                code=_lambda.Code.from_asset('lambda'),
                handler='hello.handler',
        )

        hello_with_counter = HitCounter(
                self, 'HelloHitCounter',
                downstream=my_lambda,
        )

        apigw.LambdaRestApi(
                self, 'Endpoint',
                handler=hello_with_counter._handler,
        )
