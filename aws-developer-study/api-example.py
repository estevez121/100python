# !/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
API Example
"""

import boto3

# Explicit Client Configuration
polly = boto3.client('polly',
                     region_name='us-east-1')
result = polly.synthesize_speech(Text='Hello World!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the audio from the response
audio = result['AudioStream'].read()
with open('helloworld.mp3', 'wb') as file:
    file.write(audio)
