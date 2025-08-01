 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.


.. NOTE TO CONTRIBUTORS:
   Please, only add notes to the Changelog just below the "Changelog" header when there are some breaking changes
   and you want to add an explanation to the users on how they are supposed to deal with them.
   The changelog is updated and maintained semi-automatically by release manager.

``apache-airflow-providers-docker``


Changelog
---------


4.4.2
.....

Misc
~~~~

* ``Add Python 3.13 support for Airflow. (#46891)``
* ``Remove type ignore across codebase after mypy upgrade (#53243)``
* ``Remove upper-binding for "python-requires" (#52980)``
* ``Temporarily switch to use >=,< pattern instead of '~=' (#52967)``
* ``Move all BaseHook usages to version_compat in Docker (#52802)``

Doc-only
~~~~~~~~

* ``docs: Correct TaskFlow capitalization in documentation (#51794)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Deprecate decorators from Core (#53629)``
   * ``Cleanup mypy ignore in docker provider where possible (#53273)``
   * ``Make dag_version_id in TI non-nullable (#50825)``

4.4.1
.....

Misc
~~~~

* ``Move 'BaseHook' implementation to task SDK (#51873)``
* ``Allow templating of mounts parameter in DockerOperator   (#52451)``
* ``Provider Migration: Update docker for Airflow 3.0 compatibility (#52465)``
* ``Drop support for Python 3.9 (#52072)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Make sure all test version imports come from test_common (#52425)``
   * ``Removed pytest.mark_db_test from the docker provider completely (#52027)``
   * ``Always create serdag in dagmaker fixture (#50359)``
   * ``Prepare release for June 2025 provider wave (#51724)``

4.4.0
.....

.. note::
    This release of provider is only available for Airflow 2.10+ as explained in the
    Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>_.

Misc
~~~~

* ``Remove AIRFLOW_2_10_PLUS conditions (#49877)``
* ``Bump min Airflow version in providers to 2.10 (#49843)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Update description of provider.yaml dependencies (#50231)``
   * ``Avoid committing history for providers (#49907)``
   * ``Prepare docs for Apr 3rd wave of providers (#49338)``
   * ``Use contextlib.suppress(exception) instead of try-except-pass and add SIM105 ruff rule (#49251)``
   * ``remove superfluous else block (#49199)``

4.3.1
.....

Misc
~~~~

* ``Make '@task' import from airflow.sdk (#48896)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Remove unnecessary entries in get_provider_info and update the schema (#48849)``
   * ``Remove fab from preinstalled providers (#48457)``
   * ``Improve documentation building iteration (#48760)``
   * ``Prepare docs for Apr 1st wave of providers (#48828)``
   * ``Simplify tooling by switching completely to uv (#48223)``
   * ``Upgrade ruff to latest version (#48553)``

4.3.0
.....

Features
~~~~~~~~

* ``make docker swarm service name customizable (#47957)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Upgrade providers flit build requirements to 3.12.0 (#48362)``
   * ``Move airflow sources to airflow-core package (#47798)``
   * ``Remove links to x/twitter.com (#47801)``

4.2.1
.....

Misc
~~~~

* ``Upgrade flit to 3.11.0 (#46938)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Move tests_common package to devel-common project (#47281)``
   * ``Improve documentation for updating provider dependencies (#47203)``
   * ``Add legacy namespace packages to airflow.providers (#47064)``
   * ``Remove extra whitespace in provider readme template (#46975)``

4.2.0
.....

.. note::
  This version has no code changes. It's released due to yank of previous version due to packaging issues.

4.1.0
.....

Features
~~~~~~~~

* ``Feat: support docker operator arg 'labels' (#46643)``

Bug Fixes
~~~~~~~~~

* ``Fix f-string ruff static check (#46813)``
* ``Using quotes for file path in find command (#46795)``
* ``Update DockerSwarmOperator auto_remove to align with DockerOperator (#45745)``

Misc
~~~~

* ``Using env for file path in find command (#46809)``
* ``AIP-72: Support better type-hinting for Context dict in SDK  (#45583)``
* ``Move Literal alias into TYPE_CHECKING block (#45345)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Move provider_tests to unit folder in provider tests (#46800)``
   * ``Removed the unused provider's distribution (#46608)``
   * ``Fix doc issues found with recent moves (#46372)``
   * ``Move Docker Provider to the New Structure (#46097)``

4.0.0
.....

.. note::
  This release of provider is only available for Airflow 2.9+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Breaking changes
~~~~~~~~~~~~~~~~

.. warning::
  All deprecated classes, parameters and features have been removed from the Kubernetes provider package.
  The following breaking changes were introduced:

  * Decorators
     * Deprecated parameter ``use_dill`` was removed. Please use ``serializer='dill'`` instead.
  * Operators
     * Deprecated parameter ``use_dill`` was removed. Please use ``serializer='dill'`` instead.
     * Deprecated parameter ``skip_exit_code`` was removed. Please use ``skip_on_exit_code`` instead.
     * Deprecated method ``get_hook()`` was removed. Please use ``hook`` property instead.

* ``Remove Provider Deprecations in Docker (#44583)``

Misc
~~~~

* ``Bump minimum Airflow version in providers to Airflow 2.9.0 (#44956)``
* ``fix docker documentation auth url (#44112)``
* ``Update DAG example links in multiple providers documents (#44034)``


.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Correct new changelog breaking changes header (#44659)``
   * ``Use Python 3.9 as target version for Ruff & Black rules (#44298)``

.. Review and move the new changes to one of the sections above:
   * ``Update path of example dags in docs (#45069)``

3.14.1
......

Bug Fixes
~~~~~~~~~

* ``Fix logs with leading spaces in the Docker operator (#33692) (#43840)``

Misc
~~~~

* ``Move python operator to Standard provider (#42081)``


.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Split providers out of the main "airflow/" tree into a UV workspace project (#42505)``

3.14.0
......

Features
~~~~~~~~

* ``Add logging device and logging device options to DockerSwarmOperator (#41416)``
* ``Add retrieve output docker swarm operator (#41531)``


.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):

3.13.0
......

.. note::
  This release of provider is only available for Airflow 2.8+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Misc
~~~~

* ``feat(docker): Replace 'use_dill' with 'serializer' (#41356)``
* ``Bump minimum Airflow version in providers to Airflow 2.8.0 (#41396)``


.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):

3.12.3
......

Bug Fixes
~~~~~~~~~

* ``DockerSwarmOperator: Support line breaks in service logs (#40705)``


.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):

3.12.2
......

Bug Fixes
~~~~~~~~~

* ``DockerOperator TaskFlow - correct argyments in python command (#39620)``

Misc
~~~~

* ``Improve logging behavior of DockerOperator (#40489)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Enable enforcing pydocstyle rule D213 in ruff. (#40448)``

3.12.1
......

Misc
~~~~

* ``Bump minimum docker version to 7.1.0 (#39839)``

3.12.0
......

Features
~~~~~~~~

* ``Add args to docker service ContainerSpec (#39464)``
* ``Add support to define Resources on DockerSwarmOperator (#39027)``

Misc
~~~~

* ``Faster 'airflow_version' imports (#39552)``
* ``Simplify 'airflow_version' imports (#39497)``
* ``Limit requests in botocore upgrade test (#39747)``
* ``Pin requests due to incompatibility with docker-py (#39740)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Reapply templates for all providers (#39554)``

3.11.0
......

.. note::
  This release of provider is only available for Airflow 2.7+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Misc
~~~~

* ``Bump minimum Airflow version in providers to Airflow 2.7.0 (#39240)``

3.10.0
......

.. note::
  The standard ``DOCKER_HOST`` environment variable now overrides the default value
  of the ``docker_url`` parameter when set. If ``DOCKER_HOST`` is set but you want to
  use the previous default value, then you must explicitly set
  ``docker_url="unix://var/run/docker.sock"`` in the ``DockerOperator`` constructor
  or ``@task.docker`` decorator.

Features
~~~~~~~~

* ``Improve 'DockerOperator' to support multiple Docker hosts (#38466)``

Bug Fixes
~~~~~~~~~

* ``Fix deprecated 'DockerOperator' operator arguments in 'MappedOperator' (#38379)``

Misc
~~~~

* ``Remove redundant compatibility usage of importlib_metadata (#38368)``
* ``DockerOperator: use DOCKER_HOST as default for docker_url (#38387)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``docs: add timeout description to DockerOperator. (#38710)``
   * ``Fix TRY002 for docker swarm operator (#38768)``
   * ``Bump ruff to 0.3.3 (#38240)``

3.9.2
.....

Bug Fixes
~~~~~~~~~

* ``Fix construct 'docker.TLSConfig' for 'docker>=7' (#37481)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Add comment about versions updated by release manager (#37488)``
   * ``Prepare docs 1st wave of Providers February 2024 (#37326)``
   * ``Add docs for RC2 wave of providers for 2nd round of Jan 2024 (#37019)``
   * ``Revert "Provide the logger_name param in providers hooks in order to override the logger name (#36675)" (#37015)``
   * ``Prepare docs 2nd wave of Providers January 2024 (#36945)``
   * ``Provide the logger_name param in providers hooks in order to override the logger name (#36675)``
   * ``Prepare docs 1st wave of Providers January 2024 (#36640)``
   * ``Speed up autocompletion of Breeze by simplifying provider state (#36499)``

3.9.1
.....

Bug Fixes
~~~~~~~~~

* ``Allow DockerOperator.skip_on_exit_code to be zero (#36360)``

Misc
~~~~

* ``Remove remaining Airflow 2.5 backcompat code from Docker Provider (#36325)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):

3.9.0
.....

.. note::
  This release of provider is only available for Airflow 2.6+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Bug Fixes
~~~~~~~~~

* ``Fix 'enable_logging=True' not working in 'DockerSwarmOperator' (#35677)``
* ``Fix broken log streaming from #35677 (#36127)``

Misc
~~~~

* ``Bump minimum Airflow version in providers to Airflow 2.6.0 (#36017)``
* ``Follow BaseHook connection fields method signature in child classes (#36086)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Update information about links into the provider.yaml files (#35837)``
   * ``Prepare docs 1st wave of Providers December 2023 (#36112)``

3.8.2
.....

Misc
~~~~

* ``Refactor docker operator attribute validations and docs (#35571)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Use reproducible builds for providers (#35693)``
   * ``Fix and reapply templates for provider documentation (#35686)``

3.8.1
.....

Bug Fixes
~~~~~~~~~

* ``fix '_DockerDecoratedOperator' module type attribute pickle error (#35293)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Prepare docs 3rd wave of Providers October 2023 (#35187)``
   * ``Pre-upgrade 'ruff==0.0.292' changes in providers (#35053)``
   * ``D401 Support - Providers: DaskExecutor to Github (Inclusive) (#34935)``
   * ``Prepare docs 3rd wave of Providers October 2023 - FIX (#35233)``

3.8.0
.....

.. note::
  This release of provider is only available for Airflow 2.5+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Features
~~~~~~~~

* ``Add ulimits parameter to DockerOperator (#34284)``

Misc
~~~~

* ``Bump min airflow version of providers (#34728)``
* ``Deprecate get_hook method in DockerOperator (#34432)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Refactor consolidate import from io in providers (#34378)``
   * ``Refactor usage of str() in providers (#34320)``
   * ``Refactor: Consolidate import textwrap in providers (#34220)``

3.7.5
.....

Misc
~~~~

* ``Cleanup Docker operator logging (#33914)``
* ``Replace sequence concatenation by unpacking in Airflow providers (#33933)``
* ``Use literal dict instead of calling dict() in providers (#33761)``
* ``Replace type func by isinstance in DockerOperator (#33759)``

3.7.4
.....

Misc
~~~~

* ``Refactor: Improve detection of duplicates and list sorting (#33675)``
* ``Simplify conditions on len() in other providers (#33569)``
* ``Replace repr() with proper formatting (#33520)``

3.7.3
.....

Misc
~~~~

* ``Refactor: Simplify code in providers/docker (#33232)``

3.7.2
.....

Misc
~~~~

* ``Get rid of Python2 numeric relics (#33050)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Prepare docs for July 2023 wave of Providers (RC2) (#32381)``
   * ``Remove spurious headers for provider changelogs (#32373)``
   * ``Prepare docs for July 2023 wave of Providers (#32298)``
   * ``D205 Support - Providers: Databricks to Github (inclusive) (#32243)``
   * ``Improve provider documentation and README structure (#32125)``

3.7.1
.....

.. note::
  This release dropped support for Python 3.7

Misc
~~~~

* ``Remove Python 3.7 support (#30963)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Improve docstrings in providers (#31681)``
   * ``Add D400 pydocstyle check (#31742)``
   * ``Add D400 pydocstyle check - Providers (#31427)``
   * ``Add note about dropping Python 3.7 for providers (#32015)``

3.7.0
.....

.. note::
  This release of provider is only available for Airflow 2.4+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Misc
~~~~

* ``Bump minimum Airflow version in providers (#30917)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Add full automation for min Airflow version for providers (#30994)``
   * ``Use '__version__' in providers not 'version' (#31393)``
   * ``Fixing circular import error in providers caused by airflow version check (#31379)``
   * ``adding docker port expose capability (#30730)``
   * ``Prepare docs for May 2023 wave of Providers (#31252)``
   * ``Use 'AirflowProviderDeprecationWarning' in providers (#30975)``

3.6.0
.....

Features
~~~~~~~~

* ``Add multiple exit code handling in skip logic for 'DockerOperator' and 'KubernetesPodOperator' (#30769)``
* ``In 'DockerOperator', adding an attribute 'tls_verify' to choose whether to validate certificate (#30309) (#30310)``

Misc
~~~~

* ``Deprecate 'skip_exit_code' in 'DockerOperator' and 'KubernetesPodOperator' (#30733)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Fix and augment 'check-for-inclusive-language' CI check (#29549)``
   * ``Remove "boilerplate" from all taskflow decorators (#30118)``
   * ``Add mechanism to suspend providers (#30422)``

3.5.1
.....

Bug Fixes
~~~~~~~~~

* ``fix template_fields in the decorator 'task.docker' (#29586)``

3.5.0
.....

Features
~~~~~~~~

* ``Add correct widgets in Docker Hook (#28700)``
* ``Make docker operators always use 'DockerHook' for API calls (#28363)``
* ``Skip DockerOperator task when it returns a provided exit code (#28996)``

Bug Fixes
~~~~~~~~~

* ``Fix label name for 'reauth' field in Docker Connection (#28974)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Prepare docs for Jan 2023 mid-month wave of Providers (#28929)``

3.4.0
.....

Features
~~~~~~~~

* ``add hostname argument to DockerOperator (#27822)``
* ``Move min airflow version down for Docker Provider to 2.3.0 (#28648)``

3.3.0
.....

.. note::
  This release of provider is only available for Airflow 2.3+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Misc
~~~~

* ``Move min airflow version to 2.3.0 for all providers (#27196)``

Features
~~~~~~~~

* ``Add ipc_mode for DockerOperator (#27553)``
* ``Add env-file parameter to Docker Operator (#26951)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Update old style typing (#26872)``
   * ``Enable string normalization in python formatting - providers (#27205)``

3.2.0
.....

Features
~~~~~~~~

* ``Add logging options to docker operator (#26653)``
* ``Add pre-commit hook for custom_operator_name (#25786)``
* ``Implement ExternalPythonOperator (#25780)``

Bug Fixes
~~~~~~~~~

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Apply PEP-563 (Postponed Evaluation of Annotations) to non-core airflow (#26289)``

3.1.0
.....

Features
~~~~~~~~

* ``Force-remove container after DockerOperator execution (#23160)``

Bug Fixes
~~~~~~~~~

* ``'DockerOperator' fix cli.logs giving character array instead of string (#24726)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Move provider dependencies to inside provider folders (#24672)``
   * ``Remove 'hook-class-names' from provider.yaml (#24702)``
   * ``Clean up task decorator type hints and docstrings (#24667)``

3.0.0
.....

Breaking changes
~~~~~~~~~~~~~~~~

.. note::
  This release of provider is only available for Airflow 2.2+ as explained in the
  `Apache Airflow providers support policy <https://github.com/apache/airflow/blob/main/PROVIDERS.rst#minimum-supported-version-of-airflow-for-community-managed-providers>`_.

Misc
~~~~

* ``Remove 'xcom_push' from 'DockerOperator' (#23981)``
* ``docker new system test (#23167)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Add explanatory note for contributors about updating Changelog (#24229)``
   * ``Prepare docs for May 2022 provider's release (#24231)``
   * ``Update package description to remove double min-airflow specification (#24292)``

2.7.0
.....

Features
~~~~~~~~

* ``Add 'device_requests' parameter to 'DockerOperator' (#23554)``

Bug Fixes
~~~~~~~~~

* ``Fix new MyPy errors in main (#22884)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Use new Breese for building, pulling and verifying the images. (#23104)``

2.6.0
.....

Features
~~~~~~~~

* ``Add timeout parameter to 'DockerOperator' (#22502)``

2.5.2
.....

Bug Fixes
~~~~~~~~~

* ``Fix mistakenly added install_requires for all providers (#22382)``

Misc
~~~~

* ``Correct 'multiple_outputs' param descriptions mentioning lists/tuples (#22371)``

2.5.1
.....

Bug Fixes
~~~~~~~~~

* ``Avoid trying to kill container when it did not succeed for Docker (#22145)``

Misc
~~~~~

* ``Add Trove classifiers in PyPI (Framework :: Apache Airflow :: Provider)``

2.5.0
.....

Features
~~~~~~~~

* ``added docker network_mode options (#21986)``

Misc
~~~~

* ``Support for Python 3.10``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Change default python executable to python3 for docker decorator (#21973)``
   * ``Switch to Debian 11 (bullseye) as base for our dockerfiles (#21378) (#21875)``
   * ``Revert "Switch to Debian 11 (bullseye) as base for our dockerfiles (#21378)" (#21874)``
   * ``Switch to Debian 11 (bullseye) as base for our dockerfiles (#21378)``

2.4.1
.....

Bug Fixes
~~~~~~~~~

* ``Fixes Docker xcom functionality (#21175)``
* ``Fix docker behaviour with byte lines returned (#21429)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Add optional features in providers. (#21074)``
   * ``Remove ':type' lines now sphinx-autoapi supports typehints (#20951)``
   * ``Rewrite the task decorator as a composition (#20868)``
   * ``Add documentation for January 2021 providers release (#21257)``

2.4.0
.....

Features
~~~~~~~~

* ``Allow DockerOperator's image to be templated (#19997)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Fix mypy docker provider (#20235)``
   * ``Update documentation for November 2021 provider's release (#19882)``
   * ``Remove remaining 'pylint: disable' comments (#19541)``
   * ``Fix MyPy errors for Airflow decorators (#20034)``
   * ``Use typed Context EVERYWHERE (#20565)``
   * ``Fix template_fields type to have MyPy friendly Sequence type (#20571)``
   * ``Even more typing in operators (template_fields/ext) (#20608)``
   * ``Update documentation for provider December 2021 release (#20523)``

2.3.0
.....

Features
~~~~~~~~

* ``Add support of placement in the DockerSwarmOperator (#18990)``

Bug Fixes
~~~~~~~~~

* ``Fixup string concatenations (#19099)``
* ``Remove the docker timeout workaround (#18872)``


Other
~~~~~

   * ``Move docker decorator example dag to docker provider (#18739)``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):

2.2.0
.....

Features
~~~~~~~~

* ``Add a Docker TaskFlow decorator (#15330)``

This version of Docker Provider has a new feature - TaskFlow decorator that only works in Airflow 2.2.
If you try to use the decorator in pre-Airflow 2.2 version you will get an error:

.. code-block:: text

    AttributeError: '_TaskDecorator' object has no attribute 'docker'

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Static start_date and default arg cleanup for misc. provider example DAGs (#18597)``
   * ``Cope with '@task.docker' decorated function not returning anything (#18463)``

2.1.1
.....

Features
~~~~~~~~

* ``Add support for configs, secrets, networks and replicas for DockerSwarmOperator (#17474)``

Misc
~~~~

* ``Optimise connection importing for Airflow 2.2.0``

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Update description about the new ''connection-types'' provider meta-data (#17767)``
   * ``Import Hooks lazily individually in providers manager (#17682)``

2.1.0
.....

Features
~~~~~~~~

* ``Adds option to disable mounting temporary folder in DockerOperator (#16932)``

Bug Fixes
~~~~~~~~~

* ``[FIX] Docker provider - retry docker in docker (#17061)``
* ``fix string encoding when using xcom / json (#13536)``
* if ``xcom_all`` is set to ``False``, only the last line of the log (separated by ``\n``) will be
  included in the XCom value

The ``DockerOperator`` in version 2.0.0 did not work for remote Docker Engine or Docker-In-Docker case.
That was an unintended side effect of #15843 that has been fixed in #16932. There is a fallback mode
which will make Docker Operator works with warning and you will be able to remove the warning by
using the new parameter to disable mounting the folder.

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Removes pylint from our toolchain (#16682)``
   * ``Prepare documentation for July release of providers. (#17015)``
   * ``Fixed wrongly escaped characters in amazon's changelog (#17020)``
   * ``Prepares documentation for RC2 release of Docker Provider (#17066)``
   * ``Updating Docker example DAGs to use XComArgs (#16871)``

2.0.0
.....

Breaking changes
~~~~~~~~~~~~~~~~

* ``Auto-apply apply_default decorator (#15667)``

.. warning:: Due to apply_default decorator removal, this version of the provider requires Airflow 2.1.0+.
   If your Airflow version is < 2.1.0, and you want to install this provider version, first upgrade
   Airflow to at least version 2.1.0. Otherwise your Airflow package version will be upgraded
   automatically and you will have to manually run ``airflow upgrade db`` to complete the migration.

* ``Replace DockerOperator's 'volumes' arg for 'mounts' (#15843)``

The ``volumes`` parameter in
``airflow.providers.docker.operators.docker.DockerOperator`` and
``airflow.providers.docker.operators.docker_swarm.DockerSwarmOperator``
was replaced by the ``mounts`` parameter, which uses the newer
`mount syntax <https://docs.docker.com/storage/>`__ instead of ``--bind``.

.. Below changes are excluded from the changelog. Move them to
   appropriate section above if needed. Do not delete the lines(!):
   * ``Updated documentation for June 2021 provider release (#16294)``
   * ``More documentation update for June providers release (#16405)``
   * ``Remove class references in changelogs (#16454)``
   * ``Synchronizes updated changelog after buggfix release (#16464)``

1.2.0
.....

Features
~~~~~~~~

* ``Entrypoint support in docker operator (#14642)``
* ``Add PythonVirtualenvDecorator to TaskFlow API (#14761)``
* ``Support all terminus task states in Docker Swarm Operator (#14960)``


1.1.0
.....

Features
~~~~~~~~

* ``Add privileged option in DockerOperator (#14157)``

1.0.2
.....

Bug fixes
~~~~~~~~~

* ``Corrections in docs and tools after releasing provider RCs (#14082)``

1.0.1
.....

Updated documentation and readme files.

Bug fixes
~~~~~~~~~

* ``Remove failed DockerOperator tasks with auto_remove=True (#13532) (#13993)``
* ``Fix error on DockerSwarmOperator with auto_remove True (#13532) (#13852)``


1.0.0
.....

Initial version of the provider.
