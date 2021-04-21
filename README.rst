sgrudah
=======

:Authors:
    lo3k / evillain / Villain_0x1034

OpenShift API based tool to screen OpenShift projects
-----------------------------------------------------

Quickstart
----------

**Enter hextrim project**

.. code-block:: python

    oc project hextrim

**Create user root within project hextrim**

.. code-block:: python

    oc create serviceaccount robot 

**Add a local namespace admin role to user robot**

.. code-block:: python

    oc policy add-role-to-user admin -z robot 

**Add a cluster wide cluster-admin role to user robot**

.. code-block:: python

    oc adm policy add-cluster-role-to-user cluster-admin system:serviceaccount:hextrim:robot

**Patch DeploymentConfig**

.. code-block:: python

    oc patch dc/sgrudah --patch '{"spec":{"template":{"spec":{"serviceAccountName": "robot"}}}}'