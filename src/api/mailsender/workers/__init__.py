from src.api.mailsender.workers.abstract import MailerWorker
from src.api.mailsender.workers.task import TaskMailerWorker

from typing import Callable, Optional

import asyncio


async def start_mailer_workers(stop_function: Optional[Callable] = None):
    """
    Inicializa todos os workers para monitoramento e envio de emails.
    """
    workers = [
        TaskMailerWorker(),
    ]

    for worker in workers:
        asyncio.create_task(worker.start())