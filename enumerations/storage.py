
from . import _ok as base

class Storage(base.sendhelp):

    method_ClearCookies:str
    method_ClearDataForOrigin:str
    method_ClearDataForStorageKey:str
    method_GetCookies:str
    method_GetStorageKeyForFrame:str
    method_GetUsageAndQuota:str
    method_SetCookies:str
    method_TrackCacheStorageForOrigin:str
    method_TrackCacheStorageForStorageKey:str
    method_TrackIndexedDBForOrigin:str
    method_TrackIndexedDBForStorageKey:str
    method_UntrackCacheStorageForOrigin:str
    method_UntrackCacheStorageForStorageKey:str
    method_UntrackIndexedDBForOrigin:str
    method_UntrackIndexedDBForStorageKey:str
    method_ClearSharedStorageEntries:str
    method_ClearTrustTokens:str
    method_DeleteSharedStorageEntry:str
    method_DeleteStorageBucket:str
    method_GetInterestGroupDetails:str
    method_GetSharedStorageEntries:str
    method_GetSharedStorageMetadata:str
    method_GetTrustTokens:str
    method_OverrideQuotaForOrigin:str
    method_ResetSharedStorageBudget:str
    method_RunBounceTrackingMitigations:str
    method_SetAttributionReportingLocalTestingMode:str
    method_SetAttributionReportingTracking:str
    method_SetInterestGroupTracking:str
    method_SetSharedStorageEntry:str
    method_SetSharedStorageTracking:str
    method_SetStorageBucketTracking:str

    event_CacheStorageContentUpdated:str
    event_CacheStorageListUpdated:str
    event_IndexedDBContentUpdated:str
    event_IndexedDBListUpdated:str
    event_InterestGroupAccessed:str
    event_SharedStorageAccessed:str
    event_StorageBucketCreatedOrUpdated:str
    event_StorageBucketDeleted:str
    event_AttributionReportingSourceRegistered:str

    type_InterestGroupAccessType:str
    type_InterestGroupAd:str
    type_InterestGroupDetails:str
    type_SerializedStorageKey:str
    type_SharedStorageAccessParams:str
    type_SharedStorageAccessType:str
    type_SharedStorageEntry:str
    type_SharedStorageMetadata:str
    type_SharedStorageReportingMetadata:str
    type_SharedStorageUrlWithMetadata:str
    type_StorageBucket:str
    type_StorageBucketInfo:str
    type_StorageBucketsDurability:str
    type_StorageType:str
    type_UsageForType:str
    type_AttributionReportingAggregationKeysEntry:str
    type_AttributionReportingFilterDataEntry:str
    type_AttributionReportingSourceRegistration:str
    type_AttributionReportingSourceRegistrationResult:str
    type_AttributionReportingSourceType:str
    type_SignedInt64AsBase10:str
    type_TrustTokens:str
    type_UnsignedInt128AsBase16:str
    type_UnsignedInt64AsBase10:str

    def __init__(self):
        super().__init__()

    
