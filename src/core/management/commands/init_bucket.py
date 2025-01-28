from typing import Any

import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Инициализация S3 бакета."

    def handle(self, *args: Any, **options: Any) -> None:
        client = boto3.client(
            "s3",
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
        )

        try:
            client.create_bucket(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
            self.stdout.write(
                self.style.SUCCESS(f"S3 bucket {settings.AWS_STORAGE_BUCKET_NAME} created.")
            )
        except client.exceptions.BucketAlreadyOwnedByYou:
            self.stdout.write(
                self.style.SUCCESS(f"S3 bucket {settings.AWS_STORAGE_BUCKET_NAME} already exists.")
            )
