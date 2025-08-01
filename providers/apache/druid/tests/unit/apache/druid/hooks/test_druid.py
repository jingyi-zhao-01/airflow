#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
import requests

from airflow.exceptions import AirflowException
from airflow.providers.apache.druid.hooks.druid import DruidDbApiHook, DruidHook, IngestionType


@pytest.mark.db_test
class TestDruidSubmitHook:
    def setup_method(self):
        import requests_mock

        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount("mock", adapter)

        class TestDRuidhook(DruidHook):
            self.is_sql_based_ingestion = False

            def get_conn_url(self, ingestion_type: IngestionType = IngestionType.BATCH):
                if self.conn.schema:
                    conn_type = self.conn.schema
                else:
                    conn_type = "http"

                if ingestion_type == IngestionType.MSQ:
                    return f"{conn_type}://druid-overlord:8081/druid/v2/sql/task"
                return f"{conn_type}://druid-overlord:8081/druid/indexer/v1/task"

        self.db_hook = TestDRuidhook()

    def test_submit_gone_wrong(self, requests_mock):
        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "FAILED"}}',
        )

        # The job failed for some reason
        with pytest.raises(AirflowException):
            self.db_hook.submit_indexing_job("Long json file")

        # PGH005: false positive on ``requests_mock`` argument `called_once`
        assert task_post.call_count == 1
        assert status_check.call_count == 1

    def test_submit_ok(self, requests_mock):
        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            status_code=200,
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "SUCCESS"}}',
        )

        # Exists just as it should
        self.db_hook.submit_indexing_job("Long json file")

        # PGH005: false positive on ``requests_mock`` argument `called_once`
        assert task_post.call_count == 1
        assert status_check.call_count == 1

    def test_submit_sql_based_ingestion_ok(self, requests_mock):
        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/v2/sql/task",
            status_code=202,
            text='{"taskId":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "SUCCESS"}}',
        )

        # Exists just as it should
        self.db_hook.submit_indexing_job("Long json file", IngestionType.MSQ)

        # PGH005: false positive on ``requests_mock`` argument `called_once`
        assert task_post.call_count == 1
        assert status_check.call_count == 1

    def test_submit_with_false_ssl_arg(self, requests_mock):
        # Timeout so that all three requests are sent
        self.db_hook.timeout = 1
        self.db_hook.max_ingestion_time = 5
        self.db_hook.verify_ssl = False

        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "RUNNING"}}',
        )
        shutdown_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/shutdown",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )

        with pytest.raises(AirflowException):
            self.db_hook.submit_indexing_job("Long json file")

        assert task_post.call_count == 1
        assert task_post.request_history[0].verify is False

        assert status_check.call_count > 1
        assert status_check.request_history[0].verify is False

        assert shutdown_post.call_count == 1
        assert shutdown_post.request_history[0].verify is False

    def test_submit_with_true_ssl_arg(self, requests_mock):
        # Timeout so that all three requests are sent
        self.db_hook.timeout = 1
        self.db_hook.max_ingestion_time = 5
        self.db_hook.verify_ssl = True

        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "RUNNING"}}',
        )
        shutdown_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/shutdown",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )

        with pytest.raises(AirflowException):
            self.db_hook.submit_indexing_job("Long json file")

        assert task_post.call_count == 1
        assert task_post.request_history[0].verify is True

        assert status_check.call_count > 1
        assert status_check.request_history[0].verify is True

        assert shutdown_post.call_count == 1
        assert shutdown_post.request_history[0].verify is True

    def test_submit_correct_json_body(self, requests_mock):
        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "SUCCESS"}}',
        )

        json_ingestion_string = """
        {
            "task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"
        }
        """
        self.db_hook.submit_indexing_job(json_ingestion_string)

        # PGH005: false positive on ``requests_mock`` argument `called_once`
        assert task_post.call_count == 1
        assert status_check.call_count == 1
        if task_post.called_once:
            req_body = task_post.request_history[0].json()
            assert req_body["task"] == "9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"

    def test_submit_unknown_response(self, requests_mock):
        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "UNKNOWN"}}',
        )

        # An unknown error code
        with pytest.raises(AirflowException):
            self.db_hook.submit_indexing_job("Long json file")

        # PGH005: false positive on requests_mock arguments
        assert task_post.call_count == 1
        assert status_check.call_count == 1

    def test_submit_timeout(self, requests_mock):
        self.db_hook.timeout = 1
        self.db_hook.max_ingestion_time = 5
        task_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )
        status_check = requests_mock.get(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/status",
            text='{"status":{"status": "RUNNING"}}',
        )
        shutdown_post = requests_mock.post(
            "http://druid-overlord:8081/druid/indexer/v1/task/9f8a7359-77d4-4612-b0cd-cc2f6a3c28de/shutdown",
            text='{"task":"9f8a7359-77d4-4612-b0cd-cc2f6a3c28de"}',
        )

        # Because the jobs keeps running
        with pytest.raises(AirflowException):
            self.db_hook.submit_indexing_job("Long json file")

        assert status_check.called
        # PGH005: false positive on ``requests_mock`` argument `called_once`
        assert task_post.call_count == 1
        assert shutdown_post.call_count == 1


