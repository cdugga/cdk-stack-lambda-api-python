#!/usr/bin/env python3

from aws_cdk import core

from results_reel.results_reel_stack import ResultsReelStack


app = core.App()
ResultsReelStack(app, "results-reel", env={'region': 'us-west-2'})

app.synth()
