import aws_cdk as core
import aws_cdk.assertions as assertions

from hit_counter_app_02.hit_counter_app_02_stack import HitCounterApp02Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in hit_counter_app_02/hit_counter_app_02_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HitCounterApp02Stack(app, "hit-counter-app-02")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
