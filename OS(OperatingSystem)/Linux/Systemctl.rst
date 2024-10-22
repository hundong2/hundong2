Systemctl Command Reference
===========================

Introduction
------------

This document provides a reference for the `systemctl` command, which is used to introspect and control the state of the `systemd` system and service manager.

Basic Commands
--------------

Starting a Service

To start a service, use the following command:

.. code-block:: bash

    systemctl start <service-name>
    
Stopping a Service

To stop a service, use the following command:

.. code-block:: bash

    systemctl stop <service-name>

Restarting a Service

~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    systemctl restart <service-name>

Checking the Status of a Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check the status of a service, use the following command:

.. code-block:: bash

    systemctl status <service-name>

Enabling a Service at Boot
~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable a service to start at boot, use the following command:

.. code-block:: bash

    systemctl enable <service-name>

Disabling a Service at Boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To disable a service from starting at boot, use the following command:

.. code-block:: bash

    systemctl disable <service-name>

Conclusion
----------

This document covered the basic usage of the `systemctl` command. For more detailed information, refer to the `systemctl` man pages or the official `systemd` documentation.