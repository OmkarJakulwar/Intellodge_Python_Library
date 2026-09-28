# intellodge_core

A reusable Python library for **Django + AWS DynamoDB** projects. It provides a generic DynamoDB CRUD service, consistent logging, custom exceptions, validators and helper functions, so application code doesn't repeat the same `boto3` boilerplate.

It was built for, and is used in, **[IntelLodge](https://github.com/OmkarJakulwar/Intellodge_Cloud_Platform_Programming)**, a hotel management platform on AWS. The same package runs in the Django web app and inside an AWS Lambda function.

Published on **TestPyPI** as `intellodge_core`.

---

## Installation

```bash
pip install --index-url https://test.pypi.org/simple \
            --extra-index-url https://pypi.org/simple \
            intellodge_core
```

Or install from source:

```bash
git clone https://github.com/OmkarJakulwar/Intellodge_Python_Library.git
cd Intellodge_Python_Library
pip install .
```

Requires Python 3.8+. Dependencies are `boto3`, `python-jose`, `pytz` and `django`.

---

## Modules

| Module | What it provides |
|---|---|
| `base_service` | `BaseDynamoDBService`: `create`, `read`, `update`, `delete` and `find_all` for any DynamoDB table. It builds update expressions dynamically and returns a consistent `{success, ...}` result. |
| `logger` | `get_logger()`: a logger with the same format in every module |
| `exceptions` | `NotFoundError`, `ValidationError`, `PermissionDenied`, `ServiceError` |
| `validators` | `require_fields()`, `validate_email()`, `validate_role()` |
| `response_utils` | Standard success, error, not-found and validation-error response formats |
| `auth_utils` | Session helpers: `get_current_user()`, `is_admin()`, `require_login()` |
| `datetime_utils` | `now_utc()`, `format_date()`, `parse_date()` |

---

## Quick Start

```python
from intellodge_core.base_service import BaseDynamoDBService

class RoomService(BaseDynamoDBService):
    def __init__(self):
        super().__init__("Rooms")          # DynamoDB table name

rooms = RoomService()
rooms.create({"room_number": "101", "status": "Vacant"})
rooms.update({"room_number": "101"}, {"status": "Occupied"})
rooms.read({"room_number": "101"})      # {"success": True, "item": {...}}
rooms.find_all()                        # {"success": True, "items": [...]}
```

```python
from intellodge_core.logger import get_logger
from intellodge_core.datetime_utils import now_utc

log = get_logger(__name__)
log.info(f"Booking created at {now_utc()}")
```

AWS credentials are read from the standard `boto3` sources (environment variables, `~/.aws/credentials`, or an IAM role). The default region is `us-east-1`, and you can pass `region_name` to use a different one.

---

## Used In

- **IntelLodge web app (Django on Elastic Beanstalk):** the data classes for Rooms, Bookings, Users and Revenue are all built on `BaseDynamoDBService`.
- **AutoRoomStatusLambda (AWS Lambda):** the package is bundled into the deployment zip, so the Lambda uses the same data-access code as the web app.

---

## License

MIT. See [LICENSE](LICENSE).

**Author:** Omkar Jakulwar
