# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT. THIS FILE WAS AUTOGENERATED FROM INSTRUMENTATION PACKAGES.
# RUN `python scripts/generate_instrumentation_bootstrap.py` TO REGENERATE.

libraries = {
    "aiohttp": {
        "library": "aiohttp ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-aiohttp-client==0.23b2",
    },
    "aiopg": {
        "library": "aiopg >= 0.13.0, < 1.3.0",
        "instrumentation": "opentelemetry-instrumentation-aiopg==0.23b2",
    },
    "asgiref": {
        "library": "asgiref ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-asgi==0.23b2",
    },
    "asyncpg": {
        "library": "asyncpg >= 0.12.0",
        "instrumentation": "opentelemetry-instrumentation-asyncpg==0.23b2",
    },
    "boto": {
        "library": "boto~=2.0",
        "instrumentation": "opentelemetry-instrumentation-boto==0.23b2",
    },
    "botocore": {
        "library": "botocore ~= 1.0",
        "instrumentation": "opentelemetry-instrumentation-botocore==0.23b2",
    },
    "celery": {
        "library": "celery >= 4.0, < 6.0",
        "instrumentation": "opentelemetry-instrumentation-celery==0.23b2",
    },
    "django": {
        "library": "django >= 1.10",
        "instrumentation": "opentelemetry-instrumentation-django==0.23b2",
    },
    "elasticsearch": {
        "library": "elasticsearch >= 2.0",
        "instrumentation": "opentelemetry-instrumentation-elasticsearch==0.23b2",
    },
    "falcon": {
        "library": "falcon ~= 2.0",
        "instrumentation": "opentelemetry-instrumentation-falcon==0.23b2",
    },
    "fastapi": {
        "library": "fastapi ~= 0.58.1",
        "instrumentation": "opentelemetry-instrumentation-fastapi==0.23b2",
    },
    "flask": {
        "library": "flask >= 1.0, < 3.0",
        "instrumentation": "opentelemetry-instrumentation-flask==0.23b2",
    },
    "grpcio": {
        "library": "grpcio ~= 1.27",
        "instrumentation": "opentelemetry-instrumentation-grpc==0.23b2",
    },
    "httpx": {
        "library": "httpx >= 0.18.0, < 0.19.0",
        "instrumentation": "opentelemetry-instrumentation-httpx==0.23b2",
    },
    "jinja2": {
        "library": "jinja2~=2.7",
        "instrumentation": "opentelemetry-instrumentation-jinja2==0.23b2",
    },
    "mysql-connector-python": {
        "library": "mysql-connector-python ~= 8.0",
        "instrumentation": "opentelemetry-instrumentation-mysql==0.23b2",
    },
    "psycopg2": {
        "library": "psycopg2 >= 2.7.3.1",
        "instrumentation": "opentelemetry-instrumentation-psycopg2==0.23b2",
    },
    "pymemcache": {
        "library": "pymemcache ~= 1.3",
        "instrumentation": "opentelemetry-instrumentation-pymemcache==0.23b2",
    },
    "pymongo": {
        "library": "pymongo ~= 3.1",
        "instrumentation": "opentelemetry-instrumentation-pymongo==0.23b2",
    },
    "PyMySQL": {
        "library": "PyMySQL ~= 0.10.1",
        "instrumentation": "opentelemetry-instrumentation-pymysql==0.23b2",
    },
    "pyramid": {
        "library": "pyramid >= 1.7",
        "instrumentation": "opentelemetry-instrumentation-pyramid==0.23b2",
    },
    "redis": {
        "library": "redis >= 2.6",
        "instrumentation": "opentelemetry-instrumentation-redis==0.23b2",
    },
    "requests": {
        "library": "requests ~= 2.0",
        "instrumentation": "opentelemetry-instrumentation-requests==0.23b2",
    },
    "scikit-learn": {
        "library": "scikit-learn ~= 0.24.0",
        "instrumentation": "opentelemetry-instrumentation-sklearn==0.23b2",
    },
    "sqlalchemy": {
        "library": "sqlalchemy",
        "instrumentation": "opentelemetry-instrumentation-sqlalchemy==0.23b2",
    },
    "starlette": {
        "library": "starlette ~= 0.13.0",
        "instrumentation": "opentelemetry-instrumentation-starlette==0.23b2",
    },
    "tornado": {
        "library": "tornado >= 6.0",
        "instrumentation": "opentelemetry-instrumentation-tornado==0.23b2",
    },
    "urllib3": {
        "library": "urllib3 >= 1.0.0, < 2.0.0",
        "instrumentation": "opentelemetry-instrumentation-urllib3==0.23b2",
    },
}
default_instrumentations = [
    "opentelemetry-instrumentation-dbapi==0.23b2",
    "opentelemetry-instrumentation-logging==0.23b2",
    "opentelemetry-instrumentation-sqlite3==0.23b2",
    "opentelemetry-instrumentation-urllib==0.23b2",
    "opentelemetry-instrumentation-wsgi==0.23b2",
]
