# RatingSummary

Summary of ratings for the given target.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** | Id of the rated object. This id is the external id of the other service.  | 
**target_namespace** | **str** | Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: &#x60;food-products&#x60;.  | 
**category** | **str** | Category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.  | [optional] 
**sub_category** | **str** | Sub category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.  | [optional] 
**comment_count** | **int** | Total number of published comments given to the given target, includes only published comments.  | 
**total_comment_count** | **int** | Total number of comments given to the given target, includes published and unpublished comments.  | [optional] 
**average** | **float** | Average rating of the rated object. | 
**averages** | [**RatingSummaryAverages**](RatingSummaryAverages.md) |  | [optional] 
**distribution** | [**RatingSummaryDistribution**](RatingSummaryDistribution.md) |  | 
**distributions** | [**RatingSummaryDistributions**](RatingSummaryDistributions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


