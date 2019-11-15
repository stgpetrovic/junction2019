# BasketItem

The object is an \"envelope\" for e.g. product. Describes a full item object which backend will return on each GET. The client can't modify the actual item or generated attributes. That's why there's also a partial format of the basket item object, which client can use to create or modify a basket item object. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiplier** | **float** |  | [optional] 
**total_price** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**item** | [**BasketItemItem**](BasketItemItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


