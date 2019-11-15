# ProductsStoreIdEanGet200ApplicationJsonResponse

Contains a lot of optional attributes. [Examples of different types of products.](../docs/api#product-object-examples) 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** |  | 
**name** | **str** |  | 
**price** | **float** |  | [optional] 
**total_price** | **float** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**pricing_unit** | **str** | Unit for the product price | [optional] 
**package_unit** | **str** | Unit for packaging size | [optional] 
**package_size** | **str** | Package size, numeric value returned as a string | [optional] 
**package_type** | **str** | Freeform field describing the package type | [optional] 
**cost_center_id** | **str** | Cost center ID for the product | [optional] 
**discount_limited** | **bool** | Is the product exempt from discounts | [optional] 
**plussa_limited** | **bool** | Is the product exempt from Plussa discounts | [optional] 
**type** | **str** | Product type. For Citymarket stores products vary between utility and consumer goods. For non-Citymarket stores, all products are considered consumer goods.  | [optional] 
**vat** | **float** |  | [optional] 
**group** | **str** |  | [optional] 
**size** | [**ProductSize**](ProductSize.md) |  | [optional] 
**texts** | [**list[ProductTexts]**](ProductTexts.md) |  | [optional] 
**restrictions** | [**ProductRestrictions**](ProductRestrictions.md) |  | [optional] 
**components** | [**list[BasketItemItemComponents]**](BasketItemItemComponents.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


