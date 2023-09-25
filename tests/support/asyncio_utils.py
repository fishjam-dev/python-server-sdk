# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import asyncio

from jellyfish import Notifier


async def assert_events(notifier: Notifier, event_checks: list):
    await _assert_messages(notifier.on_server_notification, event_checks, 1.)


async def assert_metrics(notifier: Notifier, metrics_checks: list):
    await _assert_messages(notifier.on_metrics, metrics_checks, 2.)


async def _assert_messages(notifier_callback, message_checks, timeout):
    success_event = asyncio.Event()

    @notifier_callback
    def handle_message(message):
        expected_msg = message_checks[0]
        if message == expected_msg or isinstance(message, expected_msg):
            message_checks.pop(0)

        if message_checks == []:
            success_event.set()

    try:
        await asyncio.wait_for(success_event.wait(), timeout)
    except asyncio.exceptions.TimeoutError as exc:
        raise asyncio.exceptions.TimeoutError(
            f"{message_checks[0]} hasn't been received within timeout") from exc


async def cancel(task):
    task.cancel()
    try:
        await task
    except asyncio.exceptions.CancelledError:
        pass
