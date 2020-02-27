import json
import pytest

from aws_cdk import core
from results_reel.results_reel_stack import ResultsReelStack


def get_template():
    app = core.App()
    ResultsReelStack(app, "results-reel")
    return json.dumps(app.synth().get_stack("results-reel").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
