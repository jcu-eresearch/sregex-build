FROM centos:7
MAINTAINER "JCU eResearch Centre" <eresearch.nospam@jcu.edu.au>

# Install required packages for building / extracting
RUN yum install -y \
  rpm-build \
  rpmdevtools \
  rsync \
  yum-utils

# Create directory structure for building
RUN rpmdev-setuptree

# 1. Build
# 2. Test
# 3. Copy the RPMs back to the host volume
CMD spectool -g -R /app/sregex.spec && \
  yum-builddep -y /app/sregex.spec && \
  rpmbuild -ba /app/sregex.spec && \
  yum install -y ~/rpmbuild/RPMS/x86_64/sregex-*.rpm && \
  sregex-cli 'a|ab' 'blab' && \
  mkdir -p /app/build/centos-7 && \
  rsync --no-relative -vahu ~/rpmbuild/RPMS ~/rpmbuild/SRPMS /app/build/centos-7
