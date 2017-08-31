sregex Packaging
================

.. image:: https://travis-ci.org/jcu-eresearch/sregex-build.svg?branch=master
   :target: https://travis-ci.org/jcu-eresearch/sregex-build

This packages `sregex <https://github.com/openresty/sregex>`_ within RPMs.

We currently support the following OSes:

* CentOS/RHEL 6 (x86_64)
* CentOS/RHEL 7 (x86_64)

Building packages
-----------------

#. Ensure `Docker <https://docs.docker.com/>`_ and `Docker Compose
   <https://docs.docker.com/compose>`_ are installed.

#. Run the following::

       git clone https://github.com/jcu-eresearch/sregex-build.git
       cd sregex-build
       docker-compose up

#. Enjoy your new RPMs, available in the `build/` directory.

If you're not into Docker, then you can manually run the build steps inside
the corresponding ``Dockerfile`` on your own EL machine, ensuring that you set
up your build environment first. You can follow the respective ``Dockerfile``
in the ``configs/`` area and its ``RUN`` commands.
