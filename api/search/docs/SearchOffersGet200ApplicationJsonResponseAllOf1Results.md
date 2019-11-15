# SearchOffersGet200ApplicationJsonResponseAllOf1Results

See payload description for possible category IDs. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**id** | **str** | Offer identifier | 
**name** | **str** | Offer name | 
**product_name** | **str** | Product name | 
**eans** | **list[str]** | List of offer product eans. Note that this field sometimes contains garbage data! Make sure you check the with some validation logic before use (i.e. check that the eans have non-zero length, contain only characters in 0-9 range).  | [optional] 
**brand** | **str** | Product brand name | [optional] 
**is_pirkka_product** | **bool** | True, if this is Pirkka product. | 
**is_plussa_offer** | **bool** | True, if this is Plussa offer. | 
**normal_price** | **str** | Normal price | 
**additional_info** | **str** | Discounted price / kg | 
**price** | **str** | Discounted price / unit | 
**unit** | **str** | Product count for discount | 
**categories** | [**list[ArticleOldCategories]**](ArticleOldCategories.md) | Associated categories. | 
**chains** | **list[str]** | List of chains where this offer is valid. Empty list, if this is store specific offer.  | 
**stores** | **list[str]** | List of stores where this offer is valid. Empty list, if this is chain specific offer.  | 
**source** | **str** | Indicates whether this is chain, store or regional offer. Possible values \&quot;chain\&quot;, \&quot;store and \&quot;regional\&quot;.  | 
**url** | **str** | K-ruoka.fi url of this offer. | [optional] 
**image** | **str** | Offer image url. See [imgix Documentation](https://docs.imgix.com/apis/url) for available image resize parameters. You should always scale the image down to desired size.  | [optional] 
**valid_from** | **str** | Date when the offer is made valid. | 
**visible_from** | **str** | Date when the offer can be published. | 
**visible_to** | **str** | Date when the offer is made invalid. | 
**sort** | **list[float]** | Only present, if the results are sorted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


