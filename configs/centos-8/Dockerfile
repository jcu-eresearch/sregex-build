FROM centos:8
MAINTAINER "JCU eResearch Centre" <eresearch.nospam@jcu.edu.au>

# Install required packages for building / extracting
RUN dnf install -y \
  rpm-build \
  rpmdevtools \
  dnf-plugins-core \
  rsync

# Create directory structure for building
RUN rpmdev-setuptree

# 1. Build
# 2. Test
# 3. Copy the RPMs back to the host volume
CMD spectool -g -R /app/sregex.spec && \
  dnf builddep -y /app/sregex.spec && \
  rpmbuild -ba /app/sregex.spec && \
  dnf install -y ~/rpmbuild/RPMS/x86_64/sregex-*.rpm && \
  sregex-cli 'a|ab' 'blab' && \
  rsync --no-relative -vahu ~/rpmbuild/RPMS ~/rpmbuild/SRPMS /app/build/centos-8
