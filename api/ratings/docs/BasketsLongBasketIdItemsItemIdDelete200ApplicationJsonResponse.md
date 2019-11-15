# BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_id** | **str** | Long or global id of the shopping basket. Equal to &#x60;{longBasketId}&#x60;. This is unique across the system.  | [optional] 
**short_id** | **str** | Shorter id of the shopping basket which must be convenient for users. **Note:** This is unique **per shop**, not globally unique.  | [optional] 
**store_id** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**total_price** | **float** |  | [optional] 
**token** | **str** |  | [optional] 
**checkout_done** | **bool** |  | [optional] 
**items** | [**list[BasketItems]**](BasketItems.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


