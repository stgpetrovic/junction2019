# Target

Rating target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | Id of the rated object. This id is the external id of the other service.  | 
**namespace** | **str** | Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: &#x60;food-products&#x60;.  | 
**name** | **str** | Name of the rated object. For moderation purposes. Only moderators and admin roles will see it.  | 
**url** | **str** | URL of the rated object. For moderation purposes. Only moderators and admin roles will see it.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


