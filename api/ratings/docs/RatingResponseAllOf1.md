# RatingResponseAllOf1

Core rating object, sent to APIs as a part of a request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** | Id of the rated object. This id is the external id of the other service.  | 
**target_namespace** | **str** | Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: &#x60;food-products&#x60;.  | 
**created_at** | **datetime** | Generated, date when rating was created | [optional] 
**rating** | **int** | Rating of the rated object. You must define either &#x60;rating&#x60;, &#x60;comment&#x60; or both.  | [optional] 
**ratings** | [**RatingRatings**](RatingRatings.md) |  | [optional] 
**comment** | **str** | Comment for the object. You must define either &#x60;rating&#x60;, &#x60;comment&#x60; or both.  | [optional] 
**author_name** | **str** | Name of the user who created the rating. | [optional] 
**author_role** | **str** | Role of the rating&#39;s author. | 
**reply_requested** | **bool** | Does the author want a reply for their comment. When no comment is given, this should be &#x60;false&#x60;. Default: &#x60;false&#x60;.  | [optional] [default to False]
**published** | **bool** | **Only for moderators+** Indicates if the rating has been published or not. If a rating has been published, it will show up in rating listings. Otherwise the item won&#39;t be returned from the API at all. This value is not returned for normal services. Only moderators and admin roles will see it. Trying to get unpublished rating directly will result to 404.  | [optional] 
**moderated** | **bool** | **Only for moderators+** Indicates if the rating has been moderated or not. If rating has been moderated, this value will be set to &#x60;true&#x60;. This value is not returned for normal services. Only moderators and admin roles will see it.  | [optional] 
**category** | **str** | Category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.  | [optional] 
**sub_category** | **str** | Sub category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.  | [optional] 
**name** | **str** | Name of the rated object. For moderation purposes. Only moderators and admin roles will see it.  | [optional] 
**url** | **str** | URL of the rated object. For moderation purposes. Only moderators and admin roles will see it.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


