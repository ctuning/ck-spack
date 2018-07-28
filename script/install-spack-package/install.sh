#! /bin/bash

#
# Universal CK installation script for spack packages
#
# See CK LICENSE for licensing details.
# See CK COPYRIGHT for copyright details.
#
# Developer(s):
# - Grigori Fursin, 2018
#

# PACKAGE_DIR
# INSTALL_DIR

# Clean ck-spack.json
CK_SPACK_JSON=${INSTALL_DIR}/ck-spack.json

rm -f ${CK_SPACK_JSON}

# Prepare config.yaml
SPACK_CONFIG=${CK_ENV_TOOL_SPACK}/etc/spack/config.yaml

echo ""
echo "Preparing ${SPACK_CONFIG} ..."
echo ""

mkdir -p ${CK_ENV_TOOL_SPACK}/etc/spack

echo "config:" > ${SPACK_CONFIG}
#echo "  install_tree: $INSTALL_DIR/spack" >> ${SPACK_CONFIG}
echo "  install_tree: ${CK_ENV_TOOL_SPACK_ROOT}/spack" >> ${SPACK_CONFIG}
echo "" >> ${SPACK_CONFIG}
echo "  install_path_scheme: '\${PACKAGE}'" >> ${SPACK_CONFIG}
echo "" >> ${SPACK_CONFIG}
echo "  build_jobs: ${CK_HOST_CPU_NUMBER_OF_PROCESSORS}" >> ${SPACK_CONFIG}

# Preparing installation path
SPACK_CMD="spack install ${SPACK_PACKAGE_NAME}"

if [ "${PACKAGE_VERSION}" != "" ] ; then
  SPACK_CMD="${SPACK_CMD}@${PACKAGE_VERSION}"
fi

if [ "${SPACK_EXTRA_CMD}" != "" ] ; then
  SPACK_CMD="${SPACK_CMD} ${SPACK_EXTRA_CMD}"
fi

echo ""
echo "Invoking \"${SPACK_CMD}\" ..."

${SPACK_CMD}

if [ "${?}" != "0" ] ; then
  echo "Error: spack installation failed!"
  exit 1
fi

# Set ck-spack.json to tell CK that installation was successful
echo "{" > ${CK_SPACK_JSON}
echo "  \"SPACK_ROOT\":\"${CK_ENV_TOOL_SPACK_ROOT}\"," >> ${CK_SPACK_JSON}
echo "  \"SPACK_DIR\":\"${CK_ENV_TOOL_SPACK_ROOT}/spack\"," >> ${CK_SPACK_JSON}
echo "  \"SPACK_SRC\":\"${CK_ENV_TOOL_SPACK}\"," >> ${CK_SPACK_JSON}
echo "  \"SPACK_PACKAGE_NAME\":\"${SPACK_PACKAGE_NAME}\"," >> ${CK_SPACK_JSON}
echo "  \"PACKAGE_VERSION\":\"${PACKAGE_VERSION}\"" >> ${CK_SPACK_JSON}
echo "}" >> ${CK_SPACK_JSON}

return 0
