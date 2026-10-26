#
# Copyright (C) 2021-2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from udon device
$(call inherit-product, device/oneplus/udon/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_udon
PRODUCT_DEVICE := udon
PRODUCT_MANUFACTURER := OnePlus
PRODUCT_BRAND := OnePlus
PRODUCT_MODEL := CPH2487

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="qssi-user 16 BP2A.250605.015 1788248988419 release-keys" \
    BuildFingerprint=OnePlus/CPH2487/OP5961L1:16/BP2A.250605.015/T.R4T3.1ec16aa_6c695f_698c49:user/release-keys \
    DeviceName=OP5961L1 \
    DeviceProduct=CPH2487 \
    SystemDevice=OP5961L1 \
    SystemName=CPH2487
