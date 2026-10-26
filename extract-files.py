#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/oplus',
    'vendor/oneplus/sm8450-common',
    'hardware/qcom-caf/sm8450',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
]

blob_fixups: blob_fixups_user_type = {
    ('odm/bin/hw/vendor.oplus.hardware.cammidasservice-V1-service', 'vendor/lib64/libmidasserviceintf_aidl.so'): blob_fixup()
        .replace_needed('android.frameworks.stats-V1-ndk_platform.so', 'android.frameworks.stats-V1-ndk.so'),
    'odm/etc/camera/CameraHWConfiguration.config': blob_fixup()
        .regex_replace('SystemCamera =  0;  0;  0;  1;  0;  1;', 'SystemCamera =  0;  0;  0;  0;  0;  1;'),
    (
        'odm/lib64/camera/components/com.oplus.node.eispreview.so',
        'odm/lib64/libOPAlgoCamSinglePortrait.so',
        'odm/lib64/libVDBayerHDR.so',
        'odm/lib64/libaisd.so',
        'odm/lib64/libarc_eis.so',
        'odm/lib64/libarcsoft_dual_sat.so',
        'odm/lib64/libarcsoft_triple_sat.so',
        'odm/lib64/libarcsoft_triple_zoomtranslator.so',
    ): blob_fixup()
        .add_needed('libc++_shared.so'),
    ('odm/lib64/libOGLManager.so', 'odm/lib64/libOPAlgoCamFaceBeautyCap.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'odm/lib64/libarcsoft_mcxmflpolicy.so': blob_fixup()
        .add_needed('libc++.so'),
    ('odm/lib64/libaiboost_hexagon.so', 'odm/lib64/libarcsoft_high_dynamic_range_v4.so'): blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open')
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_control')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf')
        .clear_symbol_version('remote_register_buf_attr'),
    ('odm/lib64/libCOppLceTonemapAPI.so', 'odm/lib64/libCS.so', 'odm/lib64/libSuperRaw.so', 'odm/lib64/libaps_frame_registration.so', 'odm/lib64/libyuv2.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'odm/lib64/vendor.oplus.hardware.sendextcamcmd-V1-service-impl.so': blob_fixup()
        .replace_needed('vendor.oplus.hardware.sendextcamcmd-V2-ndk_platform.so', 'vendor.oplus.hardware.sendextcamcmd-V2-ndk.so'),
    (
        'vendor/bin/hw/vendor.qti.camera.provider@2.7-service_64',
        'vendor/lib64/camx.device@3.4-ext-impl.so',
        'vendor/lib64/camx.device@3.5-ext-impl.so',
        'vendor/lib64/camx.device@3.6-ext-impl.so',
        'vendor/lib64/camx.provider@2.4-external.so',
        'vendor/lib64/camx.provider@2.4-impl.so',
        'vendor/lib64/camx.provider@2.4-legacy.so',
        'vendor/lib64/camx.provider@2.5-external.so',
        'vendor/lib64/camx.provider@2.5-legacy.so',
        'vendor/lib64/camx.provider@2.6-legacy.so',
        'vendor/lib64/camx.provider@2.7-legacy.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V2-ndk_platform.so', 'vendor.qti.hardware.display.config-V2-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'udon',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()
