# SearchGroupedGet200ApplicationJsonResponseStoresResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**id** | **str** | Store identifier | 
**name** | **str** |  | 
**chain_id** | **str** |  | 
**chain_independent** | **bool** | &#x60;true&#x60;, if store does not belong to \&quot;kcitymarket\&quot;, \&quot;ksupermarket\&quot;, \&quot;kmarket\&quot; or \&quot;nokm\&quot; chains, e.g. K-Myllypuro.  | 
**chainless_name** | **str** | Store name without the chain name | 
**address** | **str** |  | [optional] 
**store_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**municipality** | **str** |  | [optional] 
**municipality_swedish** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**shopping_center** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**phone_number_pricing** | **str** |  | [optional] 
**service_phone_number** | **str** |  | [optional] 
**service_phone_number_info** | **str** | Mixed information, may include pricing | [optional] 
**service_phone_number_pricing** | **str** |  | [optional] 
**kruoka_url_slug** | **str** |  | [optional] 
**prices_available** | **bool** | &#x60;true&#x60; if Mobile Scan price data is available, &#x60;false&#x60; otherwise  | [optional] 
**business_unit_ids** | **list[str]** | All alternative identifiers, always contains at least the one in the Id field  | 
**branch_code** | **int** |  | 
**opening_hours** | [**list[StoreOpeningHours]**](StoreOpeningHours.md) |  | 
**shopkeeper** | [**StoreShopkeeper**](StoreShopkeeper.md) |  | [optional] 
**coordinate** | [**StoreCoordinate**](StoreCoordinate.md) |  | 
**delivery** | [**StoreDelivery**](StoreDelivery.md) |  | 
**service_ids** | **list[float]** | List of identifiers for services provided by the store  | [optional] 
**sort** | **list[float]** | Only present, if the results are sorted by distance.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


