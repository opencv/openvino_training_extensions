"""
 Copyright (c) 2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import os
import subprocess

from ote import MMDETECTION_TOOLS

from .mmdetection import MMDetectionEvaluator
from ..registry import EVALUATORS


@EVALUATORS.register_module()
class MMFaceDetectionEvaluator(MMDetectionEvaluator):
    def __init__(self):
        super(MMFaceDetectionEvaluator, self).__init__()

    def _get_metric_functions(self):
        from ote.metrics.detection.common import coco_ap_eval_det
        from ote.metrics.face_detection.face_detection import custom_ap_eval, compute_wider_metrics

        return [coco_ap_eval_det, custom_ap_eval, compute_wider_metrics]