class TestDruidHook:
    def setup_method(self):
        import requests_mock

        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount("mock", adapter)

        class TestDRuidhook(DruidHook):
            self.is_sql_based_ingestion = False

            def get_conn_url(self, ingestion_type: IngestionType = IngestionType.BATCH):
                if ingestion_type == IngestionType.MSQ:
                    return "http://druid-overlord:8081/druid/v2/sql/task"
                return "http://druid-overlord:8081/druid/indexer/v1/task"

        self.db_hook = TestDRuidhook()

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_conn_property(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "http"
        get_conn_value.schema = None
        get_conn_value.port = "1"
        get_conn_value.extra_dejson = {"endpoint": "ingest"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook()
        assert hook.conn == get_conn_value

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_conn_url(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "http"
        get_conn_value.schema = None
        get_conn_value.port = "1"
        get_conn_value.extra_dejson = {"endpoint": "ingest"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook(timeout=1, max_ingestion_time=5)
        assert hook.get_conn_url() == "http://test_host:1/ingest"

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_conn_url_with_schema(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "http"
        get_conn_value.schema = None
        get_conn_value.port = "1"
        get_conn_value.schema = "https"
        get_conn_value.extra_dejson = {"endpoint": "ingest"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook(timeout=1, max_ingestion_time=5)
        assert hook.get_conn_url() == "https://test_host:1/ingest"

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_conn_url_with_ingestion_type(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "http"
        get_conn_value.schema = None
        get_conn_value.port = "1"
        get_conn_value.extra_dejson = {"endpoint": "ingest", "msq_endpoint": "sql_ingest"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook(timeout=1, max_ingestion_time=5)
        assert hook.get_conn_url(IngestionType.MSQ) == "http://test_host:1/sql_ingest"

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_conn_url_with_ingestion_type_and_schema(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "http"
        get_conn_value.port = "1"
        get_conn_value.schema = "https"
        get_conn_value.extra_dejson = {"endpoint": "ingest", "msq_endpoint": "sql_ingest"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook(timeout=1, max_ingestion_time=5)
        assert hook.get_conn_url(IngestionType.MSQ) == "https://test_host:1/sql_ingest"

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_status_url(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "http"
        get_conn_value.schema = "https"
        get_conn_value.port = "1"
        get_conn_value.extra_dejson = {"endpoint": "ingest", "msq_endpoint": "sql_ingest"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook(timeout=1, max_ingestion_time=5)
        assert hook.get_status_url(IngestionType.MSQ) == "https://test_host:1/druid/indexer/v1/task"

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_auth(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.login = "airflow"
        get_conn_value.password = "password"
        mock_get_connection.return_value = get_conn_value
        expected = requests.auth.HTTPBasicAuth("airflow", "password")
        assert self.db_hook.get_auth() == expected

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_auth_with_no_user(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.login = None
        get_conn_value.password = "password"
        mock_get_connection.return_value = get_conn_value
        assert self.db_hook.get_auth() is None

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_auth_with_no_password(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.login = "airflow"
        get_conn_value.password = None
        mock_get_connection.return_value = get_conn_value
        assert self.db_hook.get_auth() is None

    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_auth_with_no_user_and_password(self, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.login = None
        get_conn_value.password = None
        mock_get_connection.return_value = get_conn_value
        assert self.db_hook.get_auth() is None

    @pytest.mark.parametrize(
        "verify_ssl_arg, ca_bundle_path, expected_return_value",
        [
            (False, None, False),
            (True, None, True),
            (False, "path/to/ca_bundle", "path/to/ca_bundle"),
            (True, "path/to/ca_bundle", True),
        ],
    )
    @patch("airflow.providers.apache.druid.hooks.druid.DruidHook.get_connection")
    def test_get_verify(self, mock_get_connection, verify_ssl_arg, ca_bundle_path, expected_return_value):
        get_conn_value = MagicMock()
        get_conn_value.extra_dejson = {"ca_bundle_path": ca_bundle_path}
        mock_get_connection.return_value = get_conn_value
        hook = DruidHook(verify_ssl=verify_ssl_arg)
        assert hook.get_verify() == expected_return_value


class TestDruidDbApiHook:
    def setup_method(self):
        self.cur = MagicMock(rowcount=0)
        self.conn = conn = MagicMock()
        self.conn.host = "host"
        self.conn.port = "1000"
        self.conn.schema = None
        self.conn.conn_type = "druid"
        self.conn.extra_dejson = {"endpoint": "druid/v2/sql"}
        self.conn.cursor.return_value = self.cur

        class TestDruidDBApiHook(DruidDbApiHook):
            def get_conn(self):
                return conn

            def get_connection(self, conn_id):
                return conn

        self.db_hook = TestDruidDBApiHook

    @patch("airflow.providers.apache.druid.hooks.druid.DruidDbApiHook.get_connection")
    @patch("airflow.providers.apache.druid.hooks.druid.connect")
    @pytest.mark.parametrize(
        ("specified_context", "passed_context"),
        [
            (None, {}),
            ({"query_origin": "airflow"}, {"query_origin": "airflow"}),
        ],
    )
    def test_get_conn_with_context(
        self, mock_connect, mock_get_connection, specified_context, passed_context
    ):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "https"
        get_conn_value.login = "test_login"
        get_conn_value.password = "test_password"
        get_conn_value.port = 10000
        get_conn_value.extra_dejson = {"endpoint": "/test/endpoint", "schema": "https"}
        mock_get_connection.return_value = get_conn_value
        hook = DruidDbApiHook(context=specified_context)
        hook.get_conn()
        mock_connect.assert_called_with(
            host="test_host",
            port=10000,
            path="/test/endpoint",
            scheme="https",
            user="test_login",
            password="test_password",
            context=passed_context,
            ssl_verify_cert=True,
        )

    @patch("airflow.providers.apache.druid.hooks.druid.DruidDbApiHook.get_connection")
    @patch("airflow.providers.apache.druid.hooks.druid.connect")
    def test_get_conn_respects_ssl_verify_cert(self, mock_connect, mock_get_connection):
        get_conn_value = MagicMock()
        get_conn_value.host = "test_host"
        get_conn_value.conn_type = "https"
        get_conn_value.login = "test_login"
        get_conn_value.password = "test_password"
        get_conn_value.port = 10000
        get_conn_value.extra_dejson = {
            "endpoint": "/test/endpoint",
            "schema": "https",
            "ssl_verify_cert": False,
        }
        mock_get_connection.return_value = get_conn_value
        hook = DruidDbApiHook()
        hook.get_conn()
        mock_connect.assert_called_with(
            host="test_host",
            port=10000,
            path="/test/endpoint",
            scheme="https",
            user="test_login",
            password="test_password",
            context={},
            ssl_verify_cert=False,
        )

    def test_get_uri(self):
        db_hook = self.db_hook()
        assert db_hook.get_uri() == "druid://host:1000/druid/v2/sql"

    def test_get_first_record(self):
        statement = "SQL"
        result_sets = [("row1",), ("row2",)]
        self.cur.fetchone.return_value = result_sets[0]

        assert result_sets[0] == self.db_hook().get_first(statement)
        assert self.conn.close.call_count == 1
        assert self.cur.close.call_count == 1
        self.cur.execute.assert_called_once_with(statement)

    def test_get_records(self):
        statement = "SQL"
        result_sets = [("row1",), ("row2",)]
        self.cur.fetchall.return_value = result_sets

        assert result_sets == self.db_hook().get_records(statement)
        assert self.conn.close.call_count == 1
        assert self.cur.close.call_count == 1
        self.cur.execute.assert_called_once_with(statement)

    def test_get_df_pandas(self):
        statement = "SQL"
        column = "col"
        result_sets = [("row1",), ("row2",)]
        self.cur.description = [(column,)]
        self.cur.fetchall.return_value = result_sets
        df = self.db_hook().get_df(statement, df_type="pandas")

        assert column == df.columns[0]
        for i, item in enumerate(result_sets):
            assert item[0] == df.values.tolist()[i][0]
        assert self.conn.close.call_count == 1
        assert self.cur.close.call_count == 1
        self.cur.execute.assert_called_once_with(statement)

    def test_get_df_polars(self):
        statement = "SQL"
        column = "col"
        result_sets = [("row1",), ("row2",)]
        mock_execute = MagicMock()
        mock_execute.description = [(column, None, None, None, None, None, None)]
        mock_execute.fetchall.return_value = result_sets
        self.cur.execute.return_value = mock_execute

        df = self.db_hook().get_df(statement, df_type="polars")
        assert column == df.columns[0]
        assert result_sets[0][0] == df.row(0)[0]
        assert result_sets[1][0] == df.row(1)[0]
