#
# Copyright (C) 2021-2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Include the common OEM chipset BoardConfig.
include device/oneplus/sm8450-common/BoardConfigCommon.mk

DEVICE_PATH := device/oneplus/udon

# Assert
TARGET_OTA_ASSERT_DEVICE := udon,OP5961L1,CPH2487

# Display
TARGET_SCREEN_DENSITY := 560

# HIDL
DEVICE_MANIFEST_FILE += $(DEVICE_PATH)/manifest.xml

# Partitions - ACTUAL VALUES FROM YOUR DEVICE
BOARD_BOOTIMAGE_PARTITION_SIZE := 201326592
BOARD_VENDOR_BOOTIMAGE_PARTITION_SIZE := 201326592
BOARD_DTBOIMG_PARTITION_SIZE := 25165824
BOARD_RECOVERYIMAGE_PARTITION_SIZE := 104857600

# Super Partition
BOARD_SUPER_PARTITION_SIZE := 15032385536
BOARD_SUPER_PARTITION_GROUPS := qti_dynamic_partitions
BOARD_QTI_DYNAMIC_PARTITIONS_PARTITION_LIST := system system_ext product vendor vendor_dlkm odm
# Super partition is 14GB, leave some margin for metadata
BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 15028191232

# Userdata
BOARD_USERDATAIMAGE_PARTITION_SIZE := 108616806400

# Metadata
BOARD_USES_METADATA_PARTITION := true

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Recovery
TARGET_RECOVERY_DENSITY := xxhdpi
TARGET_RECOVERY_UI_MARGIN_HEIGHT := 126

# Verified Boot
BOARD_AVB_MAKE_VBMETA_IMAGE_ARGS += --flags 3

# Include the proprietary files BoardConfig.
include vendor/oneplus/udon/BoardConfigVendor.mk
