from __future__ import annotations

from typing import List

import parsl.jobs.job_status_poller as jsp


class JobErrorHandler:
    pass


def run(status: List[jsp.PollItem]):
    for es in status:
        if not es.executor.error_management_enabled:
            return
        es.executor.handle_errors(es.status)